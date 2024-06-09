from _typeshed import Incomplete

__all__ = ["schur", "rsf2csf"]

def schur(
    a,
    output: str = "real",
    lwork: Incomplete | None = None,
    overwrite_a: bool = False,
    sort: Incomplete | None = None,
    check_finite: bool = True,
): ...
def rsf2csf(T, Z, check_finite: bool = True): ...
