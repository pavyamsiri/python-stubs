from typing import Any

from numpy import int32

class Pointer:
    index: int32
    def __init__(self, index: int32) -> None: ...

class ObjectPointer(Pointer): ...

class AttrDict(dict[str, Any]):
    def __init__(self, init: dict[str, Any] = ...) -> None: ...
    def __getitem__(self, name: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    __setattr__ = __setitem__
    __call__ = __getitem__

def readsav(
    file_name: str,
    idict: dict[str, Any] | None = ...,
    python_dict: bool = ...,
    uncompressed_file_name: str | None = ...,
    verbose: bool = ...,
) -> dict[str, Any] | AttrDict: ...

__all__ = ["readsav"]
