from _typeshed import Incomplete

__all__ = ["readsav"]

class Pointer:
    index: Incomplete
    def __init__(self, index) -> None: ...

class ObjectPointer(Pointer): ...

class AttrDict(dict):
    def __init__(self, init={}) -> None: ...
    def __getitem__(self, name): ...
    def __setitem__(self, key, value) -> None: ...
    def __getattr__(self, name): ...
    __setattr__ = __setitem__
    __call__ = __getitem__

def readsav(
    file_name,
    idict: Incomplete | None = None,
    python_dict: bool = False,
    uncompressed_file_name: Incomplete | None = None,
    verbose: bool = False,
): ...
