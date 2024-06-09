from _typeshed import Incomplete

__all__ = ["root_scalar"]

class MemoizeDer:
    fun: Incomplete
    vals: Incomplete
    x: Incomplete
    n_calls: int
    def __init__(self, fun) -> None: ...
    def __call__(self, x, *args): ...
    def fprime(self, x, *args): ...
    def fprime2(self, x, *args): ...
    def ncalls(self): ...

def root_scalar(
    f,
    args=(),
    method: Incomplete | None = None,
    bracket: Incomplete | None = None,
    fprime: Incomplete | None = None,
    fprime2: Incomplete | None = None,
    x0: Incomplete | None = None,
    x1: Incomplete | None = None,
    xtol: Incomplete | None = None,
    rtol: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    options: Incomplete | None = None,
): ...
