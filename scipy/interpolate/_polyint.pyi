from _typeshed import Incomplete

__all__ = [
    "KroghInterpolator",
    "krogh_interpolate",
    "BarycentricInterpolator",
    "barycentric_interpolate",
    "approximate_taylor_polynomial",
]

class _Interpolator1D:
    dtype: Incomplete
    def __init__(
        self,
        xi: Incomplete | None = None,
        yi: Incomplete | None = None,
        axis: Incomplete | None = None,
    ) -> None: ...
    def __call__(self, x): ...

class _Interpolator1DWithDerivatives(_Interpolator1D):
    def derivatives(self, x, der: Incomplete | None = None): ...
    def derivative(self, x, der: int = 1): ...

class KroghInterpolator(_Interpolator1DWithDerivatives):
    xi: Incomplete
    yi: Incomplete
    c: Incomplete
    def __init__(self, xi, yi, axis: int = 0) -> None: ...

def krogh_interpolate(xi, yi, x, der: int = 0, axis: int = 0): ...
def approximate_taylor_polynomial(
    f, x, degree, scale, order: Incomplete | None = None
): ...

class BarycentricInterpolator(_Interpolator1DWithDerivatives):
    xi: Incomplete
    n: Incomplete
    wi: Incomplete
    def __init__(
        self,
        xi,
        yi: Incomplete | None = None,
        axis: int = 0,
        *,
        wi: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ) -> None: ...
    yi: Incomplete
    def set_yi(self, yi, axis: Incomplete | None = None) -> None: ...
    def add_xi(self, xi, yi: Incomplete | None = None) -> None: ...
    def __call__(self, x): ...
    def derivative(self, x, der: int = 1): ...

def barycentric_interpolate(xi, yi, x, axis: int = 0, *, der: int = 0): ...
