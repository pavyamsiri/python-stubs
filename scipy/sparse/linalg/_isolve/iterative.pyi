from _typeshed import Incomplete

__all__ = ["bicg", "bicgstab", "cg", "cgs", "gmres", "qmr"]

def bicg(
    A,
    b,
    x0: Incomplete | None = None,
    *,
    tol=...,
    maxiter: Incomplete | None = None,
    M: Incomplete | None = None,
    callback: Incomplete | None = None,
    atol: float = 0.0,
    rtol: float = 1e-05,
): ...
def bicgstab(
    A,
    b,
    *,
    x0: Incomplete | None = None,
    tol=...,
    maxiter: Incomplete | None = None,
    M: Incomplete | None = None,
    callback: Incomplete | None = None,
    atol: float = 0.0,
    rtol: float = 1e-05,
): ...
def cg(
    A,
    b,
    x0: Incomplete | None = None,
    *,
    tol=...,
    maxiter: Incomplete | None = None,
    M: Incomplete | None = None,
    callback: Incomplete | None = None,
    atol: float = 0.0,
    rtol: float = 1e-05,
): ...
def cgs(
    A,
    b,
    x0: Incomplete | None = None,
    *,
    tol=...,
    maxiter: Incomplete | None = None,
    M: Incomplete | None = None,
    callback: Incomplete | None = None,
    atol: float = 0.0,
    rtol: float = 1e-05,
): ...
def gmres(
    A,
    b,
    x0: Incomplete | None = None,
    *,
    tol=...,
    restart: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    M: Incomplete | None = None,
    callback: Incomplete | None = None,
    restrt=...,
    atol: float = 0.0,
    callback_type: Incomplete | None = None,
    rtol: float = 1e-05,
): ...
def qmr(
    A,
    b,
    x0: Incomplete | None = None,
    *,
    tol=...,
    maxiter: Incomplete | None = None,
    M1: Incomplete | None = None,
    M2: Incomplete | None = None,
    callback: Incomplete | None = None,
    atol: float = 0.0,
    rtol: float = 1e-05,
): ...
