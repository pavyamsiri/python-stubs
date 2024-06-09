from collections.abc import Callable, Iterable
from functools import partial
from typing import Any, Literal

from typing_extensions import TypeAlias

IntrospectableCallable: TypeAlias = Callable[..., Any]

__all__ = ["PytestTester", "check_free_memory", "_TestPythranFunc", "IS_MUSL"]

IS_MUSL: bool

class FPUModeChangeWarning(RuntimeWarning): ...

class PytestTester:
    module_name: str
    def __init__(self, module_name: str) -> None: ...
    def __call__(
        self,
        label: Literal["fast", "full"] | str = ...,
        verbose: int = ...,
        extra_argv: Iterable[str] | None = ...,
        doctests: bool = ...,
        coverage: bool = ...,
        tests: Iterable[str] | None = ...,
        parallel: int | None = ...,
    ) -> bool: ...

class _TestPythranFunc:
    ALL_INTEGER: list[type]
    ALL_FLOAT: list[type]
    ALL_COMPLEX: list[type]
    arguments: dict[int, tuple[Any, Iterable[type]]]
    partialfunc: partial[Any]
    expected: Any
    def setup_method(self) -> None: ...
    def get_optional_args(self, func: IntrospectableCallable) -> dict[str, Any]: ...
    def get_max_dtype_list_length(self) -> int: ...
    def get_dtype(self, dtype_list: Iterable[type], dtype_idx: int) -> type: ...
    def test_all_dtypes(self) -> None: ...
    def test_views(self) -> None: ...
    def test_strided(self) -> None: ...

def check_free_memory(free_mb: float) -> None: ...
