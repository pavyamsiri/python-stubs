from _typeshed import Incomplete
from scipy.optimize import OptimizeResult as OptimizeResult
from scipy.sparse import coo_matrix as coo_matrix, csc_matrix as csc_matrix
from scipy.sparse.linalg import splu as splu

EPS: Incomplete

def estimate_fun_jac(fun, x, y, p, f0: Incomplete | None = None): ...
def estimate_bc_jac(bc, ya, yb, p, bc0: Incomplete | None = None): ...
def compute_jac_indices(n, m, k): ...
def stacked_matmul(a, b): ...
def construct_global_jac(
    n,
    m,
    k,
    i_jac,
    j_jac,
    h,
    df_dy,
    df_dy_middle,
    df_dp,
    df_dp_middle,
    dbc_dya,
    dbc_dyb,
    dbc_dp,
): ...
def collocation_fun(fun, y, p, x, h): ...
def prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, h): ...
def solve_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol): ...
def print_iteration_header() -> None: ...
def print_iteration_progress(
    iteration, residual, bc_residual, total_nodes, nodes_added
) -> None: ...

class BVPResult(OptimizeResult): ...

TERMINATION_MESSAGES: Incomplete

def estimate_rms_residuals(fun, sol, x, h, p, r_middle, f_middle): ...
def create_spline(y, yp, x, h): ...
def modify_mesh(x, insert_1, insert_2): ...
def wrap_functions(fun, bc, fun_jac, bc_jac, k, a, S, D, dtype): ...
def solve_bvp(
    fun,
    bc,
    x,
    y,
    p: Incomplete | None = None,
    S: Incomplete | None = None,
    fun_jac: Incomplete | None = None,
    bc_jac: Incomplete | None = None,
    tol: float = 0.001,
    max_nodes: int = 1000,
    verbose: int = 0,
    bc_tol: Incomplete | None = None,
): ...
