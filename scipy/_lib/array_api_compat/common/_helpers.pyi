from _typeshed import Incomplete
from typing import Any

__all__ = [
    "is_array_api_obj",
    "array_namespace",
    "get_namespace",
    "device",
    "to_device",
    "size",
]

def is_array_api_obj(x): ...
def array_namespace(
    *xs, api_version: Incomplete | None = None, _use_compat: bool = True
): ...

get_namespace = array_namespace

def device(x: Array, /) -> Device: ...
def to_device(
    x: Array, device: Device, /, *, stream: Optional[Union[int, Any]] = None
) -> Array: ...
def size(x): ...
