from _typeshed import Incomplete

__all__ = ["sawtooth", "square", "gausspulse", "chirp", "sweep_poly", "unit_impulse"]

def sawtooth(t, width: int = 1): ...
def square(t, duty: float = 0.5): ...
def gausspulse(
    t,
    fc: int = 1000,
    bw: float = 0.5,
    bwr: int = -6,
    tpr: int = -60,
    retquad: bool = False,
    retenv: bool = False,
): ...
def chirp(
    t, f0, t1, f1, method: str = "linear", phi: int = 0, vertex_zero: bool = True
): ...
def sweep_poly(t, poly, phi: int = 0): ...
def unit_impulse(shape, idx: Incomplete | None = None, dtype=...): ...
