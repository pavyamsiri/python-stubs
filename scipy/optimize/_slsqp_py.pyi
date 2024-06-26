from _typeshed import Incomplete

__all__ = ["approx_jacobian", "fmin_slsqp"]

def approx_jacobian(x, func, epsilon, *args): ...
def fmin_slsqp(
    func,
    x0,
    eqcons=(),
    f_eqcons: Incomplete | None = None,
    ieqcons=(),
    f_ieqcons: Incomplete | None = None,
    bounds=(),
    fprime: Incomplete | None = None,
    fprime_eqcons: Incomplete | None = None,
    fprime_ieqcons: Incomplete | None = None,
    args=(),
    iter: int = 100,
    acc: float = 1e-06,
    iprint: int = 1,
    disp: Incomplete | None = None,
    full_output: int = 0,
    epsilon=...,
    callback: Incomplete | None = None,
): ...
