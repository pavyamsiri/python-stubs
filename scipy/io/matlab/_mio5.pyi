from ._byteordercodes import native_code as native_code, swapped_code as swapped_code
from ._mio5_params import (
    MDTYPES as MDTYPES,
    MatlabFunction as MatlabFunction,
    MatlabObject as MatlabObject,
    NP_TO_MTYPES as NP_TO_MTYPES,
    NP_TO_MXTYPES as NP_TO_MXTYPES,
    mat_struct as mat_struct,
    mclass_info as mclass_info,
    miCOMPRESSED as miCOMPRESSED,
    miINT8 as miINT8,
    miMATRIX as miMATRIX,
    miUINT32 as miUINT32,
    miUTF8 as miUTF8,
    mxCELL_CLASS as mxCELL_CLASS,
    mxCHAR_CLASS as mxCHAR_CLASS,
    mxDOUBLE_CLASS as mxDOUBLE_CLASS,
    mxOBJECT_CLASS as mxOBJECT_CLASS,
    mxSPARSE_CLASS as mxSPARSE_CLASS,
    mxSTRUCT_CLASS as mxSTRUCT_CLASS,
)
from ._mio5_utils import VarReader5 as VarReader5
from ._miobase import (
    MatFileReader as MatFileReader,
    MatReadError as MatReadError,
    MatReadWarning as MatReadWarning,
    MatWriteError as MatWriteError,
    arr_dtype_number as arr_dtype_number,
    arr_to_chars as arr_to_chars,
    docfiller as docfiller,
    matdims as matdims,
    read_dtype as read_dtype,
)
from ._streams import ZlibInputStream as ZlibInputStream
from _typeshed import Incomplete

class MatFile5Reader(MatFileReader):
    uint16_codec: Incomplete
    def __init__(
        self,
        mat_stream,
        byte_order: Incomplete | None = None,
        mat_dtype: bool = False,
        squeeze_me: bool = False,
        chars_as_strings: bool = True,
        matlab_compatible: bool = False,
        struct_as_record: bool = True,
        verify_compressed_data_integrity: bool = True,
        uint16_codec: Incomplete | None = None,
        simplify_cells: bool = False,
    ) -> None: ...
    def guess_byte_order(self): ...
    def read_file_header(self): ...
    def initialize_read(self) -> None: ...
    def read_var_header(self): ...
    def read_var_array(self, header, process: bool = True): ...
    def get_variables(self, variable_names: Incomplete | None = None): ...
    def list_variables(self): ...

def varmats_from_mat(file_obj): ...

class EmptyStructMarker: ...

def to_writeable(source): ...

NDT_FILE_HDR: Incomplete
NDT_TAG_FULL: Incomplete
NDT_TAG_SMALL: Incomplete
NDT_ARRAY_FLAGS: Incomplete

class VarWriter5:
    mat_tag: Incomplete
    file_stream: Incomplete
    unicode_strings: Incomplete
    long_field_names: Incomplete
    oned_as: Incomplete
    def __init__(self, file_writer) -> None: ...
    def write_bytes(self, arr) -> None: ...
    def write_string(self, s) -> None: ...
    def write_element(self, arr, mdtype: Incomplete | None = None) -> None: ...
    def write_smalldata_element(self, arr, mdtype, byte_count) -> None: ...
    def write_regular_element(self, arr, mdtype, byte_count) -> None: ...
    def write_header(
        self,
        shape,
        mclass,
        is_complex: bool = False,
        is_logical: bool = False,
        nzmax: int = 0,
    ) -> None: ...
    def update_matrix_tag(self, start_pos) -> None: ...
    def write_top(self, arr, name, is_global) -> None: ...
    def write(self, arr) -> None: ...
    def write_numeric(self, arr) -> None: ...
    def write_char(self, arr, codec: str = "ascii") -> None: ...
    def write_sparse(self, arr) -> None: ...
    def write_cells(self, arr) -> None: ...
    def write_empty_struct(self) -> None: ...
    def write_struct(self, arr) -> None: ...
    def write_object(self, arr) -> None: ...

class MatFile5Writer:
    file_stream: Incomplete
    do_compression: Incomplete
    unicode_strings: Incomplete
    global_vars: Incomplete
    long_field_names: Incomplete
    oned_as: Incomplete
    def __init__(
        self,
        file_stream,
        do_compression: bool = False,
        unicode_strings: bool = False,
        global_vars: Incomplete | None = None,
        long_field_names: bool = False,
        oned_as: str = "row",
    ) -> None: ...
    def write_file_header(self) -> None: ...
    def put_variables(self, mdict, write_header: Incomplete | None = None) -> None: ...
