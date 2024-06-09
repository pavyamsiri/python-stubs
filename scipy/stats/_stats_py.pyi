from ._stats_mstats_common import (
    linregress as linregress,
    siegelslopes as siegelslopes,
    theilslopes as theilslopes,
)
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import NamedTuple

__all__ = [
    "find_repeats",
    "gmean",
    "hmean",
    "pmean",
    "mode",
    "tmean",
    "tvar",
    "tmin",
    "tmax",
    "tstd",
    "tsem",
    "moment",
    "skew",
    "kurtosis",
    "describe",
    "skewtest",
    "kurtosistest",
    "normaltest",
    "jarque_bera",
    "scoreatpercentile",
    "percentileofscore",
    "cumfreq",
    "relfreq",
    "obrientransform",
    "sem",
    "zmap",
    "zscore",
    "gzscore",
    "iqr",
    "gstd",
    "median_abs_deviation",
    "sigmaclip",
    "trimboth",
    "trim1",
    "trim_mean",
    "f_oneway",
    "pearsonr",
    "fisher_exact",
    "spearmanr",
    "pointbiserialr",
    "kendalltau",
    "weightedtau",
    "multiscale_graphcorr",
    "linregress",
    "siegelslopes",
    "theilslopes",
    "ttest_1samp",
    "ttest_ind",
    "ttest_ind_from_stats",
    "ttest_rel",
    "kstest",
    "ks_1samp",
    "ks_2samp",
    "chisquare",
    "power_divergence",
    "tiecorrect",
    "ranksums",
    "kruskal",
    "friedmanchisquare",
    "rankdata",
    "combine_pvalues",
    "quantile_test",
    "wasserstein_distance",
    "wasserstein_distance_nd",
    "energy_distance",
    "brunnermunzel",
    "alexandergovern",
    "expectile",
]

def gmean(
    a, axis: int = 0, dtype: Incomplete | None = None, weights: Incomplete | None = None
): ...
def hmean(
    a,
    axis: int = 0,
    dtype: Incomplete | None = None,
    *,
    weights: Incomplete | None = None,
): ...
def pmean(
    a,
    p,
    *,
    axis: int = 0,
    dtype: Incomplete | None = None,
    weights: Incomplete | None = None,
): ...

class ModeResult(NamedTuple):
    mode: Incomplete
    count: Incomplete

def mode(a, axis: int = 0, nan_policy: str = "propagate", keepdims: bool = False): ...
def tmean(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: Incomplete | None = None,
): ...
def tvar(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: int = 0,
    ddof: int = 1,
): ...
def tmin(
    a,
    lowerlimit: Incomplete | None = None,
    axis: int = 0,
    inclusive: bool = True,
    nan_policy: str = "propagate",
): ...
def tmax(
    a,
    upperlimit: Incomplete | None = None,
    axis: int = 0,
    inclusive: bool = True,
    nan_policy: str = "propagate",
): ...
def tstd(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: int = 0,
    ddof: int = 1,
): ...
def tsem(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: int = 0,
    ddof: int = 1,
): ...
def moment(
    a,
    order: int = 1,
    axis: int = 0,
    nan_policy: str = "propagate",
    *,
    center: Incomplete | None = None,
): ...
def skew(a, axis: int = 0, bias: bool = True, nan_policy: str = "propagate"): ...
def kurtosis(
    a,
    axis: int = 0,
    fisher: bool = True,
    bias: bool = True,
    nan_policy: str = "propagate",
): ...

class DescribeResult(NamedTuple):
    nobs: Incomplete
    minmax: Incomplete
    mean: Incomplete
    variance: Incomplete
    skewness: Incomplete
    kurtosis: Incomplete

def describe(
    a, axis: int = 0, ddof: int = 1, bias: bool = True, nan_policy: str = "propagate"
): ...

class SkewtestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def skewtest(
    a, axis: int = 0, nan_policy: str = "propagate", alternative: str = "two-sided"
): ...

class KurtosistestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def kurtosistest(
    a, axis: int = 0, nan_policy: str = "propagate", alternative: str = "two-sided"
): ...

class NormaltestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def normaltest(a, axis: int = 0, nan_policy: str = "propagate"): ...
def jarque_bera(x, *, axis: Incomplete | None = None): ...
def scoreatpercentile(
    a,
    per,
    limit=(),
    interpolation_method: str = "fraction",
    axis: Incomplete | None = None,
): ...
def percentileofscore(a, score, kind: str = "rank", nan_policy: str = "propagate"): ...

class HistogramResult(NamedTuple):
    count: Incomplete
    lowerlimit: Incomplete
    binsize: Incomplete
    extrapoints: Incomplete

class CumfreqResult(NamedTuple):
    cumcount: Incomplete
    lowerlimit: Incomplete
    binsize: Incomplete
    extrapoints: Incomplete

def cumfreq(
    a,
    numbins: int = 10,
    defaultreallimits: Incomplete | None = None,
    weights: Incomplete | None = None,
): ...

class RelfreqResult(NamedTuple):
    frequency: Incomplete
    lowerlimit: Incomplete
    binsize: Incomplete
    extrapoints: Incomplete

def relfreq(
    a,
    numbins: int = 10,
    defaultreallimits: Incomplete | None = None,
    weights: Incomplete | None = None,
): ...
def obrientransform(*samples): ...
def sem(a, axis: int = 0, ddof: int = 1, nan_policy: str = "propagate"): ...
def zscore(a, axis: int = 0, ddof: int = 0, nan_policy: str = "propagate"): ...
def gzscore(a, *, axis: int = 0, ddof: int = 0, nan_policy: str = "propagate"): ...
def zmap(
    scores, compare, axis: int = 0, ddof: int = 0, nan_policy: str = "propagate"
): ...
def gstd(a, axis: int = 0, ddof: int = 1): ...
def iqr(
    x,
    axis: Incomplete | None = None,
    rng=(25, 75),
    scale: float = 1.0,
    nan_policy: str = "propagate",
    interpolation: str = "linear",
    keepdims: bool = False,
): ...
def median_abs_deviation(
    x, axis: int = 0, center=..., scale: float = 1.0, nan_policy: str = "propagate"
): ...

class SigmaclipResult(NamedTuple):
    clipped: Incomplete
    lower: Incomplete
    upper: Incomplete

def sigmaclip(a, low: float = 4.0, high: float = 4.0): ...
def trimboth(a, proportiontocut, axis: int = 0): ...
def trim1(a, proportiontocut, tail: str = "right", axis: int = 0): ...
def trim_mean(a, proportiontocut, axis: int = 0): ...

class F_onewayResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def f_oneway(*samples, axis: int = 0): ...
@dataclass
class AlexanderGovernResult:
    statistic: float
    pvalue: float
    def __init__(self, statistic, pvalue) -> None: ...

def alexandergovern(*samples, nan_policy: str = "propagate"): ...

class ConfidenceInterval(NamedTuple):
    low: Incomplete
    high: Incomplete

class PearsonRResult(PearsonRResultBase):
    correlation: Incomplete
    def __init__(self, statistic, pvalue, alternative, n, x, y) -> None: ...
    def confidence_interval(
        self, confidence_level: float = 0.95, method: Incomplete | None = None
    ): ...

def pearsonr(
    x, y, *, alternative: str = "two-sided", method: Incomplete | None = None
): ...
def fisher_exact(table, alternative: str = "two-sided"): ...
def spearmanr(
    a,
    b: Incomplete | None = None,
    axis: int = 0,
    nan_policy: str = "propagate",
    alternative: str = "two-sided",
): ...
def pointbiserialr(x, y): ...
def kendalltau(
    x,
    y,
    *,
    initial_lexsort=...,
    nan_policy: str = "propagate",
    method: str = "auto",
    variant: str = "b",
    alternative: str = "two-sided",
): ...
def weightedtau(
    x, y, rank: bool = True, weigher: Incomplete | None = None, additive: bool = True
): ...

class _ParallelP:
    x: Incomplete
    y: Incomplete
    random_states: Incomplete
    def __init__(self, x, y, random_states) -> None: ...
    def __call__(self, index): ...

def multiscale_graphcorr(
    x,
    y,
    compute_distance=...,
    reps: int = 1000,
    workers: int = 1,
    is_twosamp: bool = False,
    random_state: Incomplete | None = None,
): ...

class TtestResult(TtestResultBase):
    def __init__(
        self, statistic, pvalue, df, alternative, standard_error, estimate
    ) -> None: ...
    def confidence_interval(self, confidence_level: float = 0.95): ...

def ttest_1samp(
    a,
    popmean,
    axis: int = 0,
    nan_policy: str = "propagate",
    alternative: str = "two-sided",
): ...

class Ttest_indResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def ttest_ind_from_stats(
    mean1,
    std1,
    nobs1,
    mean2,
    std2,
    nobs2,
    equal_var: bool = True,
    alternative: str = "two-sided",
): ...
def ttest_ind(
    a,
    b,
    axis: int = 0,
    equal_var: bool = True,
    nan_policy: str = "propagate",
    permutations: Incomplete | None = None,
    random_state: Incomplete | None = None,
    alternative: str = "two-sided",
    trim: int = 0,
): ...
def ttest_rel(
    a, b, axis: int = 0, nan_policy: str = "propagate", alternative: str = "two-sided"
): ...

class Power_divergenceResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def power_divergence(
    f_obs,
    f_exp: Incomplete | None = None,
    ddof: int = 0,
    axis: int = 0,
    lambda_: Incomplete | None = None,
): ...
def chisquare(f_obs, f_exp: Incomplete | None = None, ddof: int = 0, axis: int = 0): ...
def ks_1samp(x, cdf, args=(), alternative: str = "two-sided", method: str = "auto"): ...

Ks_2sampResult = KstestResult

def ks_2samp(data1, data2, alternative: str = "two-sided", method: str = "auto"): ...
def kstest(
    rvs, cdf, args=(), N: int = 20, alternative: str = "two-sided", method: str = "auto"
): ...
def tiecorrect(rankvals): ...

class RanksumsResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def ranksums(x, y, alternative: str = "two-sided"): ...

class KruskalResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def kruskal(*samples, nan_policy: str = "propagate"): ...

class FriedmanchisquareResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def friedmanchisquare(*samples): ...

class BrunnerMunzelResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def brunnermunzel(
    x,
    y,
    alternative: str = "two-sided",
    distribution: str = "t",
    nan_policy: str = "propagate",
): ...
def combine_pvalues(
    pvalues, method: str = "fisher", weights: Incomplete | None = None
): ...
@dataclass
class QuantileTestResult:
    statistic: float
    statistic_type: int
    pvalue: float
    def confidence_interval(self, confidence_level: float = 0.95): ...
    def __init__(
        self, statistic, statistic_type, pvalue, _alternative, _x, _p
    ) -> None: ...

def quantile_test(x, *, q: int = 0, p: float = 0.5, alternative: str = "two-sided"): ...
def wasserstein_distance_nd(
    u_values,
    v_values,
    u_weights: Incomplete | None = None,
    v_weights: Incomplete | None = None,
): ...
def wasserstein_distance(
    u_values,
    v_values,
    u_weights: Incomplete | None = None,
    v_weights: Incomplete | None = None,
): ...
def energy_distance(
    u_values,
    v_values,
    u_weights: Incomplete | None = None,
    v_weights: Incomplete | None = None,
): ...

class RepeatedResults(NamedTuple):
    values: Incomplete
    counts: Incomplete

def find_repeats(arr): ...
def rankdata(
    a,
    method: str = "average",
    *,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
): ...
def expectile(a, alpha: float = 0.5, *, weights: Incomplete | None = None): ...
