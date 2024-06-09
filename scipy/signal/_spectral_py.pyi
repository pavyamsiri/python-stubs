from _typeshed import Incomplete

__all__ = [
    "periodogram",
    "welch",
    "lombscargle",
    "csd",
    "coherence",
    "spectrogram",
    "stft",
    "istft",
    "check_COLA",
    "check_NOLA",
]

def lombscargle(x, y, freqs, precenter: bool = False, normalize: bool = False): ...
def periodogram(
    x,
    fs: float = 1.0,
    window: str = "boxcar",
    nfft: Incomplete | None = None,
    detrend: str = "constant",
    return_onesided: bool = True,
    scaling: str = "density",
    axis: int = -1,
): ...
def welch(
    x,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    detrend: str = "constant",
    return_onesided: bool = True,
    scaling: str = "density",
    axis: int = -1,
    average: str = "mean",
): ...
def csd(
    x,
    y,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    detrend: str = "constant",
    return_onesided: bool = True,
    scaling: str = "density",
    axis: int = -1,
    average: str = "mean",
): ...
def spectrogram(
    x,
    fs: float = 1.0,
    window=("tukey", 0.25),
    nperseg: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    detrend: str = "constant",
    return_onesided: bool = True,
    scaling: str = "density",
    axis: int = -1,
    mode: str = "psd",
): ...
def check_COLA(window, nperseg, noverlap, tol: float = 1e-10): ...
def check_NOLA(window, nperseg, noverlap, tol: float = 1e-10): ...
def stft(
    x,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: int = 256,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    detrend: bool = False,
    return_onesided: bool = True,
    boundary: str = "zeros",
    padded: bool = True,
    axis: int = -1,
    scaling: str = "spectrum",
): ...
def istft(
    Zxx,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    input_onesided: bool = True,
    boundary: bool = True,
    time_axis: int = -1,
    freq_axis: int = -2,
    scaling: str = "spectrum",
): ...
def coherence(
    x,
    y,
    fs: float = 1.0,
    window: str = "hann",
    nperseg: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    nfft: Incomplete | None = None,
    detrend: str = "constant",
    axis: int = -1,
): ...
