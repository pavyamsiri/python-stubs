from _typeshed import Incomplete

__all__ = [
    "iterate_structure",
    "generate_binary_structure",
    "binary_erosion",
    "binary_dilation",
    "binary_opening",
    "binary_closing",
    "binary_hit_or_miss",
    "binary_propagation",
    "binary_fill_holes",
    "grey_erosion",
    "grey_dilation",
    "grey_opening",
    "grey_closing",
    "morphological_gradient",
    "morphological_laplace",
    "white_tophat",
    "black_tophat",
    "distance_transform_bf",
    "distance_transform_cdt",
    "distance_transform_edt",
]

def iterate_structure(structure, iterations, origin: Incomplete | None = None): ...
def generate_binary_structure(rank, connectivity): ...
def binary_erosion(
    input,
    structure: Incomplete | None = None,
    iterations: int = 1,
    mask: Incomplete | None = None,
    output: Incomplete | None = None,
    border_value: int = 0,
    origin: int = 0,
    brute_force: bool = False,
): ...
def binary_dilation(
    input,
    structure: Incomplete | None = None,
    iterations: int = 1,
    mask: Incomplete | None = None,
    output: Incomplete | None = None,
    border_value: int = 0,
    origin: int = 0,
    brute_force: bool = False,
): ...
def binary_opening(
    input,
    structure: Incomplete | None = None,
    iterations: int = 1,
    output: Incomplete | None = None,
    origin: int = 0,
    mask: Incomplete | None = None,
    border_value: int = 0,
    brute_force: bool = False,
): ...
def binary_closing(
    input,
    structure: Incomplete | None = None,
    iterations: int = 1,
    output: Incomplete | None = None,
    origin: int = 0,
    mask: Incomplete | None = None,
    border_value: int = 0,
    brute_force: bool = False,
): ...
def binary_hit_or_miss(
    input,
    structure1: Incomplete | None = None,
    structure2: Incomplete | None = None,
    output: Incomplete | None = None,
    origin1: int = 0,
    origin2: Incomplete | None = None,
): ...
def binary_propagation(
    input,
    structure: Incomplete | None = None,
    mask: Incomplete | None = None,
    output: Incomplete | None = None,
    border_value: int = 0,
    origin: int = 0,
): ...
def binary_fill_holes(
    input,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    origin: int = 0,
): ...
def grey_erosion(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def grey_dilation(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def grey_opening(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def grey_closing(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def morphological_gradient(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def morphological_laplace(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def white_tophat(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def black_tophat(
    input,
    size: Incomplete | None = None,
    footprint: Incomplete | None = None,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
    mode: str = "reflect",
    cval: float = 0.0,
    origin: int = 0,
): ...
def distance_transform_bf(
    input,
    metric: str = "euclidean",
    sampling: Incomplete | None = None,
    return_distances: bool = True,
    return_indices: bool = False,
    distances: Incomplete | None = None,
    indices: Incomplete | None = None,
): ...
def distance_transform_cdt(
    input,
    metric: str = "chessboard",
    return_distances: bool = True,
    return_indices: bool = False,
    distances: Incomplete | None = None,
    indices: Incomplete | None = None,
): ...
def distance_transform_edt(
    input,
    sampling: Incomplete | None = None,
    return_distances: bool = True,
    return_indices: bool = False,
    distances: Incomplete | None = None,
    indices: Incomplete | None = None,
): ...
