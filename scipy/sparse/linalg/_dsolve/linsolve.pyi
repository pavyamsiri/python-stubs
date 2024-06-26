from _typeshed import Incomplete

__all__ = [
    "use_solver",
    "spsolve",
    "splu",
    "spilu",
    "factorized",
    "MatrixRankWarning",
    "spsolve_triangular",
]

class MatrixRankWarning(UserWarning): ...

def use_solver(**kwargs) -> None: ...
def spsolve(A, b, permc_spec: Incomplete | None = None, use_umfpack: bool = True): ...
def splu(
    A,
    permc_spec: Incomplete | None = None,
    diag_pivot_thresh: Incomplete | None = None,
    relax: Incomplete | None = None,
    panel_size: Incomplete | None = None,
    options=...,
): ...
def spilu(
    A,
    drop_tol: Incomplete | None = None,
    fill_factor: Incomplete | None = None,
    drop_rule: Incomplete | None = None,
    permc_spec: Incomplete | None = None,
    diag_pivot_thresh: Incomplete | None = None,
    relax: Incomplete | None = None,
    panel_size: Incomplete | None = None,
    options: Incomplete | None = None,
): ...
def factorized(A): ...
def spsolve_triangular(
    A,
    b,
    lower: bool = True,
    overwrite_A: bool = False,
    overwrite_b: bool = False,
    unit_diagonal: bool = False,
): ...
