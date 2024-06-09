from scipy.linalg._fblas import *
from _typeshed import Incomplete

__all__ = ["get_blas_funcs", "find_best_blas_type"]

def find_best_blas_type(arrays=(), dtype: Incomplete | None = None): ...
def get_blas_funcs(
    names, arrays=(), dtype: Incomplete | None = None, ilp64: bool = False
): ...
