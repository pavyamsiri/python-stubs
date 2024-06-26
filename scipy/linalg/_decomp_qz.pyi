from _typeshed import Incomplete

__all__ = ["qz", "ordqz"]

def qz(
    A,
    B,
    output: str = "real",
    lwork: Incomplete | None = None,
    sort: Incomplete | None = None,
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
): ...
def ordqz(
    A,
    B,
    sort: str = "lhp",
    output: str = "real",
    overwrite_a: bool = False,
    overwrite_b: bool = False,
    check_finite: bool = True,
): ...
