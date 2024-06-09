from _typeshed import Incomplete
from numpy import absolute

__all__ = [
    "findfreqs",
    "freqs",
    "freqz",
    "tf2zpk",
    "zpk2tf",
    "normalize",
    "lp2lp",
    "lp2hp",
    "lp2bp",
    "lp2bs",
    "bilinear",
    "iirdesign",
    "iirfilter",
    "butter",
    "cheby1",
    "cheby2",
    "ellip",
    "bessel",
    "band_stop_obj",
    "buttord",
    "cheb1ord",
    "cheb2ord",
    "ellipord",
    "buttap",
    "cheb1ap",
    "cheb2ap",
    "ellipap",
    "besselap",
    "BadCoefficients",
    "freqs_zpk",
    "freqz_zpk",
    "tf2sos",
    "sos2tf",
    "zpk2sos",
    "sos2zpk",
    "group_delay",
    "sosfreqz",
    "iirnotch",
    "iirpeak",
    "bilinear_zpk",
    "lp2lp_zpk",
    "lp2hp_zpk",
    "lp2bp_zpk",
    "lp2bs_zpk",
    "gammatone",
    "iircomb",
]

class BadCoefficients(UserWarning): ...

abs = absolute

def findfreqs(num, den, N, kind: str = "ba"): ...
def freqs(b, a, worN: int = 200, plot: Incomplete | None = None): ...
def freqs_zpk(z, p, k, worN: int = 200): ...
def freqz(
    b,
    a: int = 1,
    worN: int = 512,
    whole: bool = False,
    plot: Incomplete | None = None,
    fs=...,
    include_nyquist: bool = False,
): ...
def freqz_zpk(z, p, k, worN: int = 512, whole: bool = False, fs=...): ...
def group_delay(system, w: int = 512, whole: bool = False, fs=...): ...
def sosfreqz(sos, worN: int = 512, whole: bool = False, fs=...): ...
def tf2zpk(b, a): ...
def zpk2tf(z, p, k): ...
def tf2sos(b, a, pairing: Incomplete | None = None, *, analog: bool = False): ...
def sos2tf(sos): ...
def sos2zpk(sos): ...
def zpk2sos(z, p, k, pairing: Incomplete | None = None, *, analog: bool = False): ...
def normalize(b, a): ...
def lp2lp(b, a, wo: float = 1.0): ...
def lp2hp(b, a, wo: float = 1.0): ...
def lp2bp(b, a, wo: float = 1.0, bw: float = 1.0): ...
def lp2bs(b, a, wo: float = 1.0, bw: float = 1.0): ...
def bilinear(b, a, fs: float = 1.0): ...
def iirdesign(
    wp,
    ws,
    gpass,
    gstop,
    analog: bool = False,
    ftype: str = "ellip",
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def iirfilter(
    N,
    Wn,
    rp: Incomplete | None = None,
    rs: Incomplete | None = None,
    btype: str = "band",
    analog: bool = False,
    ftype: str = "butter",
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def bilinear_zpk(z, p, k, fs): ...
def lp2lp_zpk(z, p, k, wo: float = 1.0): ...
def lp2hp_zpk(z, p, k, wo: float = 1.0): ...
def lp2bp_zpk(z, p, k, wo: float = 1.0, bw: float = 1.0): ...
def lp2bs_zpk(z, p, k, wo: float = 1.0, bw: float = 1.0): ...
def butter(
    N,
    Wn,
    btype: str = "low",
    analog: bool = False,
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def cheby1(
    N,
    rp,
    Wn,
    btype: str = "low",
    analog: bool = False,
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def cheby2(
    N,
    rs,
    Wn,
    btype: str = "low",
    analog: bool = False,
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def ellip(
    N,
    rp,
    rs,
    Wn,
    btype: str = "low",
    analog: bool = False,
    output: str = "ba",
    fs: Incomplete | None = None,
): ...
def bessel(
    N,
    Wn,
    btype: str = "low",
    analog: bool = False,
    output: str = "ba",
    norm: str = "phase",
    fs: Incomplete | None = None,
): ...
def band_stop_obj(wp, ind, passb, stopb, gpass, gstop, type): ...
def buttord(
    wp, ws, gpass, gstop, analog: bool = False, fs: Incomplete | None = None
): ...
def cheb1ord(
    wp, ws, gpass, gstop, analog: bool = False, fs: Incomplete | None = None
): ...
def cheb2ord(
    wp, ws, gpass, gstop, analog: bool = False, fs: Incomplete | None = None
): ...
def ellipord(
    wp, ws, gpass, gstop, analog: bool = False, fs: Incomplete | None = None
): ...
def buttap(N): ...
def cheb1ap(N, rp): ...
def cheb2ap(N, rs): ...
def ellipap(N, rp, rs): ...
def besselap(N, norm: str = "phase"): ...
def iirnotch(w0, Q, fs: float = 2.0): ...
def iirpeak(w0, Q, fs: float = 2.0): ...
def iircomb(
    w0, Q, ftype: str = "notch", fs: float = 2.0, *, pass_zero: bool = False
): ...
def gammatone(
    freq,
    ftype,
    order: Incomplete | None = None,
    numtaps: Incomplete | None = None,
    fs: Incomplete | None = None,
): ...
