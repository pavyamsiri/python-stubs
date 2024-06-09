from typing import Literal

ByteOrder = Literal["<", ">"]
SupportedByteOrderCode = Literal[
    "little", "big", "l", "b", "le", "be", "<", ">", "native", "=", "swapped", "s"
]

sys_is_le: bool
native_code: ByteOrder
swapped_code: ByteOrder
aliases: dict[str, tuple[str, ...]]

def to_numpy_code(code: SupportedByteOrderCode) -> ByteOrder: ...

__all__ = ["aliases", "native_code", "swapped_code", "sys_is_le", "to_numpy_code"]
