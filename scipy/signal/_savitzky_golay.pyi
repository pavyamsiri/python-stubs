from ._arraytools import axis_slice as axis_slice
from _typeshed import Incomplete
from scipy._lib._util import float_factorial as float_factorial
from scipy.linalg import lstsq as lstsq
from scipy.ndimage import convolve1d as convolve1d

def savgol_coeffs(window_length, polyorder, deriv: int = 0, delta: float = 1.0, pos: Incomplete | None = None, use: str = 'conv'): ...
def savgol_filter(x, window_length, polyorder, deriv: int = 0, delta: float = 1.0, axis: int = -1, mode: str = 'interp', cval: float = 0.0): ...
