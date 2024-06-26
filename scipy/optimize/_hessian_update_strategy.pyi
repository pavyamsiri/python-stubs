from _typeshed import Incomplete

__all__ = ["HessianUpdateStrategy", "BFGS", "SR1"]

class HessianUpdateStrategy:
    def initialize(self, n, approx_type) -> None: ...
    def update(self, delta_x, delta_grad) -> None: ...
    def dot(self, p) -> None: ...
    def get_matrix(self) -> None: ...

class FullHessianUpdateStrategy(HessianUpdateStrategy):
    init_scale: Incomplete
    first_iteration: Incomplete
    approx_type: Incomplete
    B: Incomplete
    H: Incomplete
    def __init__(self, init_scale: str = "auto") -> None: ...
    n: Incomplete
    def initialize(self, n, approx_type) -> None: ...
    def update(self, delta_x, delta_grad) -> None: ...
    def dot(self, p): ...
    def get_matrix(self): ...

class BFGS(FullHessianUpdateStrategy):
    min_curvature: Incomplete
    exception_strategy: Incomplete
    def __init__(
        self,
        exception_strategy: str = "skip_update",
        min_curvature: Incomplete | None = None,
        init_scale: str = "auto",
    ) -> None: ...

class SR1(FullHessianUpdateStrategy):
    min_denominator: Incomplete
    def __init__(
        self, min_denominator: float = 1e-08, init_scale: str = "auto"
    ) -> None: ...
