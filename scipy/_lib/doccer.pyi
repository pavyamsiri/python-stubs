from collections.abc import Callable, Iterable
from typing import Any, TypeVar

from typing_extensions import ParamSpec, TypeAlias

P = ParamSpec("P")
R = TypeVar("R")

Decorator: TypeAlias = Callable[[Callable[..., R]], Callable[..., R]]

def docformat(docstring: str, docdict: dict[str, str] | None = ...) -> str: ...
def inherit_docstring_from(cls: type[Any] | Any) -> Decorator[R]: ...
def extend_notes_in_docstring(cls: type[Any] | Any, notes: str) -> Decorator[R]: ...
def replace_notes_in_docstring(cls: type[Any] | Any, notes: str) -> Decorator[R]: ...
def indentcount_lines(lines: Iterable[str]) -> int: ...
def filldoc(docdict: dict[str, str], unindent_params: bool = ...) -> Decorator[R]: ...
def unindent_dict(docdict: dict[str, str]) -> dict[str, str]: ...
def unindent_string(docstring: str) -> str: ...
def doc_replace(obj: type[Any] | Any, oldval: str, newval: str) -> Decorator[R]: ...

__all__ = [
    "docformat",
    "inherit_docstring_from",
    "indentcount_lines",
    "filldoc",
    "unindent_dict",
    "unindent_string",
    "extend_notes_in_docstring",
    "replace_notes_in_docstring",
    "doc_replace",
]
