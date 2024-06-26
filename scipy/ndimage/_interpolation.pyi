from _typeshed import Incomplete

__all__ = [
    "spline_filter1d",
    "spline_filter",
    "geometric_transform",
    "map_coordinates",
    "affine_transform",
    "shift",
    "zoom",
    "rotate",
]

def spline_filter1d(
    input, order: int = 3, axis: int = -1, output=..., mode: str = "mirror"
): ...
def spline_filter(input, order: int = 3, output=..., mode: str = "mirror"): ...
def geometric_transform(
    input,
    mapping,
    output_shape: Incomplete | None = None,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
    extra_arguments=(),
    extra_keywords={},
): ...
def map_coordinates(
    input,
    coordinates,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
): ...
def affine_transform(
    input,
    matrix,
    offset: float = 0.0,
    output_shape: Incomplete | None = None,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
): ...
def shift(
    input,
    shift,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
): ...
def zoom(
    input,
    zoom,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
    *,
    grid_mode: bool = False,
): ...
def rotate(
    input,
    angle,
    axes=(1, 0),
    reshape: bool = True,
    output: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    prefilter: bool = True,
): ...
