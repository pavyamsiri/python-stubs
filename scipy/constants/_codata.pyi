from typing import Any

__all__ = [
    "physical_constants",
    "value",
    "unit",
    "precision",
    "find",
    "ConstantWarning",
]

physical_constants: dict[str, tuple[float, str, float]]

class ConstantWarning(DeprecationWarning): ...

def value(key: str) -> float: ...
def unit(key: str) -> str: ...
def precision(key: str) -> float: ...
def find(sub: str | None = None, disp: bool = False) -> Any: ...
