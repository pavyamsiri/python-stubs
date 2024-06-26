import typing
from ._uarray import (
    BackendNotImplementedError as BackendNotImplementedError,
    _BackendState as _BackendState,
    _Function as _Function,
    _SetBackendContext as _SetBackendContext,
    _SkipBackendContext as _SkipBackendContext,
)
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = [
    "set_backend",
    "set_global_backend",
    "skip_backend",
    "register_backend",
    "determine_backend",
    "determine_backend_multi",
    "clear_backends",
    "create_multimethod",
    "generate_multimethod",
    "_Function",
    "BackendNotImplementedError",
    "Dispatchable",
    "wrap_single_convertor",
    "wrap_single_convertor_instance",
    "all_of_type",
    "mark_as",
    "set_state",
    "get_state",
    "reset_state",
    "_BackendState",
    "_SkipBackendContext",
    "_SetBackendContext",
]

ArgumentReplacerType = typing.Callable[[tuple, dict, tuple], tuple[tuple, dict]]

def get_state(): ...
def reset_state() -> Generator[None, None, None]: ...
def set_state(state) -> Generator[None, None, None]: ...
def create_multimethod(*args, **kwargs): ...
def generate_multimethod(
    argument_extractor: ArgumentExtractorType,
    argument_replacer: ArgumentReplacerType,
    domain: str,
    default: typing.Callable | None = None,
): ...
def set_backend(backend, coerce: bool = False, only: bool = False): ...
def skip_backend(backend): ...
def set_global_backend(
    backend, coerce: bool = False, only: bool = False, *, try_last: bool = False
) -> None: ...
def register_backend(backend) -> None: ...
def clear_backends(domain, registered: bool = True, globals: bool = False) -> None: ...

class Dispatchable:
    value: Incomplete
    type: Incomplete
    coercible: Incomplete
    def __init__(self, value, dispatch_type, coercible: bool = True) -> None: ...
    def __getitem__(self, index): ...

def mark_as(dispatch_type): ...
def all_of_type(arg_type): ...
def wrap_single_convertor(convert_single): ...
def wrap_single_convertor_instance(convert_single): ...
def determine_backend(
    value, dispatch_type, *, domain, only: bool = True, coerce: bool = False
): ...
def determine_backend_multi(
    dispatchables, *, domain, only: bool = True, coerce: bool = False, **kwargs
): ...
