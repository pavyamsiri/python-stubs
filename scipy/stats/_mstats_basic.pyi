from _typeshed import Incomplete
from typing import NamedTuple

__all__ = [
    "argstoarray",
    "count_tied_groups",
    "describe",
    "f_oneway",
    "find_repeats",
    "friedmanchisquare",
    "kendalltau",
    "kendalltau_seasonal",
    "kruskal",
    "kruskalwallis",
    "ks_twosamp",
    "ks_2samp",
    "kurtosis",
    "kurtosistest",
    "ks_1samp",
    "kstest",
    "linregress",
    "mannwhitneyu",
    "meppf",
    "mode",
    "moment",
    "mquantiles",
    "msign",
    "normaltest",
    "obrientransform",
    "pearsonr",
    "plotting_positions",
    "pointbiserialr",
    "rankdata",
    "scoreatpercentile",
    "sem",
    "sen_seasonal_slopes",
    "skew",
    "skewtest",
    "spearmanr",
    "siegelslopes",
    "theilslopes",
    "tmax",
    "tmean",
    "tmin",
    "trim",
    "trimboth",
    "trimtail",
    "trima",
    "trimr",
    "trimmed_mean",
    "trimmed_std",
    "trimmed_stde",
    "trimmed_var",
    "tsem",
    "ttest_1samp",
    "ttest_onesamp",
    "ttest_ind",
    "ttest_rel",
    "tvar",
    "variation",
    "winsorize",
    "brunnermunzel",
]

def argstoarray(*args): ...
def find_repeats(arr): ...
def count_tied_groups(x, use_missing: bool = False): ...
def rankdata(data, axis: Incomplete | None = None, use_missing: bool = False): ...

class ModeResult(NamedTuple):
    mode: Incomplete
    count: Incomplete

def mode(a, axis: int = 0): ...
def msign(x): ...
def pearsonr(x, y): ...
def spearmanr(
    x,
    y: Incomplete | None = None,
    use_ties: bool = True,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
    alternative: str = "two-sided",
): ...
def kendalltau(
    x,
    y,
    use_ties: bool = True,
    use_missing: bool = False,
    method: str = "auto",
    alternative: str = "two-sided",
): ...
def kendalltau_seasonal(x): ...

class PointbiserialrResult(NamedTuple):
    correlation: Incomplete
    pvalue: Incomplete

def pointbiserialr(x, y): ...
def linregress(x, y: Incomplete | None = None): ...
def theilslopes(
    y, x: Incomplete | None = None, alpha: float = 0.95, method: str = "separate"
): ...
def siegelslopes(y, x: Incomplete | None = None, method: str = "hierarchical"): ...
def sen_seasonal_slopes(x): ...

class Ttest_1sampResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def ttest_1samp(a, popmean, axis: int = 0, alternative: str = "two-sided"): ...

ttest_onesamp = ttest_1samp

class Ttest_indResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def ttest_ind(
    a, b, axis: int = 0, equal_var: bool = True, alternative: str = "two-sided"
): ...

class Ttest_relResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def ttest_rel(a, b, axis: int = 0, alternative: str = "two-sided"): ...

class MannwhitneyuResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def mannwhitneyu(x, y, use_continuity: bool = True): ...

class KruskalResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def kruskal(*args): ...

kruskalwallis = kruskal

def ks_1samp(x, cdf, args=(), alternative: str = "two-sided", method: str = "auto"): ...
def ks_2samp(data1, data2, alternative: str = "two-sided", method: str = "auto"): ...

ks_twosamp = ks_2samp

def kstest(
    data1, data2, args=(), alternative: str = "two-sided", method: str = "auto"
): ...
def trima(a, limits: Incomplete | None = None, inclusive=(True, True)): ...
def trimr(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: Incomplete | None = None,
): ...
def trim(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    relative: bool = False,
    axis: Incomplete | None = None,
): ...
def trimboth(
    data,
    proportiontocut: float = 0.2,
    inclusive=(True, True),
    axis: Incomplete | None = None,
): ...
def trimtail(
    data,
    proportiontocut: float = 0.2,
    tail: str = "left",
    inclusive=(True, True),
    axis: Incomplete | None = None,
): ...

trim1 = trimtail

def trimmed_mean(
    a,
    limits=(0.1, 0.1),
    inclusive=(1, 1),
    relative: bool = True,
    axis: Incomplete | None = None,
): ...
def trimmed_var(
    a,
    limits=(0.1, 0.1),
    inclusive=(1, 1),
    relative: bool = True,
    axis: Incomplete | None = None,
    ddof: int = 0,
): ...
def trimmed_std(
    a,
    limits=(0.1, 0.1),
    inclusive=(1, 1),
    relative: bool = True,
    axis: Incomplete | None = None,
    ddof: int = 0,
): ...
def trimmed_stde(
    a, limits=(0.1, 0.1), inclusive=(1, 1), axis: Incomplete | None = None
): ...
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
    a, lowerlimit: Incomplete | None = None, axis: int = 0, inclusive: bool = True
): ...
def tmax(
    a, upperlimit: Incomplete | None = None, axis: int = 0, inclusive: bool = True
): ...
def tsem(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    axis: int = 0,
    ddof: int = 1,
): ...
def winsorize(
    a,
    limits: Incomplete | None = None,
    inclusive=(True, True),
    inplace: bool = False,
    axis: Incomplete | None = None,
    nan_policy: str = "propagate",
): ...
def moment(a, moment: int = 1, axis: int = 0): ...
def variation(a, axis: int = 0, ddof: int = 0): ...
def skew(a, axis: int = 0, bias: bool = True): ...
def kurtosis(a, axis: int = 0, fisher: bool = True, bias: bool = True): ...

class DescribeResult(NamedTuple):
    nobs: Incomplete
    minmax: Incomplete
    mean: Incomplete
    variance: Incomplete
    skewness: Incomplete
    kurtosis: Incomplete

def describe(a, axis: int = 0, ddof: int = 0, bias: bool = True): ...

class SkewtestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def skewtest(a, axis: int = 0, alternative: str = "two-sided"): ...

class KurtosistestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def kurtosistest(a, axis: int = 0, alternative: str = "two-sided"): ...

class NormaltestResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def normaltest(a, axis: int = 0): ...
def mquantiles(
    a,
    prob=...,
    alphap: float = 0.4,
    betap: float = 0.4,
    axis: Incomplete | None = None,
    limit=(),
): ...
def scoreatpercentile(data, per, limit=(), alphap: float = 0.4, betap: float = 0.4): ...
def plotting_positions(data, alpha: float = 0.4, beta: float = 0.4): ...

meppf = plotting_positions

def obrientransform(*args): ...
def sem(a, axis: int = 0, ddof: int = 1): ...

class F_onewayResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def f_oneway(*args): ...

class FriedmanchisquareResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def friedmanchisquare(*args): ...

class BrunnerMunzelResult(NamedTuple):
    statistic: Incomplete
    pvalue: Incomplete

def brunnermunzel(x, y, alternative: str = "two-sided", distribution: str = "t"): ...
