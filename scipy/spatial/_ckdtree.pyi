import _cython_3_0_10
import scipy as scipy
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__reduce_cython__: _cython_3_0_10.cython_function_or_method
__setstate_cython__: _cython_3_0_10.cython_function_or_method
__test__: dict
copy_if_needed: bool

class cKDTree:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    boxsize: Incomplete
    data: Incomplete
    indices: Incomplete
    leafsize: Incomplete
    m: Incomplete
    maxes: Incomplete
    mins: Incomplete
    n: Incomplete
    size: Incomplete
    tree: Incomplete
    def __init__(self, data, leafsize=..., compact_nodes=..., copy_data=..., 
balanced_tree=..., boxsize=...) -> Any: ...
    def count_neighbors(self, other, r, p=..., weights=..., cumulative=...) -> Any: ...
    def query(self, x, k=..., eps=..., p=..., distance_upper_bound=..., workers=...) -> Any: ...
    def query_ball_point(self, x, r, p=..., eps=..., workers=..., return_sorted=..., 
return_length=...) -> Any: ...
    @overload
    def query_ball_tree(self, other, r, p=..., eps=...) -> Any: ...
    @overload
    def query_ball_tree(self, kd_tree2, r=...) -> Any: ...
    @overload
    def query_pairs(self, r, p=..., eps=..., output_type=...) -> Any: ...
    @overload
    def query_pairs(self, r=...) -> Any: ...
    def sparse_distance_matrix(self, other, max_distance, p=...) -> Any: ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...

class cKDTreeNode:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    children: Incomplete
    data_points: Incomplete
    end_idx: Incomplete
    greater: Incomplete
    indices: Incomplete
    lesser: Incomplete
    level: Incomplete
    split: Incomplete
    split_dim: Incomplete
    start_idx: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...

class coo_entries:
    __array_interface__: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def coo_matrix(self, *args, **kwargs): ...
    def dict(self, *args, **kwargs): ...
    def dok_matrix(self, *args, **kwargs): ...
    def ndarray(self, *args, **kwargs): ...
    def __reduce__(self): ...

class ordered_pairs:
    __array_interface__: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def ndarray(self, *args, **kwargs): ...
    def set(self, *args, **kwargs): ...
    def __reduce__(self): ...