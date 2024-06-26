from _typeshed import Incomplete

PyCFuncPtr: Incomplete
ffi: Incomplete

class CData: ...

class LowLevelCallable(tuple):
    def __new__(
        cls,
        function,
        user_data: Incomplete | None = None,
        signature: Incomplete | None = None,
    ): ...
    @property
    def function(self): ...
    @property
    def user_data(self): ...
    @property
    def signature(self): ...
    def __getitem__(self, idx) -> None: ...
    @classmethod
    def from_cython(
        cls,
        module,
        name,
        user_data: Incomplete | None = None,
        signature: Incomplete | None = None,
    ): ...
