from scipy.linalg._flapack import *
from _typeshed import Incomplete

__all__ = ["get_lapack_funcs"]

def get_lapack_funcs(
    names, arrays=(), dtype: Incomplete | None = None, ilp64: bool = False
): ...
