from collections.abc import Callable, Iterable
from typing import Any, Literal

from numpy import int32
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import OptimizeResult
from scipy.optimize._constraints import Bounds
from scipy.sparse._base import _spbase as SparseMatrix
from scipy.sparse.linalg import LinearOperator

class LeastSquaresOptimizeResult(OptimizeResult):
    x: NDArray[Any]
    cost: float
    fun: NDArray[Any]
    jac: NDArray[Any] | SparseMatrix | LinearOperator
    grad: NDArray[Any]
    optimality: float
    active_mask: NDArray[int32]
    nfev: int
    njev: int
    status: Literal[-1, 0, 1, 2, 3, 4]
    message: str
    success: bool

TERMINATION_MESSAGES: dict[int, str]
FROM_MINPACK_TO_COMMON: dict[int, int]

def call_minpack(fun, x0, jac, ftol, xtol, gtol, max_nfev, x_scale, diff_step): ...
def prepare_bounds(bounds, n): ...
def check_tolerance(ftol, xtol, gtol, method): ...
def check_x_scale(x_scale, x0): ...
def check_jac_sparsity(jac_sparsity, m, n): ...
def huber(z, rho, cost_only) -> None: ...
def soft_l1(z, rho, cost_only) -> None: ...
def cauchy(z, rho, cost_only) -> None: ...
def arctan(z, rho, cost_only) -> None: ...

# z, rho, cost_only
IMPLEMENTED_LOSSES: dict[str, Callable[..., Any] | None]

def construct_loss_function(m, loss, f_scale): ...
def least_squares(
    fun: Callable[..., NDArray[Any]],
    x0: ArrayLike,
    jac: Literal["2-point", "3-point", "cs"] | Callable[..., NDArray[Any]] = ...,
    bounds: tuple[ArrayLike, ArrayLike] | Bounds = ...,
    method: Literal["trf", "dogbox", "lm"] = ...,
    ftol: float | None = ...,
    xtol: float | None = ...,
    gtol: float | None = ...,
    x_scale: ArrayLike | Literal["jac"] = ...,
    loss: Literal["linear", "soft_l1", "huber", "cauchy", "arctan"]
    | Callable[[NDArray[Any]], NDArray[Any]] = ...,
    f_scale: float = ...,
    diff_step: ArrayLike | None = ...,
    tr_solver: Literal["exact", "lsmr"] | None = ...,
    tr_options: dict[str, Any] = ...,
    jac_sparsity: ArrayLike | SparseMatrix | None = ...,
    max_nfev: int | None = ...,
    verbose: Literal[0, 1, 2] = ...,
    args: Iterable[Any] = ...,
    kwargs: dict[str, Any] = ...,
) -> LeastSquaresOptimizeResult: ...
