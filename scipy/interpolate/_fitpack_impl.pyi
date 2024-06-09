from _typeshed import Incomplete

__all__ = [
    "splrep",
    "splprep",
    "splev",
    "splint",
    "sproot",
    "spalde",
    "bisplrep",
    "bisplev",
    "insert",
    "splder",
    "splantider",
]

def splprep(
    x,
    w: Incomplete | None = None,
    u: Incomplete | None = None,
    ub: Incomplete | None = None,
    ue: Incomplete | None = None,
    k: int = 3,
    task: int = 0,
    s: Incomplete | None = None,
    t: Incomplete | None = None,
    full_output: int = 0,
    nest: Incomplete | None = None,
    per: int = 0,
    quiet: int = 1,
): ...
def splrep(
    x,
    y,
    w: Incomplete | None = None,
    xb: Incomplete | None = None,
    xe: Incomplete | None = None,
    k: int = 3,
    task: int = 0,
    s: Incomplete | None = None,
    t: Incomplete | None = None,
    full_output: int = 0,
    per: int = 0,
    quiet: int = 1,
): ...
def splev(x, tck, der: int = 0, ext: int = 0): ...
def splint(a, b, tck, full_output: int = 0): ...
def sproot(tck, mest: int = 10): ...
def spalde(x, tck): ...
def bisplrep(
    x,
    y,
    z,
    w: Incomplete | None = None,
    xb: Incomplete | None = None,
    xe: Incomplete | None = None,
    yb: Incomplete | None = None,
    ye: Incomplete | None = None,
    kx: int = 3,
    ky: int = 3,
    task: int = 0,
    s: Incomplete | None = None,
    eps: float = 1e-16,
    tx: Incomplete | None = None,
    ty: Incomplete | None = None,
    full_output: int = 0,
    nxest: Incomplete | None = None,
    nyest: Incomplete | None = None,
    quiet: int = 1,
): ...
def bisplev(x, y, tck, dx: int = 0, dy: int = 0): ...
def insert(x, tck, m: int = 1, per: int = 0): ...
def splder(tck, n: int = 1): ...
def splantider(tck, n: int = 1): ...
