from _typeshed import Incomplete

__all__ = ["whiten", "vq", "kmeans", "kmeans2"]

class ClusterError(Exception): ...

def whiten(obs, check_finite: bool = True): ...
def vq(obs, code_book, check_finite: bool = True): ...
def kmeans(
    obs,
    k_or_guess,
    iter: int = 20,
    thresh: float = 1e-05,
    check_finite: bool = True,
    *,
    seed: Incomplete | None = None,
): ...
def kmeans2(
    data,
    k,
    iter: int = 10,
    thresh: float = 1e-05,
    minit: str = "random",
    missing: str = "warn",
    check_finite: bool = True,
    *,
    seed: Incomplete | None = None,
): ...
