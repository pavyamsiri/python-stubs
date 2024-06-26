import _cython_3_0_10
import scipy.io.matlab._mio5_params as mio5p
from _typeshed import Incomplete
from scipy.io.matlab._mio_utils import (
    chars_to_strings as chars_to_strings,
    squeeze_element as squeeze_element,
)
from scipy.sparse._csc import csc_matrix as csc_matrix
from typing import ClassVar

__reduce_cython__: _cython_3_0_10.cython_function_or_method
__setstate_cython__: _cython_3_0_10.cython_function_or_method
__test__: dict
byteswap_u4: _cython_3_0_10.cython_function_or_method
swapped_code: str

class VarHeader5:
    dims: Incomplete
    is_global: Incomplete
    is_logical: Incomplete
    mclass: Incomplete
    name: Incomplete
    nzmax: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def set_dims(self, *args, **kwargs): ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...

class VarReader5:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    is_swapped: Incomplete
    little_endian: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def array_from_header(self, *args, **kwargs): ...
    def read_cells(self, *args, **kwargs): ...
    def read_char(self, *args, **kwargs): ...
    def read_fieldnames(self, *args, **kwargs): ...
    def read_full_tag(self, *args, **kwargs): ...
    def read_header(self, *args, **kwargs): ...
    def read_numeric(self, *args, **kwargs): ...
    def read_opaque(self, *args, **kwargs): ...
    def read_real_complex(self, *args, **kwargs): ...
    def read_struct(self, *args, **kwargs): ...
    def read_tag(self, *args, **kwargs): ...
    def set_stream(self, *args, **kwargs): ...
    def shape_from_header(self, *args, **kwargs): ...
    def __reduce__(self): ...
