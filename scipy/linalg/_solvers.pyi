from _typeshed import Incomplete

__all__ = [
    "solve_sylvester",
    "solve_continuous_lyapunov",
    "solve_discrete_lyapunov",
    "solve_lyapunov",
    "solve_continuous_are",
    "solve_discrete_are",
]

def solve_sylvester(a, b, q): ...
def solve_continuous_lyapunov(a, q): ...

solve_lyapunov = solve_continuous_lyapunov

def solve_discrete_lyapunov(a, q, method: Incomplete | None = None): ...
def solve_continuous_are(
    a,
    b,
    q,
    r,
    e: Incomplete | None = None,
    s: Incomplete | None = None,
    balanced: bool = True,
): ...
def solve_discrete_are(
    a,
    b,
    q,
    r,
    e: Incomplete | None = None,
    s: Incomplete | None = None,
    balanced: bool = True,
): ...
