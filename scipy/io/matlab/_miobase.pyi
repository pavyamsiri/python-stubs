from _typeshed import Incomplete

__all__ = [
    "MatFileReader",
    "MatReadError",
    "MatReadWarning",
    "MatVarReader",
    "MatWriteError",
    "arr_dtype_number",
    "arr_to_chars",
    "convert_dtypes",
    "doc_dict",
    "docfiller",
    "get_matfile_version",
    "matdims",
    "read_dtype",
]

class MatReadError(Exception): ...
class MatWriteError(Exception): ...
class MatReadWarning(UserWarning): ...

doc_dict: Incomplete
docfiller: Incomplete

def convert_dtypes(dtype_template, order_code): ...
def read_dtype(mat_stream, a_dtype): ...

get_matfile_version = matfile_version

def matdims(arr, oned_as: str = "column"): ...

class MatVarReader:
    def __init__(self, file_reader) -> None: ...
    def read_header(self) -> None: ...
    def array_from_header(self, header) -> None: ...

class MatFileReader:
    mat_stream: Incomplete
    dtypes: Incomplete
    byte_order: Incomplete
    struct_as_record: Incomplete
    squeeze_me: Incomplete
    chars_as_strings: Incomplete
    mat_dtype: Incomplete
    verify_compressed_data_integrity: Incomplete
    simplify_cells: Incomplete
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
        simplify_cells: bool = False,
    ) -> None: ...
    def set_matlab_compatible(self) -> None: ...
    def guess_byte_order(self): ...
    def end_of_stream(self): ...

def arr_dtype_number(arr, num): ...
def arr_to_chars(arr): ...
