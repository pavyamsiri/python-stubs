from _typeshed import Incomplete

class DCSRCH:
    stage: Incomplete
    ginit: Incomplete
    gtest: Incomplete
    gx: Incomplete
    gy: Incomplete
    finit: Incomplete
    fx: Incomplete
    fy: Incomplete
    stx: Incomplete
    sty: Incomplete
    stmin: Incomplete
    stmax: Incomplete
    width: Incomplete
    width1: Incomplete
    ftol: Incomplete
    gtol: Incomplete
    xtol: Incomplete
    stpmin: Incomplete
    stpmax: Incomplete
    phi: Incomplete
    derphi: Incomplete
    def __init__(self, phi, derphi, ftol, gtol, xtol, stpmin, stpmax) -> None: ...
    def __call__(self, alpha1, phi0: Incomplete | None = None, derphi0: Incomplete | None = None, maxiter: int = 100): ...

def dcstep(stx, fx, dx, sty, fy, dy, stp, fp, dp, brackt, stpmin, stpmax): ...
