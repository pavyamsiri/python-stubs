from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['binned_statistic', 'binned_statistic_2d', 'binned_statistic_dd']

class BinnedStatisticResult(NamedTuple):
    statistic: Incomplete
    bin_edges: Incomplete
    binnumber: Incomplete

def binned_statistic(x, values, statistic: str = 'mean', bins: int = 10, range: Incomplete | None = None): ...

class BinnedStatistic2dResult(NamedTuple):
    statistic: Incomplete
    x_edge: Incomplete
    y_edge: Incomplete
    binnumber: Incomplete

def binned_statistic_2d(x, y, values, statistic: str = 'mean', bins: int = 10, range: Incomplete | None = None, expand_binnumbers: bool = False): ...

class BinnedStatisticddResult(NamedTuple):
    statistic: Incomplete
    bin_edges: Incomplete
    binnumber: Incomplete

def binned_statistic_dd(sample, values, statistic: str = 'mean', bins: int = 10, range: Incomplete | None = None, expand_binnumbers: bool = False, binned_statistic_result: Incomplete | None = None): ...
