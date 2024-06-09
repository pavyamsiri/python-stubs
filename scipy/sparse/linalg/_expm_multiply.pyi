from _typeshed import Incomplete

__all__ = ["expm_multiply"]

def expm_multiply(
    A,
    B,
    start: Incomplete | None = None,
    stop: Incomplete | None = None,
    num: Incomplete | None = None,
    endpoint: Incomplete | None = None,
    traceA: Incomplete | None = None,
): ...

class LazyOperatorNormInfo:
    def __init__(
        self, A, A_1_norm: Incomplete | None = None, ell: int = 2, scale: int = 1
    ) -> None: ...
    def set_scale(self, scale) -> None: ...
    def onenorm(self): ...
    def d(self, p): ...
    def alpha(self, p): ...
