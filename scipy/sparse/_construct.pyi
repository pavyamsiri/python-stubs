from _typeshed import Incomplete

__all__ = [
    "spdiags",
    "eye",
    "identity",
    "kron",
    "kronsum",
    "hstack",
    "vstack",
    "bmat",
    "rand",
    "random",
    "diags",
    "block_diag",
    "diags_array",
    "block_array",
    "eye_array",
    "random_array",
]

def spdiags(
    data,
    diags,
    m: Incomplete | None = None,
    n: Incomplete | None = None,
    format: Incomplete | None = None,
): ...
def diags_array(
    diagonals,
    /,
    *,
    offsets: int = 0,
    shape: Incomplete | None = None,
    format: Incomplete | None = None,
    dtype: Incomplete | None = None,
): ...
def diags(
    diagonals,
    offsets: int = 0,
    shape: Incomplete | None = None,
    format: Incomplete | None = None,
    dtype: Incomplete | None = None,
): ...
def identity(n, dtype: str = "d", format: Incomplete | None = None): ...
def eye_array(
    m,
    n: Incomplete | None = None,
    *,
    k: int = 0,
    dtype=...,
    format: Incomplete | None = None,
): ...
def eye(
    m,
    n: Incomplete | None = None,
    k: int = 0,
    dtype=...,
    format: Incomplete | None = None,
): ...
def kron(A, B, format: Incomplete | None = None): ...
def kronsum(A, B, format: Incomplete | None = None): ...
def hstack(
    blocks, format: Incomplete | None = None, dtype: Incomplete | None = None
): ...
def vstack(
    blocks, format: Incomplete | None = None, dtype: Incomplete | None = None
): ...
def bmat(blocks, format: Incomplete | None = None, dtype: Incomplete | None = None): ...
def block_array(
    blocks, *, format: Incomplete | None = None, dtype: Incomplete | None = None
): ...
def block_diag(
    mats, format: Incomplete | None = None, dtype: Incomplete | None = None
): ...
def random_array(
    shape,
    *,
    density: float = 0.01,
    format: str = "coo",
    dtype: Incomplete | None = None,
    random_state: Incomplete | None = None,
    data_sampler: Incomplete | None = None,
): ...
def random(
    m,
    n,
    density: float = 0.01,
    format: str = "coo",
    dtype: Incomplete | None = None,
    random_state: Incomplete | None = None,
    data_rvs: Incomplete | None = None,
): ...
def rand(
    m,
    n,
    density: float = 0.01,
    format: str = "coo",
    dtype: Incomplete | None = None,
    random_state: Incomplete | None = None,
): ...
