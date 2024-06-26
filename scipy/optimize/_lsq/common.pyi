from _typeshed import Incomplete
from scipy.linalg import (
    LinAlgError as LinAlgError,
    cho_factor as cho_factor,
    cho_solve as cho_solve,
)
from scipy.sparse import issparse as issparse
from scipy.sparse.linalg import (
    LinearOperator as LinearOperator,
    aslinearoperator as aslinearoperator,
)

EPS: Incomplete

def intersect_trust_region(x, s, Delta): ...
def solve_lsq_trust_region(
    n,
    m,
    uf,
    s,
    V,
    Delta,
    initial_alpha: Incomplete | None = None,
    rtol: float = 0.01,
    max_iter: int = 10,
): ...
def solve_trust_region_2d(B, g, Delta): ...
def update_tr_radius(
    Delta, actual_reduction, predicted_reduction, step_norm, bound_hit
): ...
def build_quadratic_1d(
    J, g, s, diag: Incomplete | None = None, s0: Incomplete | None = None
): ...
def minimize_quadratic_1d(a, b, lb, ub, c: int = 0): ...
def evaluate_quadratic(J, g, s, diag: Incomplete | None = None): ...
def in_bounds(x, lb, ub): ...
def step_size_to_bound(x, s, lb, ub): ...
def find_active_constraints(x, lb, ub, rtol: float = 1e-10): ...
def make_strictly_feasible(x, lb, ub, rstep: float = 1e-10): ...
def CL_scaling_vector(x, g, lb, ub): ...
def reflective_transformation(y, lb, ub): ...
def print_header_nonlinear() -> None: ...
def print_iteration_nonlinear(
    iteration, nfev, cost, cost_reduction, step_norm, optimality
) -> None: ...
def print_header_linear() -> None: ...
def print_iteration_linear(
    iteration, cost, cost_reduction, step_norm, optimality
) -> None: ...
def compute_grad(J, f): ...
def compute_jac_scale(J, scale_inv_old: Incomplete | None = None): ...
def left_multiplied_operator(J, d): ...
def right_multiplied_operator(J, d): ...
def regularized_lsq_operator(J, diag): ...
def right_multiply(J, d, copy: bool = True): ...
def left_multiply(J, d, copy: bool = True): ...
def check_termination(dF, F, dx_norm, x_norm, ratio, ftol, xtol): ...
def scale_for_robust_loss_function(J, f, rho): ...
