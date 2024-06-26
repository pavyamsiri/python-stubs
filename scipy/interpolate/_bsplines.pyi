from _typeshed import Incomplete

__all__ = ["BSpline", "make_interp_spline", "make_lsq_spline", "make_smoothing_spline"]

class BSpline:
    k: Incomplete
    c: Incomplete
    t: Incomplete
    extrapolate: Incomplete
    axis: Incomplete
    def __init__(self, t, c, k, extrapolate: bool = True, axis: int = 0) -> None: ...
    @classmethod
    def construct_fast(cls, t, c, k, extrapolate: bool = True, axis: int = 0): ...
    @property
    def tck(self): ...
    @classmethod
    def basis_element(cls, t, extrapolate: bool = True): ...
    @classmethod
    def design_matrix(cls, x, t, k, extrapolate: bool = False): ...
    def __call__(self, x, nu: int = 0, extrapolate: Incomplete | None = None): ...
    def derivative(self, nu: int = 1): ...
    def antiderivative(self, nu: int = 1): ...
    def integrate(self, a, b, extrapolate: Incomplete | None = None): ...
    @classmethod
    def from_power_basis(cls, pp, bc_type: str = "not-a-knot"): ...
    def insert_knot(self, x, m: int = 1): ...

def make_interp_spline(
    x,
    y,
    k: int = 3,
    t: Incomplete | None = None,
    bc_type: Incomplete | None = None,
    axis: int = 0,
    check_finite: bool = True,
): ...
def make_lsq_spline(
    x,
    y,
    t,
    k: int = 3,
    w: Incomplete | None = None,
    axis: int = 0,
    check_finite: bool = True,
): ...
def make_smoothing_spline(
    x, y, w: Incomplete | None = None, lam: Incomplete | None = None
): ...
