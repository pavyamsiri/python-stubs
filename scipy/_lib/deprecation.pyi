from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

def _deprecated(msg: str, stacklevel: int = 2) -> Callable[[F], F]: ...

class _DeprecationHelperStr:
    def __init__(self, content: str, message: str) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...

__all__ = ["_deprecated"]
