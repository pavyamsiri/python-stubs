from ._fftlog_backend import fhtoffset as fhtoffset

__all__ = ["fht", "ifht", "fhtoffset"]

def fht(a, dln, mu, offset: float = 0.0, bias: float = 0.0): ...
def ifht(A, dln, mu, offset: float = 0.0, bias: float = 0.0): ...
