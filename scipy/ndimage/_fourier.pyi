from _typeshed import Incomplete

__all__ = ["fourier_gaussian", "fourier_uniform", "fourier_ellipsoid", "fourier_shift"]

def fourier_gaussian(
    input, sigma, n: int = -1, axis: int = -1, output: Incomplete | None = None
): ...
def fourier_uniform(
    input, size, n: int = -1, axis: int = -1, output: Incomplete | None = None
): ...
def fourier_ellipsoid(
    input, size, n: int = -1, axis: int = -1, output: Incomplete | None = None
): ...
def fourier_shift(
    input, shift, n: int = -1, axis: int = -1, output: Incomplete | None = None
): ...
