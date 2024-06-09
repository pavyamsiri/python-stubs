from _typeshed import Incomplete
from numpy import (
    dtype,
    float32,
    float64,
    int16,
    int32,
    int64,
    int8,
    ndarray as ndarray,
    uint16,
    uint32,
    uint64,
    uint8,
)

__all__ = ["ndarray", "Device", "Dtype"]

Device: Incomplete
Dtype = dtype[
    int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | float32 | float64
]
