from _typeshed import Incomplete

__all__ = ["fsolve", "leastsq", "fixed_point", "curve_fit"]

def fsolve(
    func,
    x0,
    args=(),
    fprime: Incomplete | None = None,
    full_output: int = 0,
    col_deriv: int = 0,
    xtol: float = 1.49012e-08,
    maxfev: int = 0,
    band: Incomplete | None = None,
    epsfcn: Incomplete | None = None,
    factor: int = 100,
    diag: Incomplete | None = None,
): ...
def leastsq(
    func,
    x0,
    args=(),
    Dfun: Incomplete | None = None,
    full_output: bool = False,
    col_deriv: bool = False,
    ftol: float = 1.49012e-08,
    xtol: float = 1.49012e-08,
    gtol: float = 0.0,
    maxfev: int = 0,
    epsfcn: Incomplete | None = None,
    factor: int = 100,
    diag: Incomplete | None = None,
): ...
def curve_fit(
    f,
    xdata,
    ydata,
    p0: Incomplete | None = None,
    sigma: Incomplete | None = None,
    absolute_sigma: bool = False,
    check_finite: Incomplete | None = None,
    bounds=...,
    method: Incomplete | None = None,
    jac: Incomplete | None = None,
    *,
    full_output: bool = False,
    nan_policy: Incomplete | None = None,
    **kwargs,
): ...
def fixed_point(
    func, x0, args=(), xtol: float = 1e-08, maxiter: int = 500, method: str = "del2"
): ...
