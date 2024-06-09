import _cython_3_0_10
from scipy.sparse._base import (
    SparseEfficiencyWarning as SparseEfficiencyWarning,
    issparse as issparse,
)
from scipy.sparse._csr import csr_matrix as csr_matrix
from scipy.sparse._sputils import (
    convert_pydata_sparse_to_scipy as convert_pydata_sparse_to_scipy,
)
from scipy.sparse.csgraph._matching import (
    maximum_bipartite_matching as maximum_bipartite_matching,
)

__test__: dict
reverse_cuthill_mckee: _cython_3_0_10.cython_function_or_method
structural_rank: _cython_3_0_10.cython_function_or_method
