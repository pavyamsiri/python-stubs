from _typeshed import Incomplete

__all__ = ['tf2ss', 'abcd_normalize', 'ss2tf', 'zpk2ss', 'ss2zpk', 'cont2discrete']

def tf2ss(num, den): ...
def abcd_normalize(A: Incomplete | None = None, B: Incomplete | None = None, C: Incomplete | None = None, D: Incomplete | None = None): ...
def ss2tf(A, B, C, D, input: int = 0): ...
def zpk2ss(z, p, k): ...
def ss2zpk(A, B, C, D, input: int = 0): ...
def cont2discrete(system, dt, method: str = 'zoh', alpha: Incomplete | None = None): ...
