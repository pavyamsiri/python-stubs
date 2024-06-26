from ._polyint import _Interpolator1D
from _typeshed import Incomplete

__all__ = ["interp1d", "interp2d", "lagrange", "PPoly", "BPoly", "NdPPoly"]

def lagrange(x, w): ...

class interp2d:
    tck: Incomplete
    bounds_error: Incomplete
    fill_value: Incomplete
    def __init__(
        self,
        x,
        y,
        z,
        kind: str = "linear",
        copy: bool = True,
        bounds_error: bool = False,
        fill_value: Incomplete | None = None,
    ) -> None: ...
    def __call__(self, x, y, dx: int = 0, dy: int = 0, assume_sorted: bool = False): ...

class interp1d(_Interpolator1D):
    bounds_error: Incomplete
    copy: Incomplete
    axis: Incomplete
    y: Incomplete
    x: Incomplete
    x_bds: Incomplete
    def __init__(
        self,
        x,
        y,
        kind: str = "linear",
        axis: int = -1,
        copy: bool = True,
        bounds_error: Incomplete | None = None,
        fill_value=...,
        assume_sorted: bool = False,
    ) -> None: ...
    @property
    def fill_value(self): ...
    @fill_value.setter
    def fill_value(self, fill_value) -> None: ...

class _PPolyBase:
    c: Incomplete
    x: Incomplete
    extrapolate: Incomplete
    axis: Incomplete
    def __init__(
        self, c, x, extrapolate: Incomplete | None = None, axis: int = 0
    ) -> None: ...
    @classmethod
    def construct_fast(
        cls, c, x, extrapolate: Incomplete | None = None, axis: int = 0
    ): ...
    def extend(self, c, x) -> None: ...
    def __call__(self, x, nu: int = 0, extrapolate: Incomplete | None = None): ...

class PPoly(_PPolyBase):
    def derivative(self, nu: int = 1): ...
    def antiderivative(self, nu: int = 1): ...
    def integrate(self, a, b, extrapolate: Incomplete | None = None): ...
    def solve(
        self,
        y: float = 0.0,
        discontinuity: bool = True,
        extrapolate: Incomplete | None = None,
    ): ...
    def roots(
        self, discontinuity: bool = True, extrapolate: Incomplete | None = None
    ): ...
    @classmethod
    def from_spline(cls, tck, extrapolate: Incomplete | None = None): ...
    @classmethod
    def from_bernstein_basis(cls, bp, extrapolate: Incomplete | None = None): ...

class BPoly(_PPolyBase):
    def derivative(self, nu: int = 1): ...
    def antiderivative(self, nu: int = 1): ...
    def integrate(self, a, b, extrapolate: Incomplete | None = None): ...
    c: Incomplete
    def extend(self, c, x): ...
    @classmethod
    def from_power_basis(cls, pp, extrapolate: Incomplete | None = None): ...
    @classmethod
    def from_derivatives(
        cls,
        xi,
        yi,
        orders: Incomplete | None = None,
        extrapolate: Incomplete | None = None,
    ): ...

class NdPPoly:
    x: Incomplete
    c: Incomplete
    extrapolate: Incomplete
    def __init__(self, c, x, extrapolate: Incomplete | None = None) -> None: ...
    @classmethod
    def construct_fast(cls, c, x, extrapolate: Incomplete | None = None): ...
    def __call__(
        self, x, nu: Incomplete | None = None, extrapolate: Incomplete | None = None
    ): ...
    def derivative(self, nu): ...
    def antiderivative(self, nu): ...
    def integrate_1d(self, a, b, axis, extrapolate: Incomplete | None = None): ...
    def integrate(self, ranges, extrapolate: Incomplete | None = None): ...
