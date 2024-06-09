import numpy as np
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import NamedTuple

__all__ = [
    "epps_singleton_2samp",
    "cramervonmises",
    "somersd",
    "barnard_exact",
    "boschloo_exact",
    "cramervonmises_2samp",
    "tukey_hsd",
    "poisson_means_test",
]

class Epps_Singleton_2sampResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def epps_singleton_2samp(x, y, t=(0.4, 0.8)): ...
def poisson_means_test(
    k1, n1, k2, n2, *, diff: int = 0, alternative: str = "two-sided"
): ...

class CramerVonMisesResult:
    statistic: Incomplete
    pvalue: Incomplete
    def __init__(self, statistic, pvalue) -> None: ...

def cramervonmises(rvs, cdf, args=()): ...
@dataclass
class SomersDResult:
    statistic: float
    pvalue: float
    table: np.ndarray
    def __init__(self, statistic, pvalue, table) -> None: ...

def somersd(x, y: Incomplete | None = None, alternative: str = "two-sided"): ...
@dataclass
class BarnardExactResult:
    statistic: float
    pvalue: float
    def __init__(self, statistic, pvalue) -> None: ...

def barnard_exact(
    table, alternative: str = "two-sided", pooled: bool = True, n: int = 32
): ...
@dataclass
class BoschlooExactResult:
    statistic: float
    pvalue: float
    def __init__(self, statistic, pvalue) -> None: ...

def boschloo_exact(table, alternative: str = "two-sided", n: int = 32): ...
def cramervonmises_2samp(x, y, method: str = "auto"): ...

class TukeyHSDResult:
    statistic: Incomplete
    pvalue: Incomplete
    def __init__(self, statistic, pvalue, _nobs, _ntreatments, _stand_err) -> None: ...
    def confidence_interval(self, confidence_level: float = 0.95): ...

def tukey_hsd(*args): ...
