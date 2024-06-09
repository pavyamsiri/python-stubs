import _cython_3_0_10
from scipy.sparse._base import issparse as issparse
from scipy.sparse._csr import csr_matrix as csr_matrix
from scipy.sparse._sputils import convert_pydata_sparse_to_scipy as convert_pydata_sparse_to_scipy
from scipy.sparse.csgraph._validation import validate_graph as validate_graph

__test__: dict
bellman_ford: _cython_3_0_10.cython_function_or_method
dijkstra: _cython_3_0_10.cython_function_or_method
floyd_warshall: _cython_3_0_10.cython_function_or_method
johnson: _cython_3_0_10.cython_function_or_method
shortest_path: _cython_3_0_10.cython_function_or_method

class NegativeCycleError(Exception):
    def __init__(self, *args, **kwargs) -> None: ...
