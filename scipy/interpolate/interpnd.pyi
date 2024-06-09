import _cython_3_0_10
import scipy.spatial._qhull as qhull
from typing import Any

__test__: dict
estimate_gradients_2d_global: _cython_3_0_10.cython_function_or_method

class CloughTocher2DInterpolator(NDInterpolatorBase):
    def __init__(self, points, values, tol=...) -> Any: ...

class GradientEstimationWarning(Warning): ...

class LinearNDInterpolator(NDInterpolatorBase):
    def __init__(self, points, values, fill_value=..., rescale=...) -> Any: ...

class NDInterpolatorBase:
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, *args, **kwargs): ...
