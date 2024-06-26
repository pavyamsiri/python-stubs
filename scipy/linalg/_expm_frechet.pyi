from _typeshed import Incomplete

__all__ = ["expm_frechet", "expm_cond"]

def expm_frechet(
    A,
    E,
    method: Incomplete | None = None,
    compute_expm: bool = True,
    check_finite: bool = True,
): ...
def expm_cond(A, check_finite: bool = True): ...
