from scipy.sparse.linalg._interface import (
    IdentityOperator as IdentityOperator,
    LinearOperator as LinearOperator,
    aslinearoperator as aslinearoperator,
)

__docformat__: str

def coerce(x, y): ...
def id(x): ...
def make_system(A, M, x0, b): ...
