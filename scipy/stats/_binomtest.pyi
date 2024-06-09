from ._common import ConfidenceInterval as ConfidenceInterval
from ._discrete_distns import binom as binom
from _typeshed import Incomplete
from scipy.optimize import brentq as brentq
from scipy.special import ndtri as ndtri

class BinomTestResult:
    k: Incomplete
    n: Incomplete
    alternative: Incomplete
    statistic: Incomplete
    pvalue: Incomplete
    proportion_estimate: Incomplete
    def __init__(self, k, n, alternative, statistic, pvalue) -> None: ...
    def proportion_ci(self, confidence_level: float = 0.95, method: str = "exact"): ...

def binomtest(k, n, p: float = 0.5, alternative: str = "two-sided"): ...
