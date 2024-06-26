from _typeshed import Incomplete

__all__ = [
    "correlate1d",
    "convolve1d",
    "gaussian_filter1d",
    "gaussian_filter",
    "prewitt",
    "sobel",
    "generic_laplace",
    "laplace",
    "gaussian_laplace",
    "generic_gradient_magnitude",
    "gaussian_gradient_magnitude",
    "correlate",
    "convolve",
    "uniform_filter1d",
    "uniform_filter",
    "minimum_filter1d",
    "maximum_filter1d",
    "minimum_filter",
    "maximum_filter",
    "rank_filter",
    "median_filter",
    "percentile_filter",
    "generic_filter1d",
    "generic_filter",
]

def correlate1d(
    input,
    weights,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def convolve1d(
    input,
    weights,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def gaussian_filter1d(
    input,
    sigma,
    axis: int = -1,
    order: int = 0,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    truncate: float = 4.0,
    *,
    radius: Incomplete | None = None,
): ...
def gaussian_filter(
    input,
    sigma,
    order: int = 0,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    truncate: float = 4.0,
    *,
    radius: Incomplete | None = None,
    axes: Incomplete | None = None,
): ...
def prewitt(
    input,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
): ...
def sobel(
    input,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
): ...
def generic_laplace(
    input,
    derivative2,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    extra_arguments=(),
    extra_keywords: Incomplete | None = None,
): ...
def laplace(
    input, output: Incomplete | None = None, mode: str = "reflect", cval: float = 0.0
): ...
def gaussian_laplace(
    input,
    sigma,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    **kwargs,
): ...
def generic_gradient_magnitude(
    input,
    derivative,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    extra_arguments=(),
    extra_keywords: Incomplete | None = None,
): ...
def gaussian_gradient_magnitude(
    input,
    sigma,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    **kwargs,
): ...
def correlate(
    input,
    weights,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def convolve(
    input,
    weights,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def uniform_filter1d(
    input,
    size,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def uniform_filter(
    input,
    size: int = 3,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def minimum_filter1d(
    input,
    size,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def maximum_filter1d(
    input,
    size,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def minimum_filter(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def maximum_filter(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def rank_filter(
    input,
    rank,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def median_filter(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def percentile_filter(
    input,
    percentile,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    *,
    axes: Incomplete | None = None,
): ...
def generic_filter1d(
    input,
    function,
    filter_size,
    axis: int = -1,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    extra_arguments=(),
    extra_keywords: Incomplete | None = None,
): ...
def generic_filter(
    input,
    function,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
    extra_arguments=(),
    extra_keywords: Incomplete | None = None,
): ...
