from _typeshed import Incomplete

__all__ = [
    "eig",
    "eigvals",
    "eigh",
    "eigvalsh",
    "eig_banded",
    "eigvals_banded",
    "eigh_tridiagonal",
    "eigvalsh_tridiagonal",
    "hessenberg",
    "cdf2rdf",
]

def eig(
    a,
    b: Incomplete | None = None,
    left: bool = False,
    right: bool = True,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
    homogeneous_eigvals: bool = False,
): ...
def eigh(
    a,
    b: Incomplete | None = None,
    *,
    lower: bool = True,
    eigvals_only: bool = False,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    turbo=...,
    eigvals=...,
    type: int = 1,
    check_finite: bool = True,
    subset_by_index: Incomplete | None = None,
    subset_by_value: Incomplete | None = None,
    driver: Incomplete | None = None,
): ...
def eig_banded(
    a_band,
    lower: bool = False,
    eigvals_only: bool = False,
    overwrite_a_band: bool = False,
    select: str = "a",
    select_range: Incomplete | None = None,
    max_ev: int = 0,
    check_finite: bool = True,
): ...
def eigvals(
    a,
    b: Incomplete | None = None,
    overwrite_a: bool = False,
    check_finite: bool = True,
    homogeneous_eigvals: bool = False,
): ...
def eigvalsh(
    a,
    b: Incomplete | None = None,
    *,
    lower: bool = True,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    turbo=...,
    eigvals=...,
    type: int = 1,
    check_finite: bool = True,
    subset_by_index: Incomplete | None = None,
    subset_by_value: Incomplete | None = None,
    driver: Incomplete | None = None,
): ...
def eigvals_banded(
    a_band,
    lower: bool = False,
    overwrite_a_band: bool = False,
    select: str = "a",
    select_range: Incomplete | None = None,
    check_finite: bool = True,
): ...
def eigvalsh_tridiagonal(
    d,
    e,
    select: str = "a",
    select_range: Incomplete | None = None,
    check_finite: bool = True,
    tol: float = 0.0,
    lapack_driver: str = "auto",
): ...
def eigh_tridiagonal(
    d,
    e,
    eigvals_only: bool = False,
    select: str = "a",
    select_range: Incomplete | None = None,
    check_finite: bool = True,
    tol: float = 0.0,
    lapack_driver: str = "auto",
): ...
def hessenberg(
    a, calc_q: bool = False, overwrite_a: bool = False, check_finite: bool = True
): ...
def cdf2rdf(w, v): ...
