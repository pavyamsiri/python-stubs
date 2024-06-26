from .common import (
    CL_scaling_vector as CL_scaling_vector,
    EPS as EPS,
    build_quadratic_1d as build_quadratic_1d,
    compute_grad as compute_grad,
    evaluate_quadratic as evaluate_quadratic,
    find_active_constraints as find_active_constraints,
    in_bounds as in_bounds,
    make_strictly_feasible as make_strictly_feasible,
    minimize_quadratic_1d as minimize_quadratic_1d,
    print_header_linear as print_header_linear,
    print_iteration_linear as print_iteration_linear,
    reflective_transformation as reflective_transformation,
    regularized_lsq_operator as regularized_lsq_operator,
    right_multiplied_operator as right_multiplied_operator,
    step_size_to_bound as step_size_to_bound,
)
from .givens_elimination import givens_elimination as givens_elimination
from _typeshed import Incomplete
from scipy.linalg import qr as qr, solve_triangular as solve_triangular
from scipy.optimize import OptimizeResult as OptimizeResult
from scipy.sparse.linalg import lsmr as lsmr

def regularized_lsq_with_qr(m, n, R, QTb, perm, diag, copy_R: bool = True): ...
def backtracking(A, g, x, p, theta, p_dot_g, lb, ub): ...
def select_step(x, A_h, g_h, c_h, p, p_h, d, lb, ub, theta): ...
def trf_linear(
    A,
    b,
    x_lsq,
    lb,
    ub,
    tol,
    lsq_solver,
    lsmr_tol,
    max_iter,
    verbose,
    *,
    lsmr_maxiter: Incomplete | None = None,
): ...
