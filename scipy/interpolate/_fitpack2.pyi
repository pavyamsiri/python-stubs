from _typeshed import Incomplete

__all__ = [
    "UnivariateSpline",
    "InterpolatedUnivariateSpline",
    "LSQUnivariateSpline",
    "BivariateSpline",
    "LSQBivariateSpline",
    "SmoothBivariateSpline",
    "LSQSphereBivariateSpline",
    "SmoothSphereBivariateSpline",
    "RectBivariateSpline",
    "RectSphereBivariateSpline",
]

class UnivariateSpline:
    def __init__(
        self,
        x,
        y,
        w: Incomplete | None = None,
        bbox=...,
        k: int = 3,
        s: Incomplete | None = None,
        ext: int = 0,
        check_finite: bool = False,
    ) -> None: ...
    @staticmethod
    def validate_input(x, y, w, bbox, k, s, ext, check_finite): ...
    def set_smoothing_factor(self, s) -> None: ...
    def __call__(self, x, nu: int = 0, ext: Incomplete | None = None): ...
    def get_knots(self): ...
    def get_coeffs(self): ...
    def get_residual(self): ...
    def integral(self, a, b): ...
    def derivatives(self, x): ...
    def roots(self): ...
    def derivative(self, n: int = 1): ...
    def antiderivative(self, n: int = 1): ...

class InterpolatedUnivariateSpline(UnivariateSpline):
    def __init__(
        self,
        x,
        y,
        w: Incomplete | None = None,
        bbox=...,
        k: int = 3,
        ext: int = 0,
        check_finite: bool = False,
    ) -> None: ...

class LSQUnivariateSpline(UnivariateSpline):
    def __init__(
        self,
        x,
        y,
        t,
        w: Incomplete | None = None,
        bbox=...,
        k: int = 3,
        ext: int = 0,
        check_finite: bool = False,
    ) -> None: ...

class _BivariateSplineBase:
    def get_residual(self): ...
    def get_knots(self): ...
    def get_coeffs(self): ...
    def __call__(self, x, y, dx: int = 0, dy: int = 0, grid: bool = True): ...
    def partial_derivative(self, dx, dy): ...

class BivariateSpline(_BivariateSplineBase):
    def ev(self, xi, yi, dx: int = 0, dy: int = 0): ...
    def integral(self, xa, xb, ya, yb): ...

class _DerivedBivariateSpline(_BivariateSplineBase):
    @property
    def fp(self) -> None: ...
    def get_residual(self) -> None: ...

class SmoothBivariateSpline(BivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    def __init__(
        self,
        x,
        y,
        z,
        w: Incomplete | None = None,
        bbox=...,
        kx: int = 3,
        ky: int = 3,
        s: Incomplete | None = None,
        eps: float = 1e-16,
    ) -> None: ...

class LSQBivariateSpline(BivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    def __init__(
        self,
        x,
        y,
        z,
        tx,
        ty,
        w: Incomplete | None = None,
        bbox=...,
        kx: int = 3,
        ky: int = 3,
        eps: Incomplete | None = None,
    ) -> None: ...

class RectBivariateSpline(BivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    def __init__(
        self, x, y, z, bbox=..., kx: int = 3, ky: int = 3, s: int = 0
    ) -> None: ...

class SphereBivariateSpline(_BivariateSplineBase):
    def __call__(
        self, theta, phi, dtheta: int = 0, dphi: int = 0, grid: bool = True
    ): ...
    def ev(self, theta, phi, dtheta: int = 0, dphi: int = 0): ...

class SmoothSphereBivariateSpline(SphereBivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    def __init__(
        self,
        theta,
        phi,
        r,
        w: Incomplete | None = None,
        s: float = 0.0,
        eps: float = 1e-16,
    ) -> None: ...
    def __call__(
        self, theta, phi, dtheta: int = 0, dphi: int = 0, grid: bool = True
    ): ...

class LSQSphereBivariateSpline(SphereBivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    def __init__(
        self, theta, phi, r, tt, tp, w: Incomplete | None = None, eps: float = 1e-16
    ) -> None: ...
    def __call__(
        self, theta, phi, dtheta: int = 0, dphi: int = 0, grid: bool = True
    ): ...

class RectSphereBivariateSpline(SphereBivariateSpline):
    fp: Incomplete
    tck: Incomplete
    degrees: Incomplete
    v0: Incomplete
    def __init__(
        self,
        u,
        v,
        r,
        s: float = 0.0,
        pole_continuity: bool = False,
        pole_values: Incomplete | None = None,
        pole_exact: bool = False,
        pole_flat: bool = False,
    ) -> None: ...
    def __call__(
        self, theta, phi, dtheta: int = 0, dphi: int = 0, grid: bool = True
    ): ...
