from ._upfirdn_apply import _output_len as _output_len

__all__ = ["upfirdn", "_output_len"]

class _UpFIRDn:
    def __init__(self, h, x_dtype, up, down) -> None: ...
    def apply_filter(
        self, x, axis: int = -1, mode: str = "constant", cval: int = 0
    ): ...

def upfirdn(
    h,
    x,
    up: int = 1,
    down: int = 1,
    axis: int = -1,
    mode: str = "constant",
    cval: int = 0,
): ...
