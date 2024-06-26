from ._ufuncs import psi
from _typeshed import Incomplete
from numpy import sinc as sinc

__all__ = [
    "ai_zeros",
    "assoc_laguerre",
    "bei_zeros",
    "beip_zeros",
    "ber_zeros",
    "bernoulli",
    "berp_zeros",
    "bi_zeros",
    "clpmn",
    "comb",
    "digamma",
    "diric",
    "erf_zeros",
    "euler",
    "factorial",
    "factorial2",
    "factorialk",
    "fresnel_zeros",
    "fresnelc_zeros",
    "fresnels_zeros",
    "h1vp",
    "h2vp",
    "ivp",
    "jn_zeros",
    "jnjnp_zeros",
    "jnp_zeros",
    "jnyn_zeros",
    "jvp",
    "kei_zeros",
    "keip_zeros",
    "kelvin_zeros",
    "ker_zeros",
    "kerp_zeros",
    "kvp",
    "lmbda",
    "lpmn",
    "lpn",
    "lqmn",
    "lqn",
    "mathieu_even_coef",
    "mathieu_odd_coef",
    "obl_cv_seq",
    "pbdn_seq",
    "pbdv_seq",
    "pbvv_seq",
    "perm",
    "polygamma",
    "pro_cv_seq",
    "riccati_jn",
    "riccati_yn",
    "sinc",
    "stirling2",
    "y0_zeros",
    "y1_zeros",
    "y1p_zeros",
    "yn_zeros",
    "ynp_zeros",
    "yvp",
    "zeta",
]

def diric(x, n): ...
def jnjnp_zeros(nt): ...
def jnyn_zeros(n, nt): ...
def jn_zeros(n, nt): ...
def jnp_zeros(n, nt): ...
def yn_zeros(n, nt): ...
def ynp_zeros(n, nt): ...
def y0_zeros(nt, complex: bool = False): ...
def y1_zeros(nt, complex: bool = False): ...
def y1p_zeros(nt, complex: bool = False): ...
def jvp(v, z, n: int = 1): ...
def yvp(v, z, n: int = 1): ...
def kvp(v, z, n: int = 1): ...
def ivp(v, z, n: int = 1): ...
def h1vp(v, z, n: int = 1): ...
def h2vp(v, z, n: int = 1): ...
def riccati_jn(n, x): ...
def riccati_yn(n, x): ...
def erf_zeros(nt): ...
def fresnelc_zeros(nt): ...
def fresnels_zeros(nt): ...
def fresnel_zeros(nt): ...
def assoc_laguerre(x, n, k: float = 0.0): ...

digamma = psi

def polygamma(n, x): ...
def mathieu_even_coef(m, q): ...
def mathieu_odd_coef(m, q): ...
def lpmn(m, n, z): ...
def clpmn(m, n, z, type: int = 3): ...
def lqmn(m, n, z): ...
def bernoulli(n): ...
def euler(n): ...
def lpn(n, z): ...
def lqn(n, z): ...
def ai_zeros(nt): ...
def bi_zeros(nt): ...
def lmbda(v, x): ...
def pbdv_seq(v, x): ...
def pbvv_seq(v, x): ...
def pbdn_seq(n, z): ...
def ber_zeros(nt): ...
def bei_zeros(nt): ...
def ker_zeros(nt): ...
def kei_zeros(nt): ...
def berp_zeros(nt): ...
def beip_zeros(nt): ...
def kerp_zeros(nt): ...
def keip_zeros(nt): ...
def kelvin_zeros(nt): ...
def pro_cv_seq(m, n, c): ...
def obl_cv_seq(m, n, c): ...
def comb(N, k, *, exact: bool = False, repetition: bool = False, legacy=...): ...
def perm(N, k, exact: bool = False): ...
def factorial(n, exact: bool = False): ...
def factorial2(n, exact: bool = False): ...
def factorialk(n, k, exact: Incomplete | None = None): ...
def stirling2(N, K, *, exact: bool = False): ...
def zeta(x, q: Incomplete | None = None, out: Incomplete | None = None): ...
