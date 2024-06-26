from _typeshed import Incomplete

__all__ = [
    "LineSearchWarning",
    "line_search_wolfe1",
    "line_search_wolfe2",
    "scalar_search_wolfe1",
    "scalar_search_wolfe2",
    "line_search_armijo",
]

class LineSearchWarning(RuntimeWarning): ...

def line_search_wolfe1(
    f,
    fprime,
    xk,
    pk,
    gfk: Incomplete | None = None,
    old_fval: Incomplete | None = None,
    old_old_fval: Incomplete | None = None,
    args=(),
    c1: float = 0.0001,
    c2: float = 0.9,
    amax: int = 50,
    amin: float = 1e-08,
    xtol: float = 1e-14,
): ...
def scalar_search_wolfe1(
    phi,
    derphi,
    phi0: Incomplete | None = None,
    old_phi0: Incomplete | None = None,
    derphi0: Incomplete | None = None,
    c1: float = 0.0001,
    c2: float = 0.9,
    amax: int = 50,
    amin: float = 1e-08,
    xtol: float = 1e-14,
): ...

line_search = line_search_wolfe1

def line_search_wolfe2(
    f,
    myfprime,
    xk,
    pk,
    gfk: Incomplete | None = None,
    old_fval: Incomplete | None = None,
    old_old_fval: Incomplete | None = None,
    args=(),
    c1: float = 0.0001,
    c2: float = 0.9,
    amax: Incomplete | None = None,
    extra_condition: Incomplete | None = None,
    maxiter: int = 10,
): ...
def scalar_search_wolfe2(
    phi,
    derphi,
    phi0: Incomplete | None = None,
    old_phi0: Incomplete | None = None,
    derphi0: Incomplete | None = None,
    c1: float = 0.0001,
    c2: float = 0.9,
    amax: Incomplete | None = None,
    extra_condition: Incomplete | None = None,
    maxiter: int = 10,
): ...
def line_search_armijo(
    f, xk, pk, gfk, old_fval, args=(), c1: float = 0.0001, alpha0: int = 1
): ...
