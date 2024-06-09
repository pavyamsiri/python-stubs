from _typeshed import Incomplete

__all__ = ["logsumexp", "softmax", "log_softmax"]

def logsumexp(
    a,
    axis: Incomplete | None = None,
    b: Incomplete | None = None,
    keepdims: bool = False,
    return_sign: bool = False,
): ...
def softmax(x, axis: Incomplete | None = None): ...
def log_softmax(x, axis: Incomplete | None = None): ...
