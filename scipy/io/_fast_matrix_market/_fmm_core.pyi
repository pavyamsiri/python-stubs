import io
import numpy
from typing import overload

__version__: str

class _read_cursor:
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...
    @property
    def header(self) -> header: ...

class _write_cursor:
    def __init__(self, *args, **kwargs) -> None: ...

class header:
    comment: str
    field: str
    format: str
    ncols: int
    nnz: int
    nrows: int
    object: str
    shape: tuple[int, int]
    symmetry: str
    def __init__(
        self,
        shape: tuple[int, int] = ...,
        nnz: int = ...,
        comment: str = ...,
        object: str = ...,
        format: str = ...,
        field: str = ...,
        symmetry: str = ...,
    ) -> None: ...

def open_read_file(arg0: str, arg1: int) -> _read_cursor: ...
def open_read_stream(arg0: io.BytesIO, arg1: int) -> _read_cursor: ...
def open_write_file(arg0: str, arg1: header, arg2: int, arg3: int) -> _write_cursor: ...
def open_write_stream(
    arg0: io.BytesIO, arg1: header, arg2: int, arg3: int
) -> _write_cursor: ...
@overload
def read_body_array(arg0: _read_cursor, arg1: numpy.ndarray[numpy.int64]) -> None: ...
@overload
def read_body_array(arg0: _read_cursor, arg1: numpy.ndarray[numpy.uint64]) -> None: ...
@overload
def read_body_array(arg0: _read_cursor, arg1: numpy.ndarray[numpy.float64]) -> None: ...
@overload
def read_body_array(
    arg0: _read_cursor, arg1: numpy.ndarray[numpy.complex128]
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int32],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int32],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.uint64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int32],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.float64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int32],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.complex128],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int64],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int64],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.uint64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int64],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.float64],
) -> None: ...
@overload
def read_body_coo(
    arg0: _read_cursor,
    arg1: numpy.ndarray[numpy.int64],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.complex128],
) -> None: ...
@overload
def write_body_array(arg0: _write_cursor, arg1: numpy.ndarray[numpy.int32]) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.uint32]
) -> None: ...
@overload
def write_body_array(arg0: _write_cursor, arg1: numpy.ndarray[numpy.int64]) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.uint64]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.float32]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.float64]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.longdouble]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.complex64]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.complex128]
) -> None: ...
@overload
def write_body_array(
    arg0: _write_cursor, arg1: numpy.ndarray[numpy.longcomplex]
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.int32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.uint32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.int64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.uint64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.float32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.float64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.longdouble],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.complex64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.complex128],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int32],
    arg3: numpy.ndarray[numpy.int32],
    arg4: numpy.ndarray[numpy.longcomplex],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.int32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.uint32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.int64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.uint64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.float32],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.float64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.longdouble],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.complex64],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.complex128],
) -> None: ...
@overload
def write_body_coo(
    arg0: _write_cursor,
    arg1: tuple[int, int],
    arg2: numpy.ndarray[numpy.int64],
    arg3: numpy.ndarray[numpy.int64],
    arg4: numpy.ndarray[numpy.longcomplex],
) -> None: ...
