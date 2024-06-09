from typing import Any, Protocol

from _typeshed import FileDescriptorOrPath
from scipy.sparse import csc_matrix
from scipy.sparse._base import _spbase as SparseMatrix  # type: ignore[private]
from typing_extensions import Self

from ._fortran_format_parser import ExpFormat, IntFormat

class FileLike(Protocol):
    def readline(self, size: int = -1, /) -> str: ...

class Readable(Protocol):
    def read(self, size: int | None = ..., /) -> str: ...

class MalformedHeader(Exception): ...
class LineOverflow(Warning): ...

class HBInfo:
    @classmethod
    def from_data(
        cls,
        m: SparseMatrix,
        title: str = ...,
        key: str = ...,
        mxtype: HBMatrixType | None = ...,
        fmt: Any | None = ...,
    ) -> HBInfo: ...
    @classmethod
    def from_file(cls, fid: FileLike) -> Self: ...

    title: str
    key: str
    total_nlines: int
    pointer_nlines: int
    indices_nlines: int
    values_nlines: int
    pointer_format: ExpFormat | IntFormat
    indices_format: ExpFormat | IntFormat
    values_format: ExpFormat | IntFormat
    pointer_dtype: type
    indices_dtype: type
    values_dtype: type
    pointer_nbytes_full: int
    indices_nbytes_full: int
    values_nbytes_full: int
    nrows: str
    ncols: str
    nnon_zeros: int
    nelementals: int
    mxtype: HBMatrixType

    def __init__(
        self,
        title: str | None,
        key: str | None,
        total_nlines: int,
        pointer_nlines: int,
        indices_nlines: int,
        values_nlines: int,
        mxtype: HBMatrixType,
        nrows: int,
        ncols: int,
        nnon_zeros: int,
        pointer_format_str: str,
        indices_format_str: str,
        values_format_str: str,
        right_hand_sides_nlines: int = ...,
        nelementals: int = ...,
    ) -> None: ...
    def dump(self) -> str: ...

class HBMatrixType:
    @classmethod
    def from_fortran(cls, fmt: str) -> Self: ...

    value_type: str
    structure: str
    storage: str

    def __init__(self, value_type: str, structure: str, storage: str = ...) -> None: ...
    @property
    def fortran_format(self) -> str: ...

class HBFile:
    def __init__(self, file: FileLike, hb_info: HBInfo | None = ...) -> None: ...
    @property
    def title(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def structure(self) -> str: ...
    @property
    def storage(self) -> str: ...
    def read_matrix(self) -> csc_matrix: ...
    def write_matrix(self, m: SparseMatrix) -> None: ...

def hb_read(path_or_open_file: FileDescriptorOrPath | Readable) -> csc_matrix: ...
def hb_write(
    path_or_open_file: FileDescriptorOrPath | Readable,
    m: SparseMatrix,
    hb_info: HBInfo | None = ...,
) -> None: ...

__all__ = ["MalformedHeader", "hb_read", "hb_write", "HBInfo", "HBFile", "HBMatrixType"]
