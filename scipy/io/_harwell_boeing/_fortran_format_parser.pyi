from _typeshed import Incomplete

__all__ = ['BadFortranFormat', 'FortranFormatParser', 'IntFormat', 'ExpFormat']

class BadFortranFormat(SyntaxError): ...

class IntFormat:
    @classmethod
    def from_number(cls, n, min: Incomplete | None = None): ...
    width: Incomplete
    repeat: Incomplete
    min: Incomplete
    def __init__(self, width, min: Incomplete | None = None, repeat: Incomplete | None = None) -> None: ...
    @property
    def fortran_format(self): ...
    @property
    def python_format(self): ...

class ExpFormat:
    @classmethod
    def from_number(cls, n, min: Incomplete | None = None): ...
    width: Incomplete
    significand: Incomplete
    repeat: Incomplete
    min: Incomplete
    def __init__(self, width, significand, min: Incomplete | None = None, repeat: Incomplete | None = None) -> None: ...
    @property
    def fortran_format(self): ...
    @property
    def python_format(self): ...

class Token:
    type: Incomplete
    value: Incomplete
    pos: Incomplete
    def __init__(self, type, value, pos) -> None: ...

class Tokenizer:
    tokens: Incomplete
    res: Incomplete
    def __init__(self) -> None: ...
    data: Incomplete
    curpos: int
    len: Incomplete
    def input(self, s) -> None: ...
    def next_token(self): ...

class FortranFormatParser:
    tokenizer: Incomplete
    def __init__(self) -> None: ...
    def parse(self, s): ...