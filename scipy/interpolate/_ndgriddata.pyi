from .interpnd import (
    CloughTocher2DInterpolator as CloughTocher2DInterpolator,
    LinearNDInterpolator as LinearNDInterpolator,
    NDInterpolatorBase,
)
from _typeshed import Incomplete

__all__ = [
    "griddata",
    "NearestNDInterpolator",
    "LinearNDInterpolator",
    "CloughTocher2DInterpolator",
]

class NearestNDInterpolator(NDInterpolatorBase):
    tree: Incomplete
    values: Incomplete
    def __init__(
        self, x, y, rescale: bool = False, tree_options: Incomplete | None = None
    ) -> None: ...
    def __call__(self, *args, **query_options): ...

def griddata(
    points, values, xi, method: str = "linear", fill_value=..., rescale: bool = False
): ...
