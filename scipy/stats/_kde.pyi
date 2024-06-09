from _typeshed import Incomplete

__all__ = ['gaussian_kde']

class gaussian_kde:
    dataset: Incomplete
    def __init__(self, dataset, bw_method: Incomplete | None = None, weights: Incomplete | None = None) -> None: ...
    def evaluate(self, points): ...
    __call__ = evaluate
    def integrate_gaussian(self, mean, cov): ...
    def integrate_box_1d(self, low, high): ...
    def integrate_box(self, low_bounds, high_bounds, maxpts: Incomplete | None = None): ...
    def integrate_kde(self, other): ...
    def resample(self, size: Incomplete | None = None, seed: Incomplete | None = None): ...
    def scotts_factor(self): ...
    def silverman_factor(self): ...
    covariance_factor = scotts_factor
    def set_bandwidth(self, bw_method: Incomplete | None = None): ...
    factor: Incomplete
    @property
    def inv_cov(self): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...
    def marginal(self, dimensions): ...
    @property
    def weights(self): ...
    @property
    def neff(self): ...
