from _typeshed import Incomplete
from typing import Any, NamedTuple, Protocol

__all__ = [
    "fixed_quad",
    "quadrature",
    "romberg",
    "romb",
    "trapezoid",
    "trapz",
    "simps",
    "simpson",
    "cumulative_trapezoid",
    "cumtrapz",
    "newton_cotes",
    "qmc_quad",
    "AccuracyWarning",
    "cumulative_simpson",
]

def trapezoid(y, x: Incomplete | None = None, dx: float = 1.0, axis: int = -1): ...
def trapz(y, x: Incomplete | None = None, dx: float = 1.0, axis: int = -1): ...

class AccuracyWarning(Warning): ...

class CacheAttributes(Protocol):
    cache: dict[int, tuple[Any, Any]]

def fixed_quad(func, a, b, args=(), n: int = 5): ...
def quadrature(
    func,
    a,
    b,
    args=(),
    tol: float = 1.49e-08,
    rtol: float = 1.49e-08,
    maxiter: int = 50,
    vec_func: bool = True,
    miniter: int = 1,
): ...
def cumtrapz(
    y,
    x: Incomplete | None = None,
    dx: float = 1.0,
    axis: int = -1,
    initial: Incomplete | None = None,
): ...
def cumulative_trapezoid(
    y,
    x: Incomplete | None = None,
    dx: float = 1.0,
    axis: int = -1,
    initial: Incomplete | None = None,
): ...
def simps(
    y, x: Incomplete | None = None, dx: float = 1.0, axis: int = -1, even=...
): ...
def simpson(
    y, *, x: Incomplete | None = None, dx: float = 1.0, axis: int = -1, even=...
): ...
def cumulative_simpson(
    y,
    *,
    x: Incomplete | None = None,
    dx: float = 1.0,
    axis: int = -1,
    initial: Incomplete | None = None,
): ...
def romb(y, dx: float = 1.0, axis: int = -1, show: bool = False): ...
def romberg(
    function,
    a,
    b,
    args=(),
    tol: float = 1.48e-08,
    rtol: float = 1.48e-08,
    show: bool = False,
    divmax: int = 10,
    vec_func: bool = False,
): ...
def newton_cotes(rn, equal: int = 0): ...

class QMCQuadResult(NamedTuple):
    integral: Incomplete
    standard_error: Incomplete

def qmc_quad(
    func,
    a,
    b,
    *,
    n_estimates: int = 8,
    n_points: int = 1024,
    qrng: Incomplete | None = None,
    log: bool = False,
): ...
