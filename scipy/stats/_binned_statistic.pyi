from _typeshed import Incomplete
from typing import NamedTuple, Literal

from collections.abc import Callable, Iterable
from numpy import float64, int64
from numpy.typing import ArrayLike, NDArray

class BinnedStatisticResult(NamedTuple):
    statistic: Incomplete
    bin_edges: Incomplete
    binnumber: Incomplete

def binned_statistic(
    x, values, statistic: str = "mean", bins: int = 10, range: Incomplete | None = None
): ...

class BinnedStatistic2dResult(NamedTuple):
    statistic: Incomplete
    x_edge: Incomplete
    y_edge: Incomplete
    binnumber: Incomplete

def binned_statistic_2d(
    x: ArrayLike,
    y: ArrayLike,
    values: ArrayLike | Iterable[ArrayLike],
    statistic: Literal["mean", "std", "median", "count", "sum", "min", "max"]
    | Callable[[ArrayLike], float] = ...,
    bins: int | tuple[int, int] | ArrayLike | tuple[ArrayLike, ArrayLike] = ...,
    range: ArrayLike = ...,
    expand_binnumbers: bool = ...,
) -> tuple[NDArray[float64], NDArray[float64], NDArray[float64], NDArray[int64]]: ...

class BinnedStatisticddResult(NamedTuple):
    statistic: Incomplete
    bin_edges: Incomplete
    binnumber: Incomplete

def binned_statistic_dd(
    sample,
    values,
    statistic: str = "mean",
    bins: int = 10,
    range: Incomplete | None = None,
    expand_binnumbers: bool = False,
    binned_statistic_result: Incomplete | None = None,
): ...

__all__ = ["binned_statistic", "binned_statistic_2d", "binned_statistic_dd"]
