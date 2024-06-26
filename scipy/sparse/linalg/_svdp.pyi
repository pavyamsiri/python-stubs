from _typeshed import Incomplete

__all__ = ["_svdp"]

class _AProd:
    A: Incomplete
    def __init__(self, A) -> None: ...
    def __call__(self, transa, m, n, x, y, sparm, iparm) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...

def _svdp(
    A,
    k,
    which: str = "LM",
    irl_mode: bool = True,
    kmax: Incomplete | None = None,
    compute_u: bool = True,
    compute_v: bool = True,
    v0: Incomplete | None = None,
    full_output: bool = False,
    tol: int = 0,
    delta: Incomplete | None = None,
    eta: Incomplete | None = None,
    anorm: int = 0,
    cgs: bool = False,
    elr: bool = True,
    min_relgap: float = 0.002,
    shifts: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    random_state: Incomplete | None = None,
): ...
