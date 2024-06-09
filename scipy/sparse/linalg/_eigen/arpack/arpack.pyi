from _typeshed import Incomplete
from scipy.sparse.linalg._interface import LinearOperator

__all__ = ["eigs", "eigsh", "ArpackError", "ArpackNoConvergence"]

SNAUPD_ERRORS = DNAUPD_ERRORS
CNAUPD_ERRORS = ZNAUPD_ERRORS
SSAUPD_ERRORS = DSAUPD_ERRORS

class ArpackError(RuntimeError):
    def __init__(self, info, infodict=...) -> None: ...

class ArpackNoConvergence(ArpackError):
    eigenvalues: Incomplete
    eigenvectors: Incomplete
    def __init__(self, msg, eigenvalues, eigenvectors) -> None: ...

class _ArpackParams:
    resid: Incomplete
    sigma: int
    v: Incomplete
    iparam: Incomplete
    mode: Incomplete
    n: Incomplete
    tol: Incomplete
    k: Incomplete
    maxiter: Incomplete
    ncv: Incomplete
    which: Incomplete
    tp: Incomplete
    info: Incomplete
    converged: bool
    ido: int
    def __init__(
        self,
        n,
        k,
        tp,
        mode: int = 1,
        sigma: Incomplete | None = None,
        ncv: Incomplete | None = None,
        v0: Incomplete | None = None,
        maxiter: Incomplete | None = None,
        which: str = "LM",
        tol: int = 0,
    ) -> None: ...

class _SymmetricArpackParams(_ArpackParams):
    OP: Incomplete
    B: Incomplete
    bmat: str
    OPa: Incomplete
    OPb: Incomplete
    A_matvec: Incomplete
    workd: Incomplete
    workl: Incomplete
    iterate_infodict: Incomplete
    extract_infodict: Incomplete
    ipntr: Incomplete
    def __init__(
        self,
        n,
        k,
        tp,
        matvec,
        mode: int = 1,
        M_matvec: Incomplete | None = None,
        Minv_matvec: Incomplete | None = None,
        sigma: Incomplete | None = None,
        ncv: Incomplete | None = None,
        v0: Incomplete | None = None,
        maxiter: Incomplete | None = None,
        which: str = "LM",
        tol: int = 0,
    ) -> None: ...
    converged: bool
    def iterate(self) -> None: ...
    def extract(self, return_eigenvectors): ...

class _UnsymmetricArpackParams(_ArpackParams):
    OP: Incomplete
    B: Incomplete
    bmat: str
    OPa: Incomplete
    OPb: Incomplete
    matvec: Incomplete
    workd: Incomplete
    workl: Incomplete
    iterate_infodict: Incomplete
    extract_infodict: Incomplete
    ipntr: Incomplete
    rwork: Incomplete
    def __init__(
        self,
        n,
        k,
        tp,
        matvec,
        mode: int = 1,
        M_matvec: Incomplete | None = None,
        Minv_matvec: Incomplete | None = None,
        sigma: Incomplete | None = None,
        ncv: Incomplete | None = None,
        v0: Incomplete | None = None,
        maxiter: Incomplete | None = None,
        which: str = "LM",
        tol: int = 0,
    ) -> None: ...
    converged: bool
    def iterate(self) -> None: ...
    def extract(self, return_eigenvectors): ...

class SpLuInv(LinearOperator):
    M_lu: Incomplete
    shape: Incomplete
    dtype: Incomplete
    isreal: Incomplete
    def __init__(self, M) -> None: ...

class LuInv(LinearOperator):
    M_lu: Incomplete
    shape: Incomplete
    dtype: Incomplete
    def __init__(self, M) -> None: ...

class IterInv(LinearOperator):
    M: Incomplete
    dtype: Incomplete
    shape: Incomplete
    ifunc: Incomplete
    tol: Incomplete
    def __init__(self, M, ifunc=..., tol: int = 0) -> None: ...

class IterOpInv(LinearOperator):
    A: Incomplete
    M: Incomplete
    sigma: Incomplete
    OP: Incomplete
    shape: Incomplete
    ifunc: Incomplete
    tol: Incomplete
    def __init__(self, A, M, sigma, ifunc=..., tol: int = 0) -> None: ...
    @property
    def dtype(self): ...

def eigs(
    A,
    k: int = 6,
    M: Incomplete | None = None,
    sigma: Incomplete | None = None,
    which: str = "LM",
    v0: Incomplete | None = None,
    ncv: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    tol: int = 0,
    return_eigenvectors: bool = True,
    Minv: Incomplete | None = None,
    OPinv: Incomplete | None = None,
    OPpart: Incomplete | None = None,
): ...
def eigsh(
    A,
    k: int = 6,
    M: Incomplete | None = None,
    sigma: Incomplete | None = None,
    which: str = "LM",
    v0: Incomplete | None = None,
    ncv: Incomplete | None = None,
    maxiter: Incomplete | None = None,
    tol: int = 0,
    return_eigenvectors: bool = True,
    Minv: Incomplete | None = None,
    OPinv: Incomplete | None = None,
    mode: str = "normal",
): ...
