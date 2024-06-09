from _typeshed import Incomplete
from scipy.sparse.linalg import LinearOperator

__all__ = ['fmin_l_bfgs_b', 'LbfgsInvHessProduct']

def fmin_l_bfgs_b(func, x0, fprime: Incomplete | None = None, args=(), approx_grad: int = 0, bounds: Incomplete | None = None, m: int = 10, factr: float = 10000000.0, pgtol: float = 1e-05, epsilon: float = 1e-08, iprint: int = -1, maxfun: int = 15000, maxiter: int = 15000, disp: Incomplete | None = None, callback: Incomplete | None = None, maxls: int = 20): ...

class LbfgsInvHessProduct(LinearOperator):
    sk: Incomplete
    yk: Incomplete
    n_corrs: Incomplete
    rho: Incomplete
    def __init__(self, sk, yk) -> None: ...
    def todense(self): ...
