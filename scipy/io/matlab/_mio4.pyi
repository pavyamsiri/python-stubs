from ._miobase import MatFileReader
from _typeshed import Incomplete

__all__ = [
    "MatFile4Reader",
    "MatFile4Writer",
    "SYS_LITTLE_ENDIAN",
    "VarHeader4",
    "VarReader4",
    "VarWriter4",
    "arr_to_2d",
    "mclass_info",
    "mdtypes_template",
    "miDOUBLE",
    "miINT16",
    "miINT32",
    "miSINGLE",
    "miUINT16",
    "miUINT8",
    "mxCHAR_CLASS",
    "mxFULL_CLASS",
    "mxSPARSE_CLASS",
    "np_to_mtypes",
    "order_codes",
]

SYS_LITTLE_ENDIAN: Incomplete
miDOUBLE: int
miSINGLE: int
miINT32: int
miINT16: int
miUINT16: int
miUINT8: int
mdtypes_template: Incomplete
np_to_mtypes: Incomplete
mxFULL_CLASS: int
mxCHAR_CLASS: int
mxSPARSE_CLASS: int
order_codes: Incomplete
mclass_info: Incomplete

class VarHeader4:
    is_logical: bool
    is_global: bool
    name: Incomplete
    dtype: Incomplete
    mclass: Incomplete
    dims: Incomplete
    is_complex: Incomplete
    def __init__(self, name, dtype, mclass, dims, is_complex) -> None: ...

class VarReader4:
    file_reader: Incomplete
    mat_stream: Incomplete
    dtypes: Incomplete
    chars_as_strings: Incomplete
    squeeze_me: Incomplete
    def __init__(self, file_reader) -> None: ...
    def read_header(self): ...
    def array_from_header(self, hdr, process: bool = True): ...
    def read_sub_array(self, hdr, copy: bool = True): ...
    def read_full_array(self, hdr): ...
    def read_char_array(self, hdr): ...
    def read_sparse_array(self, hdr): ...
    def shape_from_header(self, hdr): ...

class MatFile4Reader(MatFileReader):
    def __init__(self, mat_stream, *args, **kwargs) -> None: ...
    def guess_byte_order(self): ...
    dtypes: Incomplete
    def initialize_read(self) -> None: ...
    def read_var_header(self): ...
    def read_var_array(self, header, process: bool = True): ...
    def get_variables(self, variable_names: Incomplete | None = None): ...
    def list_variables(self): ...

def arr_to_2d(arr, oned_as: str = "row"): ...

class VarWriter4:
    file_stream: Incomplete
    oned_as: Incomplete
    def __init__(self, file_writer) -> None: ...
    def write_bytes(self, arr) -> None: ...
    def write_string(self, s) -> None: ...
    def write_header(self, name, shape, P=..., T=..., imagf: int = 0) -> None: ...
    def write(self, arr, name) -> None: ...
    def write_numeric(self, arr, name) -> None: ...
    def write_char(self, arr, name) -> None: ...
    def write_sparse(self, arr, name) -> None: ...

class MatFile4Writer:
    file_stream: Incomplete
    oned_as: Incomplete
    def __init__(self, file_stream, oned_as: Incomplete | None = None) -> None: ...
    def put_variables(self, mdict, write_header: Incomplete | None = None) -> None: ...
