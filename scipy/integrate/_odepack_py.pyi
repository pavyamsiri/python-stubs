from _typeshed import Incomplete

__all__ = ["odeint", "ODEintWarning"]

class ODEintWarning(Warning): ...

def odeint(
    func,
    y0,
    t,
    args=(),
    Dfun: Incomplete | None = None,
    col_deriv: int = 0,
    full_output: int = 0,
    ml: Incomplete | None = None,
    mu: Incomplete | None = None,
    rtol: Incomplete | None = None,
    atol: Incomplete | None = None,
    tcrit: Incomplete | None = None,
    h0: float = 0.0,
    hmax: float = 0.0,
    hmin: float = 0.0,
    ixpr: int = 0,
    mxstep: int = 0,
    mxhnil: int = 0,
    mxordn: int = 12,
    mxords: int = 5,
    printmessg: int = 0,
    tfirst: bool = False,
): ...
