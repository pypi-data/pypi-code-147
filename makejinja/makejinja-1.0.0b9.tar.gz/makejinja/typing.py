import typing as t
from abc import ABC

from jinja2 import Environment
from jinja2.ext import Extension

ExtensionType = t.Union[t.Type[Extension], str]
Extensions = t.Sequence[ExtensionType]
Filter = t.Callable[[t.Any], t.Any]
Filters = t.Sequence[Filter]
Global = t.Callable[..., t.Any]
Globals = t.Sequence[Global]
Test = t.Callable[..., t.Any]
Tests = t.Sequence[Test]
Policies = t.Mapping[str, t.Any]
MutableData = t.MutableMapping[str, t.Any]
Data = t.Mapping[str, t.Any]


class AbstractLoader(ABC):
    def __init__(self, env: Environment, data: MutableData) -> None:
        pass

    def filters(self) -> Filters:
        return []

    def globals(self) -> Globals:
        return []

    def tests(self) -> Tests:
        return []

    def policies(self) -> Policies:
        return {}

    def data(self) -> Data:
        return {}

    def extensions(self) -> Extensions:
        return []
