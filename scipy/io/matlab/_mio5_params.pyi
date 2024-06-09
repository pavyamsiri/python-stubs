from typing import Any, Literal, TypedDict

import numpy as np
from _typeshed import Incomplete
from numpy import dtype
from numpy.typing import ArrayLike
from typing_extensions import Self

ByteOrder = Literal["<", ">"]

class CodecsTemplate(TypedDict):
    codec: Literal["utf_8", "utf_16", "utf_32"]
    width: Literal[1, 2, 4]

class MDTypeDef(TypedDict):
    dtypes: dict[str, dtype[Any]]
    classes: dict[str, dtype[Any]]
    codecs: dict[str, str]

miINT8: int
miUINT8: int
miINT16: int
miUINT16: int
miINT32: int
miUINT32: int
miSINGLE: int
miDOUBLE: int
miINT64: int
miUINT64: int
miMATRIX: int
miCOMPRESSED: int
miUTF8: int
miUTF16: int
miUTF32: int
mxCELL_CLASS: int
mxSTRUCT_CLASS: int
mxOBJECT_CLASS: int
mxCHAR_CLASS: int
mxSPARSE_CLASS: int
mxDOUBLE_CLASS: int
mxSINGLE_CLASS: int
mxINT8_CLASS: int
mxUINT8_CLASS: int
mxINT16_CLASS: int
mxUINT16_CLASS: int
mxINT32_CLASS: int
mxUINT32_CLASS: int
mxINT64_CLASS: int
mxUINT64_CLASS: int
mxFUNCTION_CLASS: int
mxOPAQUE_CLASS: int
mxOBJECT_CLASS_FROM_MATRIX_H: int
mdtypes_template: dict[int, str]
mclass_dtypes_template: dict[int, str]
mclass_info: dict[int, str]
NP_TO_MTYPES: dict[str, int]
NP_TO_MXTYPES: dict[str, int]
codecs_template: dict[int, CodecsTemplate]
MDTYPES: dict[ByteOrder, MDTypeDef]

class mat_struct: ...

class MatlabObject(np.ndarray[Any, Any]):
    classname: str

    def __new__(cls, input_array: ArrayLike, classname: str | None = ...) -> Self: ...
    def __array_finalize__(self, obj: Any) -> None: ...

class MatlabFunction(np.ndarray[Any, Any]):
    def __new__(cls, input_array: ArrayLike) -> Self: ...

class MatlabOpaque(np.ndarray[Any, Any]):
    def __new__(cls, input_array: ArrayLike) -> Self: ...

OPAQUE_DTYPE: Incomplete

__all__ = [
    "MDTYPES",
    "MatlabFunction",
    "MatlabObject",
    "MatlabOpaque",
    "NP_TO_MTYPES",
    "NP_TO_MXTYPES",
    "OPAQUE_DTYPE",
    "codecs_template",
    "mat_struct",
    "mclass_dtypes_template",
    "mclass_info",
    "mdtypes_template",
    "miCOMPRESSED",
    "miDOUBLE",
    "miINT16",
    "miINT32",
    "miINT64",
    "miINT8",
    "miMATRIX",
    "miSINGLE",
    "miUINT16",
    "miUINT32",
    "miUINT64",
    "miUINT8",
    "miUTF16",
    "miUTF32",
    "miUTF8",
    "mxCELL_CLASS",
    "mxCHAR_CLASS",
    "mxDOUBLE_CLASS",
    "mxFUNCTION_CLASS",
    "mxINT16_CLASS",
    "mxINT32_CLASS",
    "mxINT64_CLASS",
    "mxINT8_CLASS",
    "mxOBJECT_CLASS",
    "mxOBJECT_CLASS_FROM_MATRIX_H",
    "mxOPAQUE_CLASS",
    "mxSINGLE_CLASS",
    "mxSPARSE_CLASS",
    "mxSTRUCT_CLASS",
    "mxUINT16_CLASS",
    "mxUINT32_CLASS",
    "mxUINT64_CLASS",
    "mxUINT8_CLASS",
]
