from collections.abc import Iterable
from typing import Any, Literal, TypedDict

from ._miobase import MatFileReader

SupportedByteOrderCode = Literal[
    "little", "big", "l", "b", "le", "be", "<", ">", "native", "=", "swapped", "s"
]

class MatReaderFactoryArgs(TypedDict):
    byte_order: SupportedByteOrderCode | None
    mat_dtype: bool
    squeeze_me: bool
    chars_as_strings: bool
    matlab_compatible: bool
    struct_as_record: bool
    verify_compressed_data_integrity: bool
    simplify_cells: bool

class LoadMatArgs(TypedDict):
    variable_names: str | Iterable[str]
    byte_order: SupportedByteOrderCode | None
    mat_dtype: bool
    squeeze_me: bool
    chars_as_strings: bool
    matlab_compatible: bool
    struct_as_record: bool
    verify_compressed_data_integrity: bool
    simplify_cells: bool

def mat_reader_factory(
    file_name: str, appendmat: bool = ..., **kwargs: MatReaderFactoryArgs
) -> tuple[MatFileReader, bool]: ...
def loadmat(
    file_name: str,
    mdict: dict[str, Any] | None = ...,
    appendmat: bool = ...,
    **kwargs: LoadMatArgs,
) -> dict[str, Any]: ...
def savemat(
    file_name: str,
    mdict: dict[str, Any],
    appendmat: bool = ...,
    format: Literal["4", "5"] = ...,
    long_field_names: bool = ...,
    do_compression: bool = ...,
    oned_as: Literal["row", "column"] = ...,
) -> None: ...
def whosmat(file_name: str, appendmat: bool = ..., **kwargs: MatReaderFactoryArgs): ...

__all__ = ["mat_reader_factory", "loadmat", "savemat", "whosmat"]
