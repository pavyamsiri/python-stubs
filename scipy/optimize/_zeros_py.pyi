from ._optimize import OptimizeResult
from _typeshed import Incomplete

__all__ = ["newton", "bisect", "ridder", "brentq", "brenth", "toms748", "RootResults"]

class RootResults(OptimizeResult):
    root: Incomplete
    iterations: Incomplete
    function_calls: Incomplete
    converged: Incomplete
    flag: Incomplete
    method: Incomplete
    def __init__(self, root, iterations, function_calls, flag, method) -> None: ...

def newton(
    func,
    x0,
    fprime: Incomplete | None = None,
    args=(),
    tol: float = 1.48e-08,
    maxiter: int = 50,
    fprime2: Incomplete | None = None,
    x1: Incomplete | None = None,
    rtol: float = 0.0,
    full_output: bool = False,
    disp: bool = True,
): ...
def bisect(
    f,
    a,
    b,
    args=(),
    xtol=...,
    rtol=...,
    maxiter=...,
    full_output: bool = False,
    disp: bool = True,
): ...
def ridder(
    f,
    a,
    b,
    args=(),
    xtol=...,
    rtol=...,
    maxiter=...,
    full_output: bool = False,
    disp: bool = True,
): ...
def brentq(
    f,
    a,
    b,
    args=(),
    xtol=...,
    rtol=...,
    maxiter=...,
    full_output: bool = False,
    disp: bool = True,
): ...
def brenth(
    f,
    a,
    b,
    args=(),
    xtol=...,
    rtol=...,
    maxiter=...,
    full_output: bool = False,
    disp: bool = True,
): ...

class TOMS748Solver:
    f: Incomplete
    args: Incomplete
    function_calls: int
    iterations: int
    k: int
    ab: Incomplete
    fab: Incomplete
    d: Incomplete
    fd: Incomplete
    e: Incomplete
    fe: Incomplete
    disp: bool
    xtol: Incomplete
    rtol: Incomplete
    maxiter: Incomplete
    def __init__(self) -> None: ...
    def configure(self, xtol, rtol, maxiter, disp, k) -> None: ...
    def get_result(self, x, flag=...): ...
    def start(self, f, a, b, args=()): ...
    def get_status(self): ...
    def iterate(self): ...
    def solve(
        self,
        f,
        a,
        b,
        args=(),
        xtol=...,
        rtol=...,
        k: int = 2,
        maxiter=...,
        disp: bool = True,
    ): ...

def toms748(
    f,
    a,
    b,
    args=(),
    k: int = 1,
    xtol=...,
    rtol=...,
    maxiter=...,
    full_output: bool = False,
    disp: bool = True,
): ...
