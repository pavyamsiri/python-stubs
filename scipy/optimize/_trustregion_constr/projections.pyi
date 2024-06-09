from _typeshed import Incomplete

__all__ = ["orthogonality", "projections"]

def orthogonality(A, g): ...
def projections(
    A,
    method: Incomplete | None = None,
    orth_tol: float = 1e-12,
    max_refin: int = 3,
    tol: float = 1e-15,
): ...
