from _typeshed import Incomplete

__all__ = ["MalformedHeader", "hb_read", "hb_write", "HBInfo", "HBFile", "HBMatrixType"]

class MalformedHeader(Exception): ...
class LineOverflow(Warning): ...

class HBInfo:
    @classmethod
    def from_data(
        cls,
        m,
        title: str = "Default title",
        key: str = "0",
        mxtype: Incomplete | None = None,
        fmt: Incomplete | None = None,
    ): ...
    @classmethod
    def from_file(cls, fid): ...
    title: Incomplete
    key: Incomplete
    total_nlines: Incomplete
    pointer_nlines: Incomplete
    indices_nlines: Incomplete
    values_nlines: Incomplete
    pointer_format: Incomplete
    indices_format: Incomplete
    values_format: Incomplete
    pointer_dtype: Incomplete
    indices_dtype: Incomplete
    values_dtype: Incomplete
    pointer_nbytes_full: Incomplete
    indices_nbytes_full: Incomplete
    values_nbytes_full: Incomplete
    nrows: Incomplete
    ncols: Incomplete
    nnon_zeros: Incomplete
    nelementals: Incomplete
    mxtype: Incomplete
    def __init__(
        self,
        title,
        key,
        total_nlines,
        pointer_nlines,
        indices_nlines,
        values_nlines,
        mxtype,
        nrows,
        ncols,
        nnon_zeros,
        pointer_format_str,
        indices_format_str,
        values_format_str,
        right_hand_sides_nlines: int = 0,
        nelementals: int = 0,
    ) -> None: ...
    def dump(self): ...

class HBMatrixType:
    @classmethod
    def from_fortran(cls, fmt): ...
    value_type: Incomplete
    structure: Incomplete
    storage: Incomplete
    def __init__(self, value_type, structure, storage: str = "assembled") -> None: ...
    @property
    def fortran_format(self): ...

class HBFile:
    def __init__(self, file, hb_info: Incomplete | None = None) -> None: ...
    @property
    def title(self): ...
    @property
    def key(self): ...
    @property
    def type(self): ...
    @property
    def structure(self): ...
    @property
    def storage(self): ...
    def read_matrix(self): ...
    def write_matrix(self, m): ...

def hb_read(path_or_open_file): ...
def hb_write(path_or_open_file, m, hb_info: Incomplete | None = None): ...
