import logging
from typing import MutableMapping, Any

from cf_extension_core.interface import (  # noqa: F401
    create_resource,
    update_resource,
    delete_resource,
    read_resource,
    list_resource,
    CustomResourceHelpers,
    generate_dynamo_resource,
)


def initialize_handler(
    callback_context: MutableMapping[str, Any],
    total_allowed_time_in_minutes: int,
) -> None:
    # TODO: Consider overriding the Table name based on Type Name here
    _default_package_logging_config()

    CustomResourceHelpers._callback_add_resource_end_time(
        callback_context=callback_context,
        total_allowed_time_in_minutes=total_allowed_time_in_minutes,
    )
    CustomResourceHelpers._callback_add_handler_entry_time(callback_context=callback_context)
    CustomResourceHelpers._return_failure_due_to_timeout(callback_context)


def _default_package_logging_config() -> None:
    """
    Helps setup default logging config for custom resources
    :return:
    """
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    logging.getLogger(__name__).setLevel(logging.DEBUG)


# Package Logger
# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger(__name__).addHandler(logging.NullHandler())
