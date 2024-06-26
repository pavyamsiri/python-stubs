from _typeshed import Incomplete

__all__ = ["ReentrancyError", "ReentrancyLock", "non_reentrant"]

class ReentrancyError(RuntimeError): ...

class ReentrancyLock:
    def __init__(self, err_msg) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def decorate(self, func): ...

def non_reentrant(err_msg: Incomplete | None = None): ...
