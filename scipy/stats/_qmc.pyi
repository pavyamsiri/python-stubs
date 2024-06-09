import abc
import numpy as np
import numpy.typing as npt
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from scipy._lib._util import DecimalNumber, IntNumber, SeedType
from typing import ClassVar, Literal, overload

__all__ = [
    "scale",
    "discrepancy",
    "geometric_discrepancy",
    "update_discrepancy",
    "QMCEngine",
    "Sobol",
    "Halton",
    "LatinHypercube",
    "PoissonDisk",
    "MultinomialQMC",
    "MultivariateNormalQMC",
]

def scale(
    sample: npt.ArrayLike,
    l_bounds: npt.ArrayLike,
    u_bounds: npt.ArrayLike,
    *,
    reverse: bool = False,
) -> np.ndarray: ...
def discrepancy(
    sample: npt.ArrayLike,
    *,
    iterative: bool = False,
    method: Literal["CD", "WD", "MD", "L2-star"] = "CD",
    workers: IntNumber = 1,
) -> float: ...
def geometric_discrepancy(
    sample: npt.ArrayLike,
    method: Literal["mindist", "mst"] = "mindist",
    metric: str = "euclidean",
) -> float: ...
def update_discrepancy(
    x_new: npt.ArrayLike, sample: npt.ArrayLike, initial_disc: DecimalNumber
) -> float: ...

class QMCEngine(ABC, metaclass=abc.ABCMeta):
    d: Incomplete
    rng: Incomplete
    rng_seed: Incomplete
    num_generated: int
    optimization_method: Incomplete
    @abstractmethod
    def __init__(
        self,
        d: IntNumber,
        *,
        optimization: Literal["random-cd", "lloyd"] | None = None,
        seed: SeedType = None,
    ): ...
    def random(self, n: IntNumber = 1, *, workers: IntNumber = 1) -> np.ndarray: ...
    def integers(
        self,
        l_bounds: npt.ArrayLike,
        *,
        u_bounds: npt.ArrayLike | None = None,
        n: IntNumber = 1,
        endpoint: bool = False,
        workers: IntNumber = 1,
    ) -> np.ndarray: ...
    def reset(self) -> QMCEngine: ...
    def fast_forward(self, n: IntNumber) -> QMCEngine: ...

class Halton(QMCEngine):
    seed: Incomplete
    base: Incomplete
    scramble: Incomplete
    def __init__(
        self,
        d: IntNumber,
        *,
        scramble: bool = True,
        optimization: Literal["random-cd", "lloyd"] | None = None,
        seed: SeedType = None,
    ) -> None: ...

class LatinHypercube(QMCEngine):
    scramble: Incomplete
    lhs_method: Incomplete
    def __init__(
        self,
        d: IntNumber,
        *,
        scramble: bool = True,
        strength: int = 1,
        optimization: Literal["random-cd", "lloyd"] | None = None,
        seed: SeedType = None,
    ) -> None: ...

class Sobol(QMCEngine):
    MAXDIM: ClassVar[int]
    bits: Incomplete
    dtype_i: Incomplete
    maxn: Incomplete
    def __init__(
        self,
        d: IntNumber,
        *,
        scramble: bool = True,
        bits: IntNumber | None = None,
        seed: SeedType = None,
        optimization: Literal["random-cd", "lloyd"] | None = None,
    ) -> None: ...
    def random_base2(self, m: IntNumber) -> np.ndarray: ...
    def reset(self) -> Sobol: ...
    def fast_forward(self, n: IntNumber) -> Sobol: ...

class PoissonDisk(QMCEngine):
    hypersphere_method: Incomplete
    radius_factor: Incomplete
    radius: Incomplete
    radius_squared: Incomplete
    ncandidates: Incomplete
    cell_size: Incomplete
    grid_size: Incomplete
    def __init__(
        self,
        d: IntNumber,
        *,
        radius: DecimalNumber = 0.05,
        hypersphere: Literal["volume", "surface"] = "volume",
        ncandidates: IntNumber = 30,
        optimization: Literal["random-cd", "lloyd"] | None = None,
        seed: SeedType = None,
    ) -> None: ...
    def fill_space(self) -> np.ndarray: ...
    def reset(self) -> PoissonDisk: ...

class MultivariateNormalQMC:
    engine: Incomplete
    def __init__(
        self,
        mean: npt.ArrayLike,
        cov: npt.ArrayLike | None = None,
        *,
        cov_root: npt.ArrayLike | None = None,
        inv_transform: bool = True,
        engine: QMCEngine | None = None,
        seed: SeedType = None,
    ) -> None: ...
    def random(self, n: IntNumber = 1) -> np.ndarray: ...

class MultinomialQMC:
    pvals: Incomplete
    n_trials: Incomplete
    engine: Incomplete
    def __init__(
        self,
        pvals: npt.ArrayLike,
        n_trials: IntNumber,
        *,
        engine: QMCEngine | None = None,
        seed: SeedType = None,
    ) -> None: ...
    def random(self, n: IntNumber = 1) -> np.ndarray: ...
