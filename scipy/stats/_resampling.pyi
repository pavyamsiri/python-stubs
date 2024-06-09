import numpy as np
from ._common import ConfidenceInterval
from _typeshed import Incomplete
from dataclasses import dataclass

__all__ = ["bootstrap", "monte_carlo_test", "permutation_test"]

@dataclass
class BootstrapResult:
    confidence_interval: ConfidenceInterval
    bootstrap_distribution: np.ndarray
    standard_error: float | np.ndarray
    def __init__(
        self, confidence_interval, bootstrap_distribution, standard_error
    ) -> None: ...

def bootstrap(
    data,
    statistic,
    *,
    n_resamples: int = 9999,
    batch: Incomplete | None = None,
    vectorized: Incomplete | None = None,
    paired: bool = False,
    axis: int = 0,
    confidence_level: float = 0.95,
    alternative: str = "two-sided",
    method: str = "BCa",
    bootstrap_result: Incomplete | None = None,
    random_state: Incomplete | None = None,
): ...
@dataclass
class MonteCarloTestResult:
    statistic: float | np.ndarray
    pvalue: float | np.ndarray
    null_distribution: np.ndarray
    def __init__(self, statistic, pvalue, null_distribution) -> None: ...

def monte_carlo_test(
    data,
    rvs,
    statistic,
    *,
    vectorized: Incomplete | None = None,
    n_resamples: int = 9999,
    batch: Incomplete | None = None,
    alternative: str = "two-sided",
    axis: int = 0,
): ...
@dataclass
class PermutationTestResult:
    statistic: float | np.ndarray
    pvalue: float | np.ndarray
    null_distribution: np.ndarray
    def __init__(self, statistic, pvalue, null_distribution) -> None: ...

def permutation_test(
    data,
    statistic,
    *,
    permutation_type: str = "independent",
    vectorized: Incomplete | None = None,
    n_resamples: int = 9999,
    batch: Incomplete | None = None,
    alternative: str = "two-sided",
    axis: int = 0,
    random_state: Incomplete | None = None,
): ...
@dataclass
class ResamplingMethod:
    n_resamples: int = ...
    batch: int = ...
    def __init__(self, n_resamples=..., batch=...) -> None: ...

@dataclass
class MonteCarloMethod(ResamplingMethod):
    rvs: object = ...
    def __init__(self, n_resamples=..., batch=..., rvs=...) -> None: ...

@dataclass
class PermutationMethod(ResamplingMethod):
    random_state: object = ...
    def __init__(self, n_resamples=..., batch=..., random_state=...) -> None: ...

@dataclass
class BootstrapMethod(ResamplingMethod):
    random_state: object = ...
    method: str = ...
    def __init__(
        self, n_resamples=..., batch=..., random_state=..., method=...
    ) -> None: ...
