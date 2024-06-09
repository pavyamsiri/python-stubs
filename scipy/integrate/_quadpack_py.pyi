from _typeshed import Incomplete

__all__ = ["quad", "dblquad", "tplquad", "nquad", "IntegrationWarning"]

class IntegrationWarning(UserWarning): ...

def quad(
    func,
    a,
    b,
    args=(),
    full_output: int = 0,
    epsabs: float = 1.49e-08,
    epsrel: float = 1.49e-08,
    limit: int = 50,
    points: Incomplete | None = None,
    weight: Incomplete | None = None,
    wvar: Incomplete | None = None,
    wopts: Incomplete | None = None,
    maxp1: int = 50,
    limlst: int = 50,
    complex_func: bool = False,
): ...
def dblquad(
    func, a, b, gfun, hfun, args=(), epsabs: float = 1.49e-08, epsrel: float = 1.49e-08
): ...
def tplquad(
    func,
    a,
    b,
    gfun,
    hfun,
    qfun,
    rfun,
    args=(),
    epsabs: float = 1.49e-08,
    epsrel: float = 1.49e-08,
): ...
def nquad(
    func,
    ranges,
    args: Incomplete | None = None,
    opts: Incomplete | None = None,
    full_output: bool = False,
): ...

class _RangeFunc:
    range_: Incomplete
    def __init__(self, range_) -> None: ...
    def __call__(self, *args): ...

class _OptFunc:
    opt: Incomplete
    def __init__(self, opt) -> None: ...
    def __call__(self, *args): ...

class _NQuad:
    abserr: int
    func: Incomplete
    ranges: Incomplete
    opts: Incomplete
    maxdepth: Incomplete
    full_output: Incomplete
    out_dict: Incomplete
    def __init__(self, func, ranges, opts, full_output) -> None: ...
    def integrate(self, *args, **kwargs): ...
