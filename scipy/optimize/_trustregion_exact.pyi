from ._trustregion import BaseQuadraticSubproblem
from _typeshed import Incomplete

__all__ = [
    "_minimize_trustregion_exact",
    "estimate_smallest_singular_value",
    "singular_leading_submatrix",
    "IterativeSubproblem",
]

def _minimize_trustregion_exact(
    fun,
    x0,
    args=(),
    jac: Incomplete | None = None,
    hess: Incomplete | None = None,
    **trust_region_options,
): ...
def estimate_smallest_singular_value(U): ...
def singular_leading_submatrix(A, U, k): ...

class IterativeSubproblem(BaseQuadraticSubproblem):
    UPDATE_COEFF: float
    EPS: Incomplete
    previous_tr_radius: int
    lambda_lb: Incomplete
    niter: int
    k_easy: Incomplete
    k_hard: Incomplete
    dimension: Incomplete
    hess_inf: Incomplete
    hess_fro: Incomplete
    CLOSE_TO_ZERO: Incomplete
    def __init__(
        self,
        x,
        fun,
        jac,
        hess,
        hessp: Incomplete | None = None,
        k_easy: float = 0.1,
        k_hard: float = 0.2,
    ) -> None: ...
    lambda_current: Incomplete
    def solve(self, tr_radius): ...
