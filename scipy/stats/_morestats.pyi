from _typeshed import Incomplete
from typing import NamedTuple

__all__ = [
    "mvsdist",
    "bayes_mvs",
    "kstat",
    "kstatvar",
    "probplot",
    "ppcc_max",
    "ppcc_plot",
    "boxcox_llf",
    "boxcox",
    "boxcox_normmax",
    "boxcox_normplot",
    "shapiro",
    "anderson",
    "ansari",
    "bartlett",
    "levene",
    "fligner",
    "mood",
    "wilcoxon",
    "median_test",
    "circmean",
    "circvar",
    "circstd",
    "anderson_ksamp",
    "yeojohnson_llf",
    "yeojohnson",
    "yeojohnson_normmax",
    "yeojohnson_normplot",
    "directional_stats",
    "false_discovery_control",
]

class Mean(NamedTuple):
    statistic: Incomplete
    minmax: Incomplete

class Variance(NamedTuple):
    statistic: Incomplete
    minmax: Incomplete

class Std_dev(NamedTuple):
    statistic: Incomplete
    minmax: Incomplete

def bayes_mvs(data, alpha: float = 0.9): ...
def mvsdist(data): ...
def kstat(data, n: int = 2): ...
def kstatvar(data, n: int = 2): ...
def probplot(
    x,
    sparams=(),
    dist: str = "norm",
    fit: bool = True,
    plot: Incomplete | None = None,
    rvalue: bool = False,
): ...
def ppcc_max(x, brack=(0.0, 1.0), dist: str = "tukeylambda"): ...
def ppcc_plot(
    x, a, b, dist: str = "tukeylambda", plot: Incomplete | None = None, N: int = 80
): ...
def boxcox_llf(lmb, data): ...
def boxcox(
    x,
    lmbda: Incomplete | None = None,
    alpha: Incomplete | None = None,
    optimizer: Incomplete | None = None,
): ...

class _BigFloat: ...

def boxcox_normmax(
    x,
    brack: Incomplete | None = None,
    method: str = "pearsonr",
    optimizer: Incomplete | None = None,
    *,
    ymax=...,
): ...
def boxcox_normplot(x, la, lb, plot: Incomplete | None = None, N: int = 80): ...
def yeojohnson(x, lmbda: Incomplete | None = None): ...
def yeojohnson_llf(lmb, data): ...
def yeojohnson_normmax(x, brack: Incomplete | None = None): ...
def yeojohnson_normplot(x, la, lb, plot: Incomplete | None = None, N: int = 80): ...

class ShapiroResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def shapiro(x): ...
def anderson(x, dist: str = "norm"): ...
def anderson_ksamp(
    samples, midrank: bool = True, *, method: Incomplete | None = None
): ...

class AnsariResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

class _ABW:
    m: Incomplete
    n: Incomplete
    astart: Incomplete
    total: Incomplete
    freqs: Incomplete
    def __init__(self) -> None: ...
    def pmf(self, k, n, m): ...
    def cdf(self, k, n, m): ...
    def sf(self, k, n, m): ...

def ansari(x, y, alternative: str = "two-sided"): ...

class BartlettResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def bartlett(*samples): ...

class LeveneResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def levene(*samples, center: str = "median", proportiontocut: float = 0.05): ...

class FlignerResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def fligner(*samples, center: str = "median", proportiontocut: float = 0.05): ...
def mood(x, y, axis: int = 0, alternative: str = "two-sided"): ...
def wilcoxon(
    x,
    y: Incomplete | None = None,
    zero_method: str = "wilcox",
    correction: bool = False,
    alternative: str = "two-sided",
    method: str = "auto",
    *,
    axis: int = 0,
): ...
def median_test(
    *samples,
    ties: str = "below",
    correction: bool = True,
    lambda_: int = 1,
    nan_policy: str = "propagate",
): ...
def circmean(
    samples,
    high=...,
    low: int = 0,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
): ...
def circvar(
    samples,
    high=...,
    low: int = 0,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
): ...
def circstd(
    samples,
    high=...,
    low: int = 0,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
    *,
    normalize: bool = False,
): ...

class DirectionalStats:
    mean_direction: Incomplete
    mean_resultant_length: Incomplete
    def __init__(self, mean_direction, mean_resultant_length) -> None: ...

def directional_stats(samples, *, axis: int = 0, normalize: bool = True): ...
def false_discovery_control(ps, *, axis: int = 0, method: str = "bh"): ...
