from _typeshed import Incomplete

__all__ = [
    "correlate",
    "correlation_lags",
    "correlate2d",
    "convolve",
    "convolve2d",
    "fftconvolve",
    "oaconvolve",
    "order_filter",
    "medfilt",
    "medfilt2d",
    "wiener",
    "lfilter",
    "lfiltic",
    "sosfilt",
    "deconvolve",
    "hilbert",
    "hilbert2",
    "cmplx_sort",
    "unique_roots",
    "invres",
    "invresz",
    "residue",
    "residuez",
    "resample",
    "resample_poly",
    "detrend",
    "lfilter_zi",
    "sosfilt_zi",
    "sosfiltfilt",
    "choose_conv_method",
    "filtfilt",
    "decimate",
    "vectorstrength",
]

def correlate(in1, in2, mode: str = "full", method: str = "auto"): ...
def correlation_lags(in1_len, in2_len, mode: str = "full"): ...
def fftconvolve(in1, in2, mode: str = "full", axes: Incomplete | None = None): ...
def oaconvolve(in1, in2, mode: str = "full", axes: Incomplete | None = None): ...
def choose_conv_method(in1, in2, mode: str = "full", measure: bool = False): ...
def convolve(in1, in2, mode: str = "full", method: str = "auto"): ...
def order_filter(a, domain, rank): ...
def medfilt(volume, kernel_size: Incomplete | None = None): ...
def wiener(im, mysize: Incomplete | None = None, noise: Incomplete | None = None): ...
def convolve2d(
    in1, in2, mode: str = "full", boundary: str = "fill", fillvalue: int = 0
): ...
def correlate2d(
    in1, in2, mode: str = "full", boundary: str = "fill", fillvalue: int = 0
): ...
def medfilt2d(input, kernel_size: int = 3): ...
def lfilter(b, a, x, axis: int = -1, zi: Incomplete | None = None): ...
def lfiltic(b, a, y, x: Incomplete | None = None): ...
def deconvolve(signal, divisor): ...
def hilbert(x, N: Incomplete | None = None, axis: int = -1): ...
def hilbert2(x, N: Incomplete | None = None): ...
def cmplx_sort(p): ...
def unique_roots(p, tol: float = 0.001, rtype: str = "min"): ...
def invres(r, p, k, tol: float = 0.001, rtype: str = "avg"): ...
def residue(b, a, tol: float = 0.001, rtype: str = "avg"): ...
def residuez(b, a, tol: float = 0.001, rtype: str = "avg"): ...
def invresz(r, p, k, tol: float = 0.001, rtype: str = "avg"): ...
def resample(
    x,
    num,
    t: Incomplete | None = None,
    axis: int = 0,
    window: Incomplete | None = None,
    domain: str = "time",
): ...
def resample_poly(
    x,
    up,
    down,
    axis: int = 0,
    window=("kaiser", 5.0),
    padtype: str = "constant",
    cval: Incomplete | None = None,
): ...
def vectorstrength(events, period): ...
def detrend(
    data,
    axis: int = -1,
    type: str = "linear",
    bp: int = 0,
    overwrite_data: bool = False,
): ...
def lfilter_zi(b, a): ...
def sosfilt_zi(sos): ...
def filtfilt(
    b,
    a,
    x,
    axis: int = -1,
    padtype: str = "odd",
    padlen: Incomplete | None = None,
    method: str = "pad",
    irlen: Incomplete | None = None,
): ...
def sosfilt(sos, x, axis: int = -1, zi: Incomplete | None = None): ...
def sosfiltfilt(
    sos, x, axis: int = -1, padtype: str = "odd", padlen: Incomplete | None = None
): ...
def decimate(
    x,
    q,
    n: Incomplete | None = None,
    ftype: str = "iir",
    axis: int = -1,
    zero_phase: bool = True,
): ...
