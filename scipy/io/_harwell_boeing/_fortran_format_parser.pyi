from re import Pattern

from _typeshed import Incomplete
from typing_extensions import Self

class BadFortranFormat(SyntaxError): ...

class IntFormat:
    @classmethod
    def from_number(cls, n: int, min: int | None = ...) -> Self: ...

    width: int
    repeat: int
    min: int

    def __init__(
        self, width: int, min: int | None = ..., repeat: int | None = ...
    ) -> None: ...
    @property
    def fortran_format(self) -> str: ...
    @property
    def python_format(self) -> str: ...

class ExpFormat:
    @classmethod
    def from_number(cls, n: float, min: int | None = ...) -> Self: ...

    width: int
    significand: int
    min: int | None
    repeat: int | None

    def __init__(
        self,
        width: int,
        significand: int,
        min: int | None = ...,
        repeat: int | None = ...,
    ) -> None: ...
    @property
    def fortran_format(self) -> str: ...
    @property
    def python_format(self) -> str: ...

class Token:
    type: str
    value: str
    pos: int
    def __init__(self, type: str, value: str, pos: int) -> None: ...

class Tokenizer:
    tokens: list[str]
    res: list[Pattern[str]]
    data: str
    curpos: int
    len: int

    def __init__(self) -> None: ...
    def input(self, s: str) -> None: ...
    def next_token(self) -> Token: ...

class FortranFormatParser:
    tokenizer: Incomplete
    def __init__(self) -> None: ...
    def parse(self, s: str) -> ExpFormat | IntFormat: ...

__all__ = ["BadFortranFormat", "FortranFormatParser", "IntFormat", "ExpFormat"]
