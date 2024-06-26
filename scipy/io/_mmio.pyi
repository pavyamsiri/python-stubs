from _typeshed import Incomplete

__all__ = ["mminfo", "mmread", "mmwrite", "MMFile"]

def mminfo(source): ...
def mmread(source): ...
def mmwrite(
    target,
    a,
    comment: str = "",
    field: Incomplete | None = None,
    precision: Incomplete | None = None,
    symmetry: Incomplete | None = None,
) -> None: ...

class MMFile:
    @property
    def rows(self): ...
    @property
    def cols(self): ...
    @property
    def entries(self): ...
    @property
    def format(self): ...
    @property
    def field(self): ...
    @property
    def symmetry(self): ...
    @property
    def has_symmetry(self): ...
    FORMAT_COORDINATE: str
    FORMAT_ARRAY: str
    FORMAT_VALUES: Incomplete
    FIELD_INTEGER: str
    FIELD_UNSIGNED: str
    FIELD_REAL: str
    FIELD_COMPLEX: str
    FIELD_PATTERN: str
    FIELD_VALUES: Incomplete
    SYMMETRY_GENERAL: str
    SYMMETRY_SYMMETRIC: str
    SYMMETRY_SKEW_SYMMETRIC: str
    SYMMETRY_HERMITIAN: str
    SYMMETRY_VALUES: Incomplete
    DTYPES_BY_FIELD: Incomplete
    @staticmethod
    def reader() -> None: ...
    @staticmethod
    def writer() -> None: ...
    @classmethod
    def info(self, source): ...
    def __init__(self, **kwargs) -> None: ...
    def read(self, source): ...
    def write(
        self,
        target,
        a,
        comment: str = "",
        field: Incomplete | None = None,
        precision: Incomplete | None = None,
        symmetry: Incomplete | None = None,
    ) -> None: ...
