import numpy.typing as npt
from ._constraints import Bounds
from scipy.optimize import OptimizeResult
from typing import Any, Callable, Iterable

__all__ = ['direct']

def direct(func: Callable[[npt.ArrayLike, tuple[Any]], float], bounds: Iterable | Bounds, *, args: tuple = (), eps: float = 0.0001, maxfun: int | None = None, maxiter: int = 1000, locally_biased: bool = True, f_min: float = ..., f_min_rtol: float = 0.0001, vol_tol: float = 1e-16, len_tol: float = 1e-06, callback: Callable[[npt.ArrayLike], None] | None = None) -> OptimizeResult: ...
