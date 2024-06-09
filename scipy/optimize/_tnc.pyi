from _typeshed import Incomplete

__all__ = ["fmin_tnc"]

def fmin_tnc(
    func,
    x0,
    fprime: Incomplete | None = None,
    args=(),
    approx_grad: int = 0,
    bounds: Incomplete | None = None,
    epsilon: float = 1e-08,
    scale: Incomplete | None = None,
    offset: Incomplete | None = None,
    messages=...,
    maxCGit: int = -1,
    maxfun: Incomplete | None = None,
    eta: int = -1,
    stepmx: int = 0,
    accuracy: int = 0,
    fmin: int = 0,
    ftol: int = -1,
    xtol: int = -1,
    pgtol: int = -1,
    rescale: int = -1,
    disp: Incomplete | None = None,
    callback: Incomplete | None = None,
): ...
