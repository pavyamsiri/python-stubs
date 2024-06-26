from .common import (
    print_header_linear as print_header_linear,
    print_iteration_linear as print_iteration_linear,
)
from _typeshed import Incomplete
from scipy.optimize import OptimizeResult as OptimizeResult

def compute_kkt_optimality(g, on_bound): ...
def bvls(
    A, b, x_lsq, lb, ub, tol, max_iter, verbose, rcond: Incomplete | None = None
): ...
