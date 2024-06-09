from ._linesearch import line_search_wolfe2 as line_search
from _typeshed import Incomplete
from scipy._lib._util import _RichResult

__all__ = [
    "fmin",
    "fmin_powell",
    "fmin_bfgs",
    "fmin_ncg",
    "fmin_cg",
    "fminbound",
    "brent",
    "golden",
    "bracket",
    "rosen",
    "rosen_der",
    "rosen_hess",
    "rosen_hess_prod",
    "brute",
    "approx_fprime",
    "line_search",
    "check_grad",
    "OptimizeResult",
    "show_options",
    "OptimizeWarning",
]

class MemoizeJac:
    fun: Incomplete
    jac: Incomplete
    x: Incomplete
    def __init__(self, fun) -> None: ...
    def __call__(self, x, *args): ...
    def derivative(self, x, *args): ...

class OptimizeResult(_RichResult): ...
class OptimizeWarning(UserWarning): ...

def rosen(x): ...
def rosen_der(x): ...
def rosen_hess(x): ...
def rosen_hess_prod(x, p): ...

class _MaxFuncCallError(RuntimeError): ...

def fmin(
    func,
    x0,
    args=(),
    xtol: float = 0.0001,
    ftol: float = 0.0001,
    maxiter: Incomplete | None = None,
    maxfun: Incomplete | None = None,
    full_output: int = 0,
    disp: int = 1,
    retall: int = 0,
    callback: Incomplete | None = None,
    initial_simplex: Incomplete | None = None,
): ...
def approx_fprime(xk, f, epsilon=..., *args): ...
def check_grad(
    func,
    grad,
    x0,
    *args,
    epsilon=...,
    direction: str = "all",
    seed: Incomplete | None = None,
): ...

class _LineSearchError(RuntimeError): ...

def fmin_bfgs(
    f,
    x0,
    fprime: Incomplete | None = None,
    args=(),
    gtol: float = 1e-05,
    norm=...,
    epsilon=...,
    maxiter: Incomplete | None = None,
    full_output: int = 0,
    disp: int = 1,
    retall: int = 0,
    callback: Incomplete | None = None,
    xrtol: int = 0,
    c1: float = 0.0001,
    c2: float = 0.9,
    hess_inv0: Incomplete | None = None,
): ...
def fmin_cg(
    f,
    x0,
    fprime: Incomplete | None = None,
    args=(),
    gtol: float = 1e-05,
    norm=...,
    epsilon=...,
    maxiter: Incomplete | None = None,
    full_output: int = 0,
    disp: int = 1,
    retall: int = 0,
    callback: Incomplete | None = None,
    c1: float = 0.0001,
    c2: float = 0.4,
): ...
def fmin_ncg(
    f,
    x0,
    fprime,
    fhess_p: Incomplete | None = None,
    fhess: Incomplete | None = None,
    args=(),
    avextol: float = 1e-05,
    epsilon=...,
    maxiter: Incomplete | None = None,
    full_output: int = 0,
    disp: int = 1,
    retall: int = 0,
    callback: Incomplete | None = None,
    c1: float = 0.0001,
    c2: float = 0.9,
): ...
def fminbound(
    func,
    x1,
    x2,
    args=(),
    xtol: float = 1e-05,
    maxfun: int = 500,
    full_output: int = 0,
    disp: int = 1,
): ...

class Brent:
    func: Incomplete
    args: Incomplete
    tol: Incomplete
    maxiter: Incomplete
    xmin: Incomplete
    fval: Incomplete
    iter: int
    funcalls: int
    disp: Incomplete
    def __init__(
        self,
        func,
        args=(),
        tol: float = 1.48e-08,
        maxiter: int = 500,
        full_output: int = 0,
        disp: int = 0,
    ) -> None: ...
    brack: Incomplete
    def set_bracket(self, brack: Incomplete | None = None) -> None: ...
    def get_bracket_info(self): ...
    def optimize(self) -> None: ...
    def get_result(self, full_output: bool = False): ...

def brent(
    func,
    args=(),
    brack: Incomplete | None = None,
    tol: float = 1.48e-08,
    full_output: int = 0,
    maxiter: int = 500,
): ...
def golden(
    func,
    args=(),
    brack: Incomplete | None = None,
    tol=...,
    full_output: int = 0,
    maxiter: int = 5000,
): ...
def bracket(
    func,
    xa: float = 0.0,
    xb: float = 1.0,
    args=(),
    grow_limit: float = 110.0,
    maxiter: int = 1000,
): ...

class BracketError(RuntimeError): ...

def fmin_powell(
    func,
    x0,
    args=(),
    xtol: float = 0.0001,
    ftol: float = 0.0001,
    maxiter: Incomplete | None = None,
    maxfun: Incomplete | None = None,
    full_output: int = 0,
    disp: int = 1,
    retall: int = 0,
    callback: Incomplete | None = None,
    direc: Incomplete | None = None,
): ...
def brute(
    func,
    ranges,
    args=(),
    Ns: int = 20,
    full_output: int = 0,
    finish=...,
    disp: bool = False,
    workers: int = 1,
): ...

class _Brute_Wrapper:
    f: Incomplete
    args: Incomplete
    def __init__(self, f, args) -> None: ...
    def __call__(self, x): ...

def show_options(
    solver: Incomplete | None = None,
    method: Incomplete | None = None,
    disp: bool = True,
): ...
