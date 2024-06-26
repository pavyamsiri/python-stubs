from _typeshed import Incomplete

__all__ = [
    "argrelmin",
    "argrelmax",
    "argrelextrema",
    "peak_prominences",
    "peak_widths",
    "find_peaks",
    "find_peaks_cwt",
]

def argrelmin(data, axis: int = 0, order: int = 1, mode: str = "clip"): ...
def argrelmax(data, axis: int = 0, order: int = 1, mode: str = "clip"): ...
def argrelextrema(
    data, comparator, axis: int = 0, order: int = 1, mode: str = "clip"
): ...
def peak_prominences(x, peaks, wlen: Incomplete | None = None): ...
def peak_widths(
    x,
    peaks,
    rel_height: float = 0.5,
    prominence_data: Incomplete | None = None,
    wlen: Incomplete | None = None,
): ...
def find_peaks(
    x,
    height: Incomplete | None = None,
    threshold: Incomplete | None = None,
    distance: Incomplete | None = None,
    prominence: Incomplete | None = None,
    width: Incomplete | None = None,
    wlen: Incomplete | None = None,
    rel_height: float = 0.5,
    plateau_size: Incomplete | None = None,
): ...
def find_peaks_cwt(
    vector,
    widths,
    wavelet: Incomplete | None = None,
    max_distances: Incomplete | None = None,
    gap_thresh: Incomplete | None = None,
    min_length: Incomplete | None = None,
    min_snr: int = 1,
    noise_perc: int = 10,
    window_size: Incomplete | None = None,
): ...
