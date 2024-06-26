from _typeshed import Incomplete

__all__ = ["dct", "idct", "dst", "idst", "dctn", "idctn", "dstn", "idstn"]

def dctn(
    x,
    type: int = 2,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    orthogonalize: Incomplete | None = None,
): ...
def idctn(
    x,
    type: int = 2,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    orthogonalize: Incomplete | None = None,
): ...
def dstn(
    x,
    type: int = 2,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    orthogonalize: Incomplete | None = None,
): ...
def idstn(
    x,
    type: int = 2,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    orthogonalize: Incomplete | None = None,
): ...
def dct(
    x,
    type: int = 2,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    orthogonalize: Incomplete | None = None,
): ...
def idct(
    x,
    type: int = 2,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    orthogonalize: Incomplete | None = None,
): ...
def dst(
    x,
    type: int = 2,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    orthogonalize: Incomplete | None = None,
): ...
def idst(
    x,
    type: int = 2,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    orthogonalize: Incomplete | None = None,
): ...
