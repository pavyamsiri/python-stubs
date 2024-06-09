import numpy as np
from _typeshed import Incomplete
from scipy._lib._array_api import array_namespace as array_namespace
from typing import NamedTuple, TypeVar

AxisError: type[Exception]
ComplexWarning: type[Warning]
VisibleDeprecationWarning: type[Warning]
DTypePromotionError = TypeError
np_long: type
np_ulong: type
IntNumber = int | np.integer
DecimalNumber = float | np.floating | np.integer
copy_if_needed: bool | None
SeedType: Incomplete
GeneratorType = TypeVar(
    "GeneratorType", bound=np.random.Generator | np.random.RandomState
)

class Generator: ...

def float_factorial(n: int) -> float: ...
def check_random_state(seed): ...

class FullArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete
    kwonlyargs: Incomplete
    kwonlydefaults: Incomplete
    annotations: Incomplete

def getfullargspec_no_self(func): ...

class _FunctionWrapper:
    f: Incomplete
    args: Incomplete
    def __init__(self, f, args) -> None: ...
    def __call__(self, x): ...

class MapWrapper:
    pool: Incomplete
    def __init__(self, pool: int = 1) -> None: ...
    def __enter__(self): ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def close(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def __call__(self, func, iterable): ...

def rng_integers(
    gen,
    low,
    high: Incomplete | None = None,
    size: Incomplete | None = None,
    dtype: str = "int64",
    endpoint: bool = False,
): ...
def normalize_axis_index(axis, ndim): ...

class _RichResult(dict):
    def __getattr__(self, name): ...
    __setattr__: Incomplete
    __delattr__: Incomplete
    def __dir__(self): ...
