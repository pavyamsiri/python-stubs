from _typeshed import Incomplete
from scipy import special as special, stats as stats
from typing import NamedTuple

class _MWU:
    def __init__(self) -> None: ...
    def pmf(self, k, m, n): ...
    def pmf_recursive(self, k, m, n): ...
    def pmf_iterative(self, k, m, n): ...
    def cdf(self, k, m, n): ...
    def sf(self, k, m, n): ...

class MannwhitneyuResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def mannwhitneyu(
    x,
    y,
    use_continuity: bool = True,
    alternative: str = "two-sided",
    axis: int = 0,
    method: str = "auto",
): ...
