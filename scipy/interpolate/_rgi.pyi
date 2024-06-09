from _typeshed import Incomplete

__all__ = ['RegularGridInterpolator', 'interpn']

class RegularGridInterpolator:
    method: Incomplete
    bounds_error: Incomplete
    values: Incomplete
    fill_value: Incomplete
    def __init__(self, points, values, method: str = 'linear', bounds_error: bool = True, fill_value=..., *, solver: Incomplete | None = None, solver_args: Incomplete | None = None) -> None: ...
    def __call__(self, xi, method: Incomplete | None = None, *, nu: Incomplete | None = None): ...

def interpn(points, values, xi, method: str = 'linear', bounds_error: bool = True, fill_value=...): ...
