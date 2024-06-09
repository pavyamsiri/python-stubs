from _typeshed import Incomplete

__all__ = ["_minimize_trust_krylov"]

def _minimize_trust_krylov(
    fun,
    x0,
    args=(),
    jac: Incomplete | None = None,
    hess: Incomplete | None = None,
    hessp: Incomplete | None = None,
    inexact: bool = True,
    **trust_region_options,
): ...
