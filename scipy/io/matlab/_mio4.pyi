from collections.abc import Iterable
from typing import Any, BinaryIO, Literal, TypedDict

from numpy import dtype
from numpy.typing import ArrayLike, NDArray
from scipy.sparse import coo_matrix
from scipy.sparse._base import _spbase as SparseMatrix

from ._miobase import MatFileReader

ByteOrder = Literal["<", ">"]
SupportedByteOrderCode = Literal[
    "little", "big", "l", "b", "le", "be", "<", ">", "native", "=", "swapped", "s"
]

class MatFileReaderArgs(TypedDict):
    byte_order: SupportedByteOrderCode | None
    mat_dtype: bool
    squeeze_me: bool
    chars_as_strings: bool
    matlab_compatible: bool
    struct_as_record: bool
    verify_compressed_data_integrity: bool
    simplify_cells: bool

SYS_LITTLE_ENDIAN: bool
miDOUBLE: int
miSINGLE: int
miINT32: int
miINT16: int
miUINT16: int
miUINT8: int
mdtypes_template: dict[int | str, str | tuple[tuple[str, str], ...]]
np_to_mtypes: dict[str, int]
mxFULL_CLASS: int
mxCHAR_CLASS: int
mxSPARSE_CLASS: int
order_codes: dict[int, str]
mclass_info: dict[int, str]

class VarHeader4:
    is_logical: bool
    is_global: bool
    name: bytes
    dtype: dtype[Any]
    mclass: int
    dims: int
    is_complex: bool

    def __init__(
        self, name: bytes, dtype: dtype[Any], mclass: int, dims: int, is_complex: bool
    ) -> None: ...

class VarReader4:
    file_reader: MatFile4Reader
    mat_stream: BinaryIO
    dtypes: dict[str, dtype[Any]]
    chars_as_strings: bool
    squeeze_me: bool

    def __init__(self, file_reader: MatFile4Reader) -> None: ...
    def read_header(self) -> VarHeader4: ...
    def array_from_header(
        self, hdr: VarHeader4, process: bool = ...
    ) -> NDArray[Any]: ...
    def read_sub_array(self, hdr: VarHeader4, copy: bool = ...) -> NDArray[Any]: ...
    def read_full_array(self, hdr: VarHeader4) -> NDArray[Any]: ...
    def read_char_array(self, hdr: VarHeader4) -> NDArray[Any]: ...
    def read_sparse_array(self, hdr: VarHeader4) -> coo_matrix: ...
    def shape_from_header(self, hdr: VarHeader4) -> tuple[int, ...]: ...

class MatFile4Reader(MatFileReader):
    dtypes: dict[str, dtype[Any]]

    def __init__(
        self, mat_stream: BinaryIO, *args: Iterable[Any], **kwargs: MatFileReaderArgs
    ) -> None: ...
    def guess_byte_order(self) -> ByteOrder: ...
    def initialize_read(self) -> None: ...
    def read_var_header(self) -> VarHeader4: ...
    def read_var_array(
        self, header: VarHeader4, process: bool = ...
    ) -> NDArray[Any]: ...
    def get_variables(
        self, variable_names: str | Iterable[str] | None = ...
    ) -> dict[str, Any]: ...
    def list_variables(self) -> list[tuple[str, tuple[int, ...], str]]: ...

def arr_to_2d(
    arr: NDArray[Any], oned_as: Literal["row", "column"] = ...
) -> NDArray[Any]: ...

class VarWriter4:
    file_stream: MatFile4Writer
    oned_as: Literal["row", "column"]

    def __init__(self, file_writer: MatFile4Writer) -> None: ...
    def write_bytes(self, arr: NDArray[Any]) -> None: ...
    def write_string(self, s: str) -> None: ...
    def write_header(
        self,
        name: str,
        shape: Iterable[int],
        P: int = ...,
        T: int = ...,
        imagf: int = ...,
    ) -> None: ...
    def write(self, arr: ArrayLike | SparseMatrix, name: str) -> None: ...
    def write_numeric(self, arr: NDArray[Any], name: str) -> None: ...
    def write_char(self, arr: NDArray[Any], name: str) -> None: ...
    def write_sparse(self, arr: SparseMatrix, name: str) -> None: ...

class MatFile4Writer:
    file_stream: BinaryIO
    oned_as: Literal["row", "column"]
    def __init__(
        self, file_stream: BinaryIO, oned_as: Literal["row", "column"] | None = ...
    ) -> None: ...
    def put_variables(
        self, mdict: dict[str, Any], write_header: bool | None = ...
    ) -> None: ...

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
