from ._base import sparray
from ._compressed import _cs_matrix
from ._matrix import spmatrix
from _typeshed import Incomplete

__all__ = ['csr_array', 'csr_matrix', 'isspmatrix_csr']

class _csr_base(_cs_matrix):
    def transpose(self, axes: Incomplete | None = None, copy: bool = False): ...
    def tolil(self, copy: bool = False): ...
    def tocsr(self, copy: bool = False): ...
    def tocsc(self, copy: bool = False): ...
    def tobsr(self, blocksize: Incomplete | None = None, copy: bool = True): ...
    def __iter__(self): ...

def isspmatrix_csr(x): ...

class csr_array(_csr_base, sparray): ...
class csr_matrix(spmatrix, _csr_base): ...