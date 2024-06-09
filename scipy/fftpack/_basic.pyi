from _typeshed import Incomplete

__all__ = ["fft", "ifft", "fftn", "ifftn", "rfft", "irfft", "fft2", "ifft2"]

def fft(x, n: Incomplete | None = None, axis: int = -1, overwrite_x: bool = False): ...
def ifft(x, n: Incomplete | None = None, axis: int = -1, overwrite_x: bool = False): ...
def rfft(x, n: Incomplete | None = None, axis: int = -1, overwrite_x: bool = False): ...
def irfft(
    x, n: Incomplete | None = None, axis: int = -1, overwrite_x: bool = False
): ...
def fftn(
    x,
    shape: Incomplete | None = None,
    axes: Incomplete | None = None,
    overwrite_x: bool = False,
): ...
def ifftn(
    x,
    shape: Incomplete | None = None,
    axes: Incomplete | None = None,
    overwrite_x: bool = False,
): ...
def fft2(
    x, shape: Incomplete | None = None, axes=(-2, -1), overwrite_x: bool = False
): ...
def ifft2(
    x, shape: Incomplete | None = None, axes=(-2, -1), overwrite_x: bool = False
): ...
