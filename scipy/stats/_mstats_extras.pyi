from _typeshed import Incomplete

__all__ = [
    "compare_medians_ms",
    "hdquantiles",
    "hdmedian",
    "hdquantiles_sd",
    "idealfourths",
    "median_cihs",
    "mjci",
    "mquantiles_cimj",
    "rsh",
    "trimmed_mean_ci",
]

def hdquantiles(data, prob=..., axis: Incomplete | None = None, var: bool = False): ...
def hdmedian(data, axis: int = -1, var: bool = False): ...
def hdquantiles_sd(data, prob=..., axis: Incomplete | None = None): ...
def trimmed_mean_ci(
    data,
    limits=(0.2, 0.2),
    inclusive=(True, True),
    alpha: float = 0.05,
    axis: Incomplete | None = None,
): ...
def mjci(data, prob=[0.25, 0.5, 0.75], axis: Incomplete | None = None): ...
def mquantiles_cimj(
    data, prob=[0.25, 0.5, 0.75], alpha: float = 0.05, axis: Incomplete | None = None
): ...
def median_cihs(data, alpha: float = 0.05, axis: Incomplete | None = None): ...
def compare_medians_ms(group_1, group_2, axis: Incomplete | None = None): ...
def idealfourths(data, axis: Incomplete | None = None): ...
def rsh(data, points: Incomplete | None = None): ...
