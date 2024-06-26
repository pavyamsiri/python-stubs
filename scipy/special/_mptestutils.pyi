from _typeshed import Incomplete
from scipy.special._testutils import assert_func_equal as assert_func_equal

class Arg:
    def __init__(
        self, a=..., b=..., inclusive_a: bool = True, inclusive_b: bool = True
    ) -> None: ...
    def values(self, n): ...

class FixedArg:
    def __init__(self, values) -> None: ...
    def values(self, n): ...

class ComplexArg:
    real: Incomplete
    imag: Incomplete
    def __init__(self, a=..., b=...) -> None: ...
    def values(self, n): ...

class IntArg:
    a: Incomplete
    b: Incomplete
    def __init__(self, a: int = -1000, b: int = 1000) -> None: ...
    def values(self, n): ...

def get_args(argspec, n): ...

class MpmathData:
    scipy_func: Incomplete
    mpmath_func: Incomplete
    arg_spec: Incomplete
    dps: Incomplete
    prec: Incomplete
    n: Incomplete
    rtol: Incomplete
    atol: Incomplete
    ignore_inf_sign: Incomplete
    nan_ok: Incomplete
    is_complex: Incomplete
    distinguish_nan_and_inf: Incomplete
    name: Incomplete
    param_filter: Incomplete
    def __init__(
        self,
        scipy_func,
        mpmath_func,
        arg_spec,
        name: Incomplete | None = None,
        dps: Incomplete | None = None,
        prec: Incomplete | None = None,
        n: Incomplete | None = None,
        rtol: float = 1e-07,
        atol: float = 1e-300,
        ignore_inf_sign: bool = False,
        distinguish_nan_and_inf: bool = True,
        nan_ok: bool = True,
        param_filter: Incomplete | None = None,
    ) -> None: ...
    def check(self): ...

def assert_mpmath_equal(*a, **kw) -> None: ...
def nonfunctional_tooslow(func): ...
def mpf2float(x): ...
def mpc2complex(x): ...
def trace_args(func): ...

POSIX: Incomplete

class TimeoutError(Exception): ...

def time_limited(timeout: float = 0.5, return_val=..., use_sigalrm: bool = True): ...
def exception_to_nan(func): ...
def inf_to_nan(func): ...
def mp_assert_allclose(res, std, atol: int = 0, rtol: float = 1e-17) -> None: ...
