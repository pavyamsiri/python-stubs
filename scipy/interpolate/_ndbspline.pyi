from _typeshed import Incomplete

__all__ = ["NdBSpline"]

class NdBSpline:
    k: Incomplete
    t: Incomplete
    c: Incomplete
    extrapolate: Incomplete
    def __init__(self, t, c, k, *, extrapolate: Incomplete | None = None) -> None: ...
    def __call__(
        self, xi, *, nu: Incomplete | None = None, extrapolate: Incomplete | None = None
    ): ...
    @classmethod
    def design_matrix(cls, xvals, t, k, extrapolate: bool = True): ...
