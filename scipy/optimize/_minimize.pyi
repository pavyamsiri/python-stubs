from _typeshed import Incomplete

__all__ = ["minimize", "minimize_scalar"]

def minimize(
    fun,
    x0,
    args=(),
    method: Incomplete | None = None,
    jac: Incomplete | None = None,
    hess: Incomplete | None = None,
    hessp: Incomplete | None = None,
    bounds: Incomplete | None = None,
    constraints=(),
    tol: Incomplete | None = None,
    callback: Incomplete | None = None,
    options: Incomplete | None = None,
): ...
def minimize_scalar(
    fun,
    bracket: Incomplete | None = None,
    bounds: Incomplete | None = None,
    args=(),
    method: Incomplete | None = None,
    tol: Incomplete | None = None,
    options: Incomplete | None = None,
): ...
