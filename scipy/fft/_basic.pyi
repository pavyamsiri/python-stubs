from _typeshed import Incomplete
from scipy._lib.uarray import (
    Dispatchable as Dispatchable,
    generate_multimethod as generate_multimethod,
)

def fft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ifft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def rfft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def irfft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def hfft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ihfft(
    x,
    n: Incomplete | None = None,
    axis: int = -1,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def fftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ifftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def fft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ifft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def rfftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def rfft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def irfftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def irfft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def hfftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def hfft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ihfftn(
    x,
    s: Incomplete | None = None,
    axes: Incomplete | None = None,
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
def ihfft2(
    x,
    s: Incomplete | None = None,
    axes=(-2, -1),
    norm: Incomplete | None = None,
    overwrite_x: bool = False,
    workers: Incomplete | None = None,
    *,
    plan: Incomplete | None = None,
): ...
