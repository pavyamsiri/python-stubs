from _typeshed import Incomplete
from numpy.linalg import LinAlgError as LinAlgError

__all__ = ["LinAlgError", "LinAlgWarning", "norm"]

class LinAlgWarning(RuntimeWarning): ...

def norm(
    a,
    ord: Incomplete | None = None,
    axis: Incomplete | None = None,
    keepdims: bool = False,
    check_finite: bool = True,
): ...
