from _typeshed import Incomplete

__all__ = ["RBFInterpolator"]

class RBFInterpolator:
    y: Incomplete
    d: Incomplete
    d_shape: Incomplete
    d_dtype: Incomplete
    neighbors: Incomplete
    smoothing: Incomplete
    kernel: Incomplete
    epsilon: Incomplete
    powers: Incomplete
    def __init__(
        self,
        y,
        d,
        neighbors: Incomplete | None = None,
        smoothing: float = 0.0,
        kernel: str = "thin_plate_spline",
        epsilon: Incomplete | None = None,
        degree: Incomplete | None = None,
    ) -> None: ...
    def __call__(self, x): ...
