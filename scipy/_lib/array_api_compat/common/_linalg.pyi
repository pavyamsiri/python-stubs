from ._aliases import (
    matmul as matmul,
    matrix_transpose as matrix_transpose,
    tensordot as tensordot,
    vecdot as vecdot,
)
from ._typing import ndarray
from _typeshed import Incomplete
from typing import Literal, NamedTuple

__all__ = [
    "cross",
    "matmul",
    "outer",
    "tensordot",
    "EighResult",
    "QRResult",
    "SlogdetResult",
    "SVDResult",
    "eigh",
    "qr",
    "slogdet",
    "svd",
    "cholesky",
    "matrix_rank",
    "pinv",
    "matrix_norm",
    "matrix_transpose",
    "svdvals",
    "vecdot",
    "vector_norm",
    "diagonal",
    "trace",
]

def cross(x1: ndarray, x2: ndarray, /, xp, *, axis: int = -1, **kwargs) -> ndarray: ...
def outer(x1: ndarray, x2: ndarray, /, xp, **kwargs) -> ndarray: ...

class EighResult(NamedTuple):
    eigenvalues: ndarray
    eigenvectors: ndarray

class QRResult(NamedTuple):
    Q: ndarray
    R: ndarray

class SlogdetResult(NamedTuple):
    sign: ndarray
    logabsdet: ndarray

class SVDResult(NamedTuple):
    U: ndarray
    S: ndarray
    Vh: ndarray

def eigh(x: ndarray, /, xp, **kwargs) -> EighResult: ...
def qr(
    x: ndarray, /, xp, *, mode: Literal["reduced", "complete"] = "reduced", **kwargs
) -> QRResult: ...
def slogdet(x: ndarray, /, xp, **kwargs) -> SlogdetResult: ...
def svd(x: ndarray, /, xp, *, full_matrices: bool = True, **kwargs) -> SVDResult: ...
def cholesky(x: ndarray, /, xp, *, upper: bool = False, **kwargs) -> ndarray: ...
def matrix_rank(
    x: ndarray, /, xp, *, rtol: float | ndarray | None = None, **kwargs
) -> ndarray: ...
def pinv(
    x: ndarray, /, xp, *, rtol: float | ndarray | None = None, **kwargs
) -> ndarray: ...
def matrix_norm(
    x: ndarray,
    /,
    xp,
    *,
    keepdims: bool = False,
    ord: int | float | Literal["fro", "nuc"] | None = "fro",
) -> ndarray: ...
def svdvals(x: ndarray, /, xp) -> ndarray | tuple[ndarray, ...]: ...
def vector_norm(
    x: ndarray,
    /,
    xp,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    ord: int | float | None = 2,
) -> ndarray: ...
def diagonal(x: ndarray, /, xp, *, offset: int = 0, **kwargs) -> ndarray: ...
def trace(
    x: ndarray, /, xp, *, offset: int = 0, dtype: Incomplete | None = None, **kwargs
) -> ndarray: ...
