from _typeshed import Incomplete

__all__ = ['broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden', 'excitingmixing', 'newton_krylov', 'BroydenFirst', 'KrylovJacobian', 'InverseJacobian', 'NoConvergence']

class NoConvergence(Exception): ...

class TerminationCondition:
    x_tol: Incomplete
    x_rtol: Incomplete
    f_tol: Incomplete
    f_rtol: Incomplete
    norm: Incomplete
    iter: Incomplete
    f0_norm: Incomplete
    iteration: int
    def __init__(self, f_tol: Incomplete | None = None, f_rtol: Incomplete | None = None, x_tol: Incomplete | None = None, x_rtol: Incomplete | None = None, iter: Incomplete | None = None, norm=...) -> None: ...
    def check(self, f, x, dx): ...

class Jacobian:
    def __init__(self, **kw) -> None: ...
    def aspreconditioner(self): ...
    def solve(self, v, tol: int = 0) -> None: ...
    def update(self, x, F) -> None: ...
    func: Incomplete
    shape: Incomplete
    dtype: Incomplete
    def setup(self, x, F, func) -> None: ...

class InverseJacobian:
    jacobian: Incomplete
    matvec: Incomplete
    update: Incomplete
    setup: Incomplete
    rmatvec: Incomplete
    def __init__(self, jacobian) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...

class GenericBroyden(Jacobian):
    last_f: Incomplete
    last_x: Incomplete
    alpha: Incomplete
    def setup(self, x0, f0, func) -> None: ...
    def update(self, x, f) -> None: ...

class LowRankMatrix:
    alpha: Incomplete
    cs: Incomplete
    ds: Incomplete
    n: Incomplete
    dtype: Incomplete
    collapsed: Incomplete
    def __init__(self, alpha, n, dtype) -> None: ...
    def matvec(self, v): ...
    def rmatvec(self, v): ...
    def solve(self, v, tol: int = 0): ...
    def rsolve(self, v, tol: int = 0): ...
    def append(self, c, d) -> None: ...
    def __array__(self, dtype: Incomplete | None = None, copy: Incomplete | None = None): ...
    def collapse(self) -> None: ...
    def restart_reduce(self, rank) -> None: ...
    def simple_reduce(self, rank) -> None: ...
    def svd_reduce(self, max_rank, to_retain: Incomplete | None = None) -> None: ...

class BroydenFirst(GenericBroyden):
    alpha: Incomplete
    Gm: Incomplete
    max_rank: Incomplete
    def __init__(self, alpha: Incomplete | None = None, reduction_method: str = 'restart', max_rank: Incomplete | None = None) -> None: ...
    def setup(self, x, F, func) -> None: ...
    def todense(self): ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...

class BroydenSecond(BroydenFirst): ...

class Anderson(GenericBroyden):
    alpha: Incomplete
    M: Incomplete
    dx: Incomplete
    df: Incomplete
    gamma: Incomplete
    w0: Incomplete
    def __init__(self, alpha: Incomplete | None = None, w0: float = 0.01, M: int = 5) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...

class DiagBroyden(GenericBroyden):
    alpha: Incomplete
    def __init__(self, alpha: Incomplete | None = None) -> None: ...
    d: Incomplete
    def setup(self, x, F, func) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class LinearMixing(GenericBroyden):
    alpha: Incomplete
    def __init__(self, alpha: Incomplete | None = None) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class ExcitingMixing(GenericBroyden):
    alpha: Incomplete
    alphamax: Incomplete
    beta: Incomplete
    def __init__(self, alpha: Incomplete | None = None, alphamax: float = 1.0) -> None: ...
    def setup(self, x, F, func) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class KrylovJacobian(Jacobian):
    preconditioner: Incomplete
    rdiff: Incomplete
    method: Incomplete
    method_kw: Incomplete
    def __init__(self, rdiff: Incomplete | None = None, method: str = 'lgmres', inner_maxiter: int = 20, inner_M: Incomplete | None = None, outer_k: int = 10, **kw) -> None: ...
    def matvec(self, v): ...
    def solve(self, rhs, tol: int = 0): ...
    x0: Incomplete
    f0: Incomplete
    def update(self, x, f) -> None: ...
    op: Incomplete
    def setup(self, x, f, func) -> None: ...

broyden1: Incomplete
broyden2: Incomplete
anderson: Incomplete
linearmixing: Incomplete
diagbroyden: Incomplete
excitingmixing: Incomplete
newton_krylov: Incomplete