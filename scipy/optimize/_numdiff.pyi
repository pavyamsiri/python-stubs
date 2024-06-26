from ..sparse import (
    coo_matrix as coo_matrix,
    csc_matrix as csc_matrix,
    csr_matrix as csr_matrix,
    find as find,
    issparse as issparse,
)
from ._group_columns import group_dense as group_dense, group_sparse as group_sparse
from _typeshed import Incomplete
from scipy._lib._array_api import (
    array_namespace as array_namespace,
    atleast_nd as atleast_nd,
)
from scipy.sparse.linalg import LinearOperator as LinearOperator

def group_columns(A, order: int = 0): ...
def approx_derivative(
    fun,
    x0,
    method: str = "3-point",
    rel_step: Incomplete | None = None,
    abs_step: Incomplete | None = None,
    f0: Incomplete | None = None,
    bounds=...,
    sparsity: Incomplete | None = None,
    as_linear_operator: bool = False,
    args=(),
    kwargs={},
): ...
def check_derivative(fun, jac, x0, bounds=..., args=(), kwargs={}): ...
