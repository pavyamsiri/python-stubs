from .common import (
    EPS as EPS,
    in_bounds as in_bounds,
    make_strictly_feasible as make_strictly_feasible,
)
from .dogbox import dogbox as dogbox
from .trf import trf as trf
from _typeshed import Incomplete
from scipy.optimize import OptimizeResult as OptimizeResult
from scipy.optimize._minimize import Bounds as Bounds
from scipy.optimize._numdiff import (
    approx_derivative as approx_derivative,
    group_columns as group_columns,
)
from scipy.sparse import issparse as issparse
from scipy.sparse.linalg import LinearOperator as LinearOperator

TERMINATION_MESSAGES: Incomplete
FROM_MINPACK_TO_COMMON: Incomplete

def call_minpack(fun, x0, jac, ftol, xtol, gtol, max_nfev, x_scale, diff_step): ...
def prepare_bounds(bounds, n): ...
def check_tolerance(ftol, xtol, gtol, method): ...
def check_x_scale(x_scale, x0): ...
def check_jac_sparsity(jac_sparsity, m, n): ...
def huber(z, rho, cost_only) -> None: ...
def soft_l1(z, rho, cost_only) -> None: ...
def cauchy(z, rho, cost_only) -> None: ...
def arctan(z, rho, cost_only) -> None: ...

IMPLEMENTED_LOSSES: Incomplete

def construct_loss_function(m, loss, f_scale): ...
def least_squares(
    fun,
    x0,
    jac: str = "2-point",
    bounds=...,
    method: str = "trf",
    ftol: float = 1e-08,
    xtol: float = 1e-08,
    gtol: float = 1e-08,
    x_scale: float = 1.0,
    loss: str = "linear",
    f_scale: float = 1.0,
    diff_step: Incomplete | None = None,
    tr_solver: Incomplete | None = None,
    tr_options={},
    jac_sparsity: Incomplete | None = None,
    max_nfev: Incomplete | None = None,
    verbose: int = 0,
    args=(),
    kwargs={},
): ...
