import numpy as np
from _typeshed import Incomplete

__all__ = [
    "legendre",
    "chebyt",
    "chebyu",
    "chebyc",
    "chebys",
    "jacobi",
    "laguerre",
    "genlaguerre",
    "hermite",
    "hermitenorm",
    "gegenbauer",
    "sh_legendre",
    "sh_chebyt",
    "sh_chebyu",
    "sh_jacobi",
    "roots_legendre",
    "roots_chebyt",
    "roots_chebyu",
    "roots_chebyc",
    "roots_chebys",
    "roots_jacobi",
    "roots_laguerre",
    "roots_genlaguerre",
    "roots_hermite",
    "roots_hermitenorm",
    "roots_gegenbauer",
    "roots_sh_legendre",
    "roots_sh_chebyt",
    "roots_sh_chebyu",
    "roots_sh_jacobi",
    "p_roots",
    "t_roots",
    "u_roots",
    "c_roots",
    "s_roots",
    "j_roots",
    "l_roots",
    "la_roots",
    "h_roots",
    "he_roots",
    "cg_roots",
    "ps_roots",
    "ts_roots",
    "us_roots",
    "js_roots",
]

class orthopoly1d(np.poly1d):
    weights: Incomplete
    weight_func: Incomplete
    limits: Incomplete
    normcoef: Incomplete
    def __init__(
        self,
        roots,
        weights: Incomplete | None = None,
        hn: float = 1.0,
        kn: float = 1.0,
        wfunc: Incomplete | None = None,
        limits: Incomplete | None = None,
        monic: bool = False,
        eval_func: Incomplete | None = None,
    ) -> None: ...
    def __call__(self, v): ...

def roots_jacobi(n, alpha, beta, mu: bool = False): ...
def jacobi(n, alpha, beta, monic: bool = False): ...
def roots_sh_jacobi(n, p1, q1, mu: bool = False): ...
def sh_jacobi(n, p, q, monic: bool = False): ...
def roots_genlaguerre(n, alpha, mu: bool = False): ...
def genlaguerre(n, alpha, monic: bool = False): ...
def roots_laguerre(n, mu: bool = False): ...
def laguerre(n, monic: bool = False): ...
def roots_hermite(n, mu: bool = False): ...
def hermite(n, monic: bool = False): ...
def roots_hermitenorm(n, mu: bool = False): ...
def hermitenorm(n, monic: bool = False): ...
def roots_gegenbauer(n, alpha, mu: bool = False): ...
def gegenbauer(n, alpha, monic: bool = False): ...
def roots_chebyt(n, mu: bool = False): ...
def chebyt(n, monic: bool = False): ...
def roots_chebyu(n, mu: bool = False): ...
def chebyu(n, monic: bool = False): ...
def roots_chebyc(n, mu: bool = False): ...
def chebyc(n, monic: bool = False): ...
def roots_chebys(n, mu: bool = False): ...
def chebys(n, monic: bool = False): ...
def roots_sh_chebyt(n, mu: bool = False): ...
def sh_chebyt(n, monic: bool = False): ...
def roots_sh_chebyu(n, mu: bool = False): ...
def sh_chebyu(n, monic: bool = False): ...
def roots_legendre(n, mu: bool = False): ...
def legendre(n, monic: bool = False): ...
def roots_sh_legendre(n, mu: bool = False): ...
def sh_legendre(n, monic: bool = False): ...

# Names in __all__ with no definition:
#   c_roots
#   cg_roots
#   h_roots
#   he_roots
#   j_roots
#   js_roots
#   l_roots
#   la_roots
#   p_roots
#   ps_roots
#   s_roots
#   t_roots
#   ts_roots
#   u_roots
#   us_roots
