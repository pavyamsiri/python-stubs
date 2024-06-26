from _typeshed import Incomplete

__all__ = [
    "kaiser_beta",
    "kaiser_atten",
    "kaiserord",
    "firwin",
    "firwin2",
    "remez",
    "firls",
    "minimum_phase",
]

def kaiser_beta(a): ...
def kaiser_atten(numtaps, width): ...
def kaiserord(ripple, width): ...
def firwin(
    numtaps,
    cutoff,
    *,
    width: Incomplete | None = None,
    window: str = "hamming",
    pass_zero: bool = True,
    scale: bool = True,
    nyq=...,
    fs: Incomplete | None = None,
): ...
def firwin2(
    numtaps,
    freq,
    gain,
    *,
    nfreqs: Incomplete | None = None,
    window: str = "hamming",
    nyq=...,
    antisymmetric: bool = False,
    fs: Incomplete | None = None,
): ...
def remez(
    numtaps,
    bands,
    desired,
    *,
    weight: Incomplete | None = None,
    Hz=...,
    type: str = "bandpass",
    maxiter: int = 25,
    grid_density: int = 16,
    fs: Incomplete | None = None,
): ...
def firls(
    numtaps,
    bands,
    desired,
    *,
    weight: Incomplete | None = None,
    nyq=...,
    fs: Incomplete | None = None,
): ...
def minimum_phase(h, method: str = "homomorphic", n_fft: Incomplete | None = None): ...
