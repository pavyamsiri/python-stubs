from _typeshed import Incomplete

__all__ = ["PytestTester", "check_free_memory", "_TestPythranFunc", "IS_MUSL"]

IS_MUSL: bool

class FPUModeChangeWarning(RuntimeWarning): ...

class PytestTester:
    module_name: Incomplete
    def __init__(self, module_name) -> None: ...
    def __call__(
        self,
        label: str = "fast",
        verbose: int = 1,
        extra_argv: Incomplete | None = None,
        doctests: bool = False,
        coverage: bool = False,
        tests: Incomplete | None = None,
        parallel: Incomplete | None = None,
    ): ...

class _TestPythranFunc:
    ALL_INTEGER: Incomplete
    ALL_FLOAT: Incomplete
    ALL_COMPLEX: Incomplete
    arguments: Incomplete
    partialfunc: Incomplete
    expected: Incomplete
    def setup_method(self) -> None: ...
    def get_optional_args(self, func): ...
    def get_max_dtype_list_length(self): ...
    def get_dtype(self, dtype_list, dtype_idx): ...
    def test_all_dtypes(self) -> None: ...
    def test_views(self) -> None: ...
    def test_strided(self) -> None: ...

def check_free_memory(free_mb) -> None: ...
