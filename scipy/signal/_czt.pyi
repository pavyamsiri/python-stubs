from _typeshed import Incomplete

__all__ = ["czt", "zoom_fft", "CZT", "ZoomFFT", "czt_points"]

def czt_points(m, w: Incomplete | None = None, a: complex = ...): ...

class CZT:
    def __init__(
        self,
        n,
        m: Incomplete | None = None,
        w: Incomplete | None = None,
        a: complex = ...,
    ) -> None: ...
    def __call__(self, x, *, axis: int = -1): ...
    def points(self): ...

class ZoomFFT(CZT):
    w: Incomplete
    a: Incomplete
    def __init__(
        self, n, fn, m: Incomplete | None = None, *, fs: int = 2, endpoint: bool = False
    ) -> None: ...

def czt(
    x,
    m: Incomplete | None = None,
    w: Incomplete | None = None,
    a: complex = ...,
    *,
    axis: int = -1,
): ...
def zoom_fft(
    x,
    fn,
    m: Incomplete | None = None,
    *,
    fs: int = 2,
    endpoint: bool = False,
    axis: int = -1,
): ...
