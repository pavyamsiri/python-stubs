from ._base import _spbase, sparray
from ._index import IndexMixin
from ._matrix import spmatrix
from _typeshed import Incomplete

__all__ = ['lil_array', 'lil_matrix', 'isspmatrix_lil']

class _lil_base(_spbase, IndexMixin):
    dtype: Incomplete
    rows: Incomplete
    data: Incomplete
    def __init__(self, arg1, shape: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def __imul__(self, other): ...
    def __itruediv__(self, other): ...
    def count_nonzero(self): ...
    def getrowview(self, i): ...
    def getrow(self, i): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, x) -> None: ...
    def __truediv__(self, other): ...
    def copy(self): ...
    def reshape(self, *args, **kwargs): ...
    def resize(self, *shape) -> None: ...
    def toarray(self, order: Incomplete | None = None, out: Incomplete | None = None): ...
    def transpose(self, axes: Incomplete | None = None, copy: bool = False): ...
    def tolil(self, copy: bool = False): ...
    def tocsr(self, copy: bool = False): ...

def isspmatrix_lil(x): ...

class lil_array(_lil_base, sparray): ...
class lil_matrix(spmatrix, _lil_base): ...
