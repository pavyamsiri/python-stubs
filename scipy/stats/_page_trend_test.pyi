from ._continuous_distns import norm as norm
from _typeshed import Incomplete
from dataclasses import dataclass

@dataclass
class PageTrendTestResult:
    statistic: float
    pvalue: float
    method: str
    def __init__(self, statistic, pvalue, method) -> None: ...

def page_trend_test(
    data,
    ranked: bool = False,
    predicted_ranks: Incomplete | None = None,
    method: str = "auto",
): ...

class _PageL:
    all_pmfs: Incomplete
    def __init__(self) -> None: ...
    k: Incomplete
    def set_k(self, k) -> None: ...
    def sf(self, l, n): ...
    def p_l_k_1(self): ...
    def pmf(self, l, n): ...
