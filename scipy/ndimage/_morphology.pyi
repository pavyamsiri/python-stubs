from _typeshed import Incomplete
from collections.abc import Iterable
from typing import overload, Literal
from numpy import float64, int32
from numpy.typing import ArrayLike, NDArray

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
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[False] = ...,
    return_indices: Literal[False] = ...,
    distances: NDArray[float64] | None = ...,
    indices: NDArray[int32] | None = ...,
) -> None: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[False] = ...,
    distances: None = ...,
    indices: NDArray[int32] | None = ...,
) -> NDArray[float64]: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[False] = ...,
    distances: NDArray[float64] = ...,
    indices: NDArray[int32] | None = ...,
) -> None: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[False] = ...,
    return_indices: Literal[True] = ...,
    distances: NDArray[float64] | None = ...,
    indices: None = ...,
) -> NDArray[int32]: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[False] = ...,
    return_indices: Literal[True] = ...,
    distances: NDArray[float64] | None = ...,
    indices: NDArray[int32] = ...,
) -> None: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[True] = ...,
    distances: None = ...,
    indices: None = ...,
) -> tuple[NDArray[float64], NDArray[int32]]: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[True] = ...,
    distances: NDArray[float64] = ...,
    indices: None = ...,
) -> NDArray[int32]: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[True] = ...,
    distances: None = ...,
    indices: NDArray[int32] = ...,
) -> NDArray[float64]: ...
@overload
def distance_transform_edt(
    input: ArrayLike,
    sampling: float | Iterable[float] | None = ...,
    return_distances: Literal[True] = ...,
    return_indices: Literal[True] = ...,
    distances: NDArray[float64] = ...,
    indices: NDArray[int32] = ...,
) -> None: ...
