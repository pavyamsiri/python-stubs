from . import PPoly
from _typeshed import Incomplete
from typing import Literal

__all__ = ['CubicHermiteSpline', 'PchipInterpolator', 'pchip_interpolate', 'Akima1DInterpolator', 'CubicSpline']

class CubicHermiteSpline(PPoly):
    axis: Incomplete
    def __init__(self, x, y, dydx, axis: int = 0, extrapolate: Incomplete | None = None) -> None: ...

class PchipInterpolator(CubicHermiteSpline):
    axis: Incomplete
    def __init__(self, x, y, axis: int = 0, extrapolate: Incomplete | None = None) -> None: ...

def pchip_interpolate(xi, yi, x, der: int = 0, axis: int = 0): ...

class Akima1DInterpolator(CubicHermiteSpline):
    axis: Incomplete
    def __init__(self, x, y, axis: int = 0, *, method: Literal['akima', 'makima'] = 'akima') -> None: ...
    def extend(self, c, x, right: bool = True) -> None: ...
    @classmethod
    def from_spline(cls, tck, extrapolate: Incomplete | None = None) -> None: ...
    @classmethod
    def from_bernstein_basis(cls, bp, extrapolate: Incomplete | None = None) -> None: ...

class CubicSpline(CubicHermiteSpline):
    axis: Incomplete
    def __init__(self, x, y, axis: int = 0, bc_type: str = 'not-a-knot', extrapolate: Incomplete | None = None) -> None: ...
