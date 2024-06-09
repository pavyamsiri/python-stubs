from _typeshed import Incomplete

__all__ = ["qr", "qr_multiply", "rq"]

def qr(
    a,
    overwrite_a: bool = False,
    lwork: Incomplete | None = None,
    mode: str = "full",
    pivoting: bool = False,
    check_finite: bool = True,
): ...
def qr_multiply(
    a,
    c,
    mode: str = "right",
    pivoting: bool = False,
    conjugate: bool = False,
    overwrite_a: bool = False,
    overwrite_c: bool = False,
): ...
def rq(
    a,
    overwrite_a: bool = False,
    lwork: Incomplete | None = None,
    mode: str = "full",
    check_finite: bool = True,
): ...
