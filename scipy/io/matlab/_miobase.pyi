from typing import Any, BinaryIO, Literal, TypeVar

from numpy import dtype, generic
from numpy.typing import NDArray
from scipy._lib import doccer

T = TypeVar("T", bound=generic)
ByteOrder = Literal["<", ">"]
SupportedByteOrderCode = Literal[
    "little", "big", "l", "b", "le", "be", "<", ">", "native", "=", "swapped", "s"
]

class MatReadError(Exception): ...
class MatWriteError(Exception): ...
class MatReadWarning(UserWarning): ...

doc_dict: dict[str, str]
docfiller: doccer.Decorator[...]

def matfile_version(
    file_name: str, *, appendmat: bool = ...
) -> tuple[Literal[0, 1, 2], int]: ...
def convert_dtypes(
    dtype_template: dict[str, dtype[Any]], order_code: str
) -> dict[str, dtype[Any]]: ...
def read_dtype(mat_stream: BinaryIO, a_dtype: type[T]) -> NDArray[T]: ...

get_matfile_version = matfile_version

def matdims(
    arr: NDArray[Any], oned_as: Literal["row", "column"] = ...
) -> tuple[int, ...]: ...

class MatVarReader:
    def __init__(self, file_reader: Any) -> None: ...
    def read_header(self) -> None: ...
    def array_from_header(self, header: Any) -> None: ...

class MatFileReader:
    mat_stream: BinaryIO
    dtypes: dict[str, dtype[Any]]
    byte_order: ByteOrder
    struct_as_record: bool
    squeeze_me: bool
    chars_as_strings: bool
    mat_dtype: bool
    verify_compressed_data_integrity: bool
    simplify_cells: bool

    def __init__(
        self,
        mat_stream: BinaryIO,
        byte_order: SupportedByteOrderCode | None = ...,
        mat_dtype: bool = ...,
        squeeze_me: bool = ...,
        chars_as_strings: bool = ...,
        matlab_compatible: bool = ...,
        struct_as_record: bool = ...,
        verify_compressed_data_integrity: bool = ...,
        simplify_cells: bool = ...,
    ) -> None: ...
    def set_matlab_compatible(self) -> None: ...
    def guess_byte_order(self) -> ByteOrder: ...
    def end_of_stream(self) -> bool: ...

def arr_dtype_number(arr: NDArray[Any], num: int) -> dtype[Any]: ...
def arr_to_chars(arr: NDArray[Any]) -> NDArray[Any]: ...

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
