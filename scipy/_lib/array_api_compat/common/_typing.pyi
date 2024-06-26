from typing import Any, Protocol

__all__ = ["NestedSequence", "SupportsBufferProtocol"]

class NestedSequence(Protocol[_T_co]):
    def __getitem__(self, key: int) -> _T_co | NestedSequence[_T_co]: ...
    def __len__(self) -> int: ...

SupportsBufferProtocol = Any
