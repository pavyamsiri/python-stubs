from _typeshed import Incomplete

__all__ = [
    "solve",
    "solve_triangular",
    "solveh_banded",
    "solve_banded",
    "solve_toeplitz",
    "solve_circulant",
    "inv",
    "det",
    "lstsq",
    "pinv",
    "pinvh",
    "matrix_balance",
    "matmul_toeplitz",
]

def solve(
    a,
    b,
    lower: bool = False,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
    assume_a: str = "gen",
    transposed: bool = False,
): ...
def solve_triangular(
    a,
    b,
    trans: int = 0,
    lower: bool = False,
    unit_diagonal: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
): ...
def solve_banded(
    l_and_u,
    ab,
    b,
    overwrite_ab: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
): ...
def solveh_banded(
    ab,
    b,
    overwrite_ab: bool = False,
    overwrite_b: bool = False,
    lower: bool = False,
    check_finite: bool = True,
): ...
def solve_toeplitz(c_or_cr, b, check_finite: bool = True): ...
def solve_circulant(
    c,
    b,
    singular: str = "raise",
    tol: Incomplete | None = None,
    caxis: int = -1,
    baxis: int = 0,
    outaxis: int = 0,
): ...
def inv(a, overwrite_a: bool = False, check_finite: bool = True): ...
def det(a, overwrite_a: bool = False, check_finite: bool = True): ...
def lstsq(
    a,
    b,
    cond: Incomplete | None = None,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
    lapack_driver: Incomplete | None = None,
): ...
def pinv(
    a,
    *,
    atol: Incomplete | None = None,
    rtol: Incomplete | None = None,
    return_rank: bool = False,
    check_finite: bool = True,
    cond=...,
    rcond=...,
): ...
def pinvh(
    a,
    atol: Incomplete | None = None,
    rtol: Incomplete | None = None,
    lower: bool = True,
    return_rank: bool = False,
    check_finite: bool = True,
): ...
def matrix_balance(
    A,
    permute: bool = True,
    scale: bool = True,
    separate: bool = False,
    overwrite_a: bool = False,
): ...
def matmul_toeplitz(
    c_or_cr, x, check_finite: bool = False, workers: Incomplete | None = None
): ...
