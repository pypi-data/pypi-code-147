import json
import os

from helios.base import HeliosBase, HeliosTags  # noqa: F401 (ignore lint error: imported but not used)
from helios.base.data_obfuscator import DataObfuscator, DataObfuscatorConfiguration, Rules
from helios.base.tracing.suppress_tracing import SuppressTracing
from helios.instrumentation.pika import RabbitMqMessageContext
from helios.instrumentation.botocore.sqs_message_context import SqsMessageContext
from helios.helios import Helios
from helios.helios_test_trace import HeliosTestTrace
from typing import Any, Callable, Dict, List, Optional, Union
from opentelemetry.util import types
from opentelemetry.propagate import inject, extract
from opentelemetry.context import get_current
from opentelemetry.propagators import textmap
from logging import getLogger

_LOG = getLogger(__name__)


def initialize(
        api_token: str,
        service_name: str,
        enabled: bool = False,
        collector_endpoint: Optional[str] = None,
        test_collector_endpoint: Optional[str] = None,
        sampling_ratio: Optional[Union[float, int, str]] = 1.0,
        environment: Optional[str] = None,
        resource_tags: Optional[Dict[str, Union[bool, float, int, str]]] = None,
        debug: Optional[bool] = False,
        max_queue_size: Optional[int] = None,
        data_obfuscation_allowlist: Rules = None,
        data_obfuscation_blocklist: Rules = None,
        data_obfuscation_hmac_key: Optional[str] = None,
        data_obfuscation_http_headers_allowlist: Optional[List[str]] = None,
        data_obfuscation_http_headers_blocklist: Optional[List[str]] = None,
        excluded_urls: Optional[str] = None,
        metadata_only: Optional[bool] = False,
        **kwargs
) -> Helios:
    auto_init = kwargs.get('auto_init', False)
    if Helios.has_instance() and not auto_init and Helios.get_instance().auto_init:
        _LOG.warning('Helios already auto-initialized')
        return Helios.get_instance()

    data_obfuscation = _get_data_obfuscator_configuration(
        allowlist=data_obfuscation_allowlist,
        blocklist=data_obfuscation_blocklist,
        hmac_key=data_obfuscation_hmac_key,
        http_headers_allowlist=data_obfuscation_http_headers_allowlist,
        http_headers_blocklist=data_obfuscation_http_headers_blocklist
    )

    return Helios.get_instance(
        api_token=api_token,
        service_name=service_name,
        enabled=enabled,
        collector_endpoint=collector_endpoint,
        test_collector_endpoint=test_collector_endpoint,
        sampling_ratio=sampling_ratio,
        environment=environment,
        resource_tags=resource_tags,
        max_queue_size=max_queue_size,
        debug=debug,
        data_obfuscation=data_obfuscation,
        excluded_urls=excluded_urls,
        metadata_only=metadata_only,
        **kwargs
    )


def auto_initialize(_):
    api_token = _get_environment_variable('HS_TOKEN')
    service_name = _get_environment_variable('HS_SERVICE_NAME')

    if api_token is None or service_name is None:
        _LOG.warning('HS_TOKEN and HS_SERVICE_NAME must be provided')
        return

    collector_endpoint = _get_environment_variable('HS_COLLECTOR_ENDPOINT')
    sampling_ratio = _get_environment_variable('HS_SAMPLING_RATIO')
    excluded_urls = _get_environment_variable('HS_EXCLUDED_URLS')
    metadata_only = _get_environment_variable('HS_METADATA_ONLY')

    environment = _get_environment_variable('HS_ENVIRONMENT')
    resource_tags = _get_environment_variable('HS_RESOURCE_TAGS', json.loads)
    debug = _get_environment_variable('HS_DEBUG', lambda value: value in ['True', 'true'])
    max_queue_size = _get_environment_variable('HS_MAX_QUEUE_SIZE', int)
    data_obfuscation_allowlist = _get_environment_variable('HS_DATA_OBFUSCATION_ALLOWLIST', json.loads)
    data_obfuscation_blocklist = _get_environment_variable('HS_DATA_OBFUSCATION_BLOCKLIST', json.loads)
    data_obfuscation_hmac_key = _get_environment_variable('HS_DATA_OBFUSCATION_HMAC_KEY')
    data_obfuscation_http_headers_allowlist = _get_environment_variable('HS_DATA_OBFUSCATION_HTTP_HEADERS_ALLOWLIST',
                                                                        json.loads)
    data_obfuscation_http_headers_blocklist = _get_environment_variable('HS_DATA_OBFUSCATION_HTTP_HEADERS_BLOCKLIST',
                                                                        json.loads)

    if data_obfuscation_hmac_key is None and (
            data_obfuscation_allowlist is not None or
            data_obfuscation_blocklist is not None or
            data_obfuscation_http_headers_allowlist is not None or
            data_obfuscation_http_headers_blocklist is not None
    ):
        _LOG.warning('HS_DATA_OBFUSCATION_HMAC_KEY must be provided. Data obfuscation will not be activated')

    return initialize(
        api_token=api_token,
        service_name=service_name,
        enabled=True,
        collector_endpoint=collector_endpoint,
        sampling_ratio=sampling_ratio,
        environment=environment,
        resource_tags=resource_tags,
        debug=debug,
        max_queue_size=max_queue_size,
        data_obfuscation_allowlist=data_obfuscation_allowlist,
        data_obfuscation_blocklist=data_obfuscation_blocklist,
        data_obfuscation_hmac_key=data_obfuscation_hmac_key,
        data_obfuscation_http_headers_allowlist=data_obfuscation_http_headers_allowlist,
        data_obfuscation_http_headers_blocklist=data_obfuscation_http_headers_blocklist,
        excluded_urls=excluded_urls,
        metadata_only=metadata_only,
        auto_init=True
    )


def create_custom_span(
        name: str,
        attributes: types.Attributes = None,
        wrapped_fn: Optional[Callable[[], any]] = None,
        set_as_current_context: bool = False
):
    if not Helios.has_instance():
        _LOG.debug('Cannot create custom span before initializing Helios')
        if wrapped_fn is not None:
            return wrapped_fn()
        return

    hs = Helios.get_instance()
    return hs.create_custom_span(name, attributes, wrapped_fn, set_as_current_context)


def flush():
    if not Helios.has_instance():
        _LOG.debug('Cannot flush before initializing Helios')

    hs = Helios.get_instance()
    hs.flush()


def validate(spans, validations_callback, expected_number_of_spans=1):
    if len(spans) <= expected_number_of_spans:
        for s in spans:
            validations_callback(s)
    else:
        validated_spans_count = 0
        for s in spans:
            try:
                validations_callback(s)
                validated_spans_count += 1
            except AssertionError:
                continue
        assert validated_spans_count == expected_number_of_spans


def inject_current_context(carrier: textmap.CarrierT, setter: textmap.Setter = None):
    carrier = carrier if carrier is not None else {}
    current_context = get_current()
    if setter is not None:
        inject(carrier, context=current_context, setter=setter)
    else:
        inject(carrier, context=current_context)
    return carrier


def extract_context(carrier: textmap.CarrierT):
    carrier = carrier if carrier else {}
    context = extract(carrier)
    return context


def initialize_test(api_token: Optional[str] = None):
    return HeliosTestTrace(api_token)


def initialize_playwright_test(page, api_token: Optional[str] = None):
    test_trace_manager = HeliosTestTrace(api_token)
    test_trace_manager.instrument_playwright(page)
    return test_trace_manager


def obfuscate_data(key: str, msg: Any, length: Optional[int] = None) -> str:
    return DataObfuscator.hash(key, msg, length)


def _get_environment_variable(key: str, parser: Optional[Callable[[str], Any]] = None) -> Any:
    value = os.environ.get(key)

    if value is None:
        return None

    if parser is None:
        return value
    else:
        try:
            return parser(value)
        except Exception as exception:
            _LOG.error(f'Cannot parse {key}, value is {value}.', exception)
            return None


def _get_data_obfuscator_configuration(
        allowlist: Rules = None,
        blocklist: Rules = None,
        hmac_key: Optional[str] = None,
        http_headers_allowlist: Optional[List[str]] = None,
        http_headers_blocklist: Optional[List[str]] = None
) -> Optional[DataObfuscatorConfiguration]:
    if hmac_key is None:
        return None

    if allowlist is not None and blocklist is not None:
        _LOG.error('Data obfuscation cannot be configured with both an allowlist and a blocklist.')
        return None

    if http_headers_allowlist is not None and http_headers_blocklist is not None:
        _LOG.error('HTTP headers obfuscation cannot be configured with both an allowlist and a blocklist.')
        return None

    return DataObfuscatorConfiguration(
        hmac_key=hmac_key,
        http_headers_mode='allowlist' if http_headers_allowlist is not None
                          else 'blocklist' if http_headers_blocklist is not None else None,
        http_headers_rules=http_headers_allowlist if http_headers_allowlist is not None
                          else http_headers_blocklist if http_headers_blocklist is not None else None,
        mode='allowlist' if allowlist is not None else 'blocklist' if blocklist is not None else None,
        rules=allowlist if allowlist is not None else blocklist if blocklist is not None else None)


__all__ = [
    'initialize',
    'initialize_test',
    'extract_context',
    'inject_current_context',
    'validate',
    'create_custom_span',
    'flush',
    'auto_initialize',
    'SuppressTracing',
    'RabbitMqMessageContext',
    'SqsMessageContext',
    'obfuscate_data',
]
