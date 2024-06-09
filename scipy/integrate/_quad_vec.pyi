import collections
from _typeshed import Incomplete
from scipy._lib._util import MapWrapper as MapWrapper

class LRUDict(collections.OrderedDict):
    def __init__(self, max_size) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def update(self, other) -> None: ...

class SemiInfiniteFunc:
    def __init__(self, func, start, infty) -> None: ...
    def get_t(self, x): ...
    def __call__(self, t): ...

class DoubleInfiniteFunc:
    def __init__(self, func) -> None: ...
    def get_t(self, x): ...
    def __call__(self, t): ...

class _Bunch:
    def __init__(self, **kwargs) -> None: ...

def quad_vec(
    f,
    a,
    b,
    epsabs: float = 1e-200,
    epsrel: float = 1e-08,
    norm: str = "2",
    cache_size: float = 100000000.0,
    limit: int = 10000,
    workers: int = 1,
    points: Incomplete | None = None,
    quadrature: Incomplete | None = None,
    full_output: bool = False,
    *,
    args=(),
): ...
