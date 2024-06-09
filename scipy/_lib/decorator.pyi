import re
from collections.abc import Callable, Iterable
from contextlib import _GeneratorContextManager  # type: ignore[private]
from typing import Any, NamedTuple
from inspect import FullArgSpec

from _typeshed import Incomplete

__version__: str

def get_init(cls: type[Any]) -> Callable[..., None]: ...

class ArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete

def getargspec(f: object) -> ArgSpec: ...

DEF: re.Pattern[str]

class FunctionMaker:
    name: str
    shortsignature: str | None
    doc: str | None
    module: str
    annotations: dict[str, type | str]
    signature: str
    dict: dict[str, Any]
    args: Iterable[str]
    defaults: Iterable[Any] | None
    varargs: str | None
    varkw: str | None
    kwonlyargs: Iterable[str] | None
    kwonlydefaults: dict[str, Any] | None

    def __init__(
        self,
        func: Callable[..., Any] | None = ...,
        name: str | None = ...,
        signature: str | None = ...,
        defaults: Iterable[Any] | None = ...,
        doc: str | None = ...,
        module: str | None = ...,
        funcdict: dict[str, Any] | None = ...,
    ) -> None: ...
    def update(self, func: Callable[..., Any], **kw: dict[str, Any]) -> None: ...
    def make(
        self,
        src_templ: str,
        evaldict: dict[str, Any] | None = ...,
        addsource: bool = ...,
        **attrs: dict[str, Any],
    ) -> Callable[..., Any]: ...
    @classmethod
    def create(
        cls,
        obj: Callable[..., Any] | str,
        body: str,
        evaldict: dict[str, Any],
        defaults: Iterable[Any] | None = ...,
        doc: str | None = ...,
        module: str | None = ...,
        addsource: bool = ...,
        **attrs: dict[str, Any],
    ) -> Callable[..., Any]: ...

def decorate(func: Callable[..., Any], caller: Any) -> Callable[..., Any]: ...
def decorator(
    caller: Any, _func: Callable[..., Any] | None = ...
) -> Callable[..., Any]: ...

class ContextManager(_GeneratorContextManager):  # type: ignore
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]: ...

init: FullArgSpec
n_args: int

def __init__(
    self: Any, g: Callable[..., Any], *a: Iterable[Any], **k: dict[str, Any]
) -> None: ...

contextmanager: Callable[..., Any]

def append(a: type, vancestors: list[type]) -> None: ...
def dispatch_on(*dispatch_args: Iterable[Any]) -> Callable[..., Any]: ...
