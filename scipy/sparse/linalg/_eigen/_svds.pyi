from _typeshed import Incomplete

__all__ = ["svds"]

def svds(
    A,
    k: int = 6,
    ncv: Incomplete | None = None,
    tol: int = 0,
    which: str = "LM",
    v0: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    return_singular_vectors: bool = True,
    solver: str = "arpack",
    random_state: Incomplete | None = None,
    options: Incomplete | None = None,
): ...
