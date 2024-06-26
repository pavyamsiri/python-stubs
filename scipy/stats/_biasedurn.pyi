import _cython_3_0_10
from typing import ClassVar

__reduce_cython__: _cython_3_0_10.cython_function_or_method
__setstate_cython__: _cython_3_0_10.cython_function_or_method
__test__: dict

class _PyFishersNCHypergeometric:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def mean(self, *args, **kwargs): ...
    def mode(self, *args, **kwargs): ...
    def moments(self, *args, **kwargs): ...
    def probability(self, *args, **kwargs): ...
    def variance(self, *args, **kwargs): ...
    def __reduce__(self): ...

class _PyStochasticLib3:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def FishersNCHyp(self, *args, **kwargs): ...
    def Random(self, *args, **kwargs): ...
    def SetAccuracy(self, *args, **kwargs): ...
    def WalleniusNCHyp(self, *args, **kwargs): ...
    def rvs_fisher(self, *args, **kwargs): ...
    def rvs_wallenius(self, *args, **kwargs): ...
    def __reduce__(self): ...

class _PyWalleniusNCHypergeometric:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def mean(self, *args, **kwargs): ...
    def mode(self, *args, **kwargs): ...
    def moments(self, *args, **kwargs): ...
    def probability(self, *args, **kwargs): ...
    def variance(self, *args, **kwargs): ...
    def __reduce__(self): ...
