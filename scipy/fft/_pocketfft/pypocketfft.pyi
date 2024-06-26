import numpy

def c2c(
    a: numpy.ndarray,
    axes: object = ...,
    forward: bool = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
def c2r(
    a: numpy.ndarray,
    axes: object = ...,
    lastsize: int = ...,
    forward: bool = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
def dct(
    a: numpy.ndarray,
    type: int,
    axes: object = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
    ortho: object = ...,
) -> numpy.ndarray: ...
def dst(
    a: numpy.ndarray,
    type: int,
    axes: object = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
    ortho: object = ...,
) -> numpy.ndarray: ...
def genuine_hartley(
    a: numpy.ndarray,
    axes: object = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
def good_size(*args, **kwargs): ...
def r2c(
    a: numpy.ndarray,
    axes: object = ...,
    forward: bool = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
def r2r_fftpack(
    a: numpy.ndarray,
    axes: object,
    real2hermitian: bool,
    forward: bool,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
def separable_hartley(
    a: numpy.ndarray,
    axes: object = ...,
    inorm: int = ...,
    out: object = ...,
    nthreads: int = ...,
) -> numpy.ndarray: ...
