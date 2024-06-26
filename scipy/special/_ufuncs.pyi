import _cython_3_0_10
import numpy
import types
from typing import Any, overload

__test__: dict
agm: numpy.ufunc
airy: numpy.ufunc
airye: numpy.ufunc
bdtr: numpy.ufunc
bdtrc: numpy.ufunc
bdtri: numpy.ufunc
bdtrik: numpy.ufunc
bdtrin: numpy.ufunc
bei: numpy.ufunc
beip: numpy.ufunc
ber: numpy.ufunc
berp: numpy.ufunc
besselpoly: numpy.ufunc
beta: numpy.ufunc
betainc: numpy.ufunc
betaincc: numpy.ufunc
betainccinv: numpy.ufunc
betaincinv: numpy.ufunc
betaln: numpy.ufunc
binom: numpy.ufunc
boxcox: numpy.ufunc
boxcox1p: numpy.ufunc
btdtr: numpy.ufunc
btdtri: numpy.ufunc
btdtria: numpy.ufunc
btdtrib: numpy.ufunc
cbrt: numpy.ufunc
chdtr: numpy.ufunc
chdtrc: numpy.ufunc
chdtri: numpy.ufunc
chdtriv: numpy.ufunc
chndtr: numpy.ufunc
chndtridf: numpy.ufunc
chndtrinc: numpy.ufunc
chndtrix: numpy.ufunc
cosdg: numpy.ufunc
cosm1: numpy.ufunc
cotdg: numpy.ufunc
dawsn: numpy.ufunc
ellipe: numpy.ufunc
ellipeinc: numpy.ufunc
ellipj: numpy.ufunc
ellipk: numpy.ufunc
ellipkinc: numpy.ufunc
ellipkm1: numpy.ufunc
elliprc: numpy.ufunc
elliprd: numpy.ufunc
elliprf: numpy.ufunc
elliprg: numpy.ufunc
elliprj: numpy.ufunc
entr: numpy.ufunc
erf: numpy.ufunc
erfc: numpy.ufunc
erfcinv: numpy.ufunc
erfcx: numpy.ufunc
erfi: numpy.ufunc
erfinv: numpy.ufunc
eval_chebyc: numpy.ufunc
eval_chebys: numpy.ufunc
eval_chebyt: numpy.ufunc
eval_chebyu: numpy.ufunc
eval_gegenbauer: numpy.ufunc
eval_genlaguerre: numpy.ufunc
eval_hermite: numpy.ufunc
eval_hermitenorm: numpy.ufunc
eval_jacobi: numpy.ufunc
eval_laguerre: numpy.ufunc
eval_legendre: numpy.ufunc
eval_sh_chebyt: numpy.ufunc
eval_sh_chebyu: numpy.ufunc
eval_sh_jacobi: numpy.ufunc
eval_sh_legendre: numpy.ufunc
exp1: numpy.ufunc
exp10: numpy.ufunc
exp2: numpy.ufunc
expi: numpy.ufunc
expit: numpy.ufunc
expm1: numpy.ufunc
expn: numpy.ufunc
exprel: numpy.ufunc
fdtr: numpy.ufunc
fdtrc: numpy.ufunc
fdtri: numpy.ufunc
fdtridfd: numpy.ufunc
fresnel: numpy.ufunc
gamma: numpy.ufunc
gammainc: numpy.ufunc
gammaincc: numpy.ufunc
gammainccinv: numpy.ufunc
gammaincinv: numpy.ufunc
gammaln: numpy.ufunc
gammasgn: numpy.ufunc
gdtr: numpy.ufunc
gdtrc: numpy.ufunc
gdtria: numpy.ufunc
gdtrib: numpy.ufunc
gdtrix: numpy.ufunc
geterr: _cython_3_0_10.cython_function_or_method
hankel1: numpy.ufunc
hankel1e: numpy.ufunc
hankel2: numpy.ufunc
hankel2e: numpy.ufunc
huber: numpy.ufunc
hyp0f1: numpy.ufunc
hyp1f1: numpy.ufunc
hyp2f1: numpy.ufunc
hyperu: numpy.ufunc
i0: numpy.ufunc
i0e: numpy.ufunc
i1: numpy.ufunc
i1e: numpy.ufunc
inv_boxcox: numpy.ufunc
inv_boxcox1p: numpy.ufunc
it2i0k0: numpy.ufunc
it2j0y0: numpy.ufunc
it2struve0: numpy.ufunc
itairy: numpy.ufunc
iti0k0: numpy.ufunc
itj0y0: numpy.ufunc
itmodstruve0: numpy.ufunc
itstruve0: numpy.ufunc
iv: numpy.ufunc
ive: numpy.ufunc
j0: numpy.ufunc
j1: numpy.ufunc
jn: numpy.ufunc
jv: numpy.ufunc
jve: numpy.ufunc
k0: numpy.ufunc
k0e: numpy.ufunc
k1: numpy.ufunc
k1e: numpy.ufunc
kei: numpy.ufunc
keip: numpy.ufunc
kelvin: numpy.ufunc
ker: numpy.ufunc
kerp: numpy.ufunc
kl_div: numpy.ufunc
kn: numpy.ufunc
kolmogi: numpy.ufunc
kolmogorov: numpy.ufunc
kv: numpy.ufunc
kve: numpy.ufunc
log1p: numpy.ufunc
log_expit: numpy.ufunc
log_ndtr: numpy.ufunc
loggamma: numpy.ufunc
logit: numpy.ufunc
lpmv: numpy.ufunc
mathieu_a: numpy.ufunc
mathieu_b: numpy.ufunc
mathieu_cem: numpy.ufunc
mathieu_modcem1: numpy.ufunc
mathieu_modcem2: numpy.ufunc
mathieu_modsem1: numpy.ufunc
mathieu_modsem2: numpy.ufunc
mathieu_sem: numpy.ufunc
modfresnelm: numpy.ufunc
modfresnelp: numpy.ufunc
modstruve: numpy.ufunc
nbdtr: numpy.ufunc
nbdtrc: numpy.ufunc
nbdtri: numpy.ufunc
nbdtrik: numpy.ufunc
nbdtrin: numpy.ufunc
ncfdtr: numpy.ufunc
ncfdtri: numpy.ufunc
ncfdtridfd: numpy.ufunc
ncfdtridfn: numpy.ufunc
ncfdtrinc: numpy.ufunc
nctdtr: numpy.ufunc
nctdtridf: numpy.ufunc
nctdtrinc: numpy.ufunc
nctdtrit: numpy.ufunc
ndtr: numpy.ufunc
ndtri: numpy.ufunc
ndtri_exp: numpy.ufunc
nrdtrimn: numpy.ufunc
nrdtrisd: numpy.ufunc
obl_ang1: numpy.ufunc
obl_ang1_cv: numpy.ufunc
obl_cv: numpy.ufunc
obl_rad1: numpy.ufunc
obl_rad1_cv: numpy.ufunc
obl_rad2: numpy.ufunc
obl_rad2_cv: numpy.ufunc
owens_t: numpy.ufunc
pbdv: numpy.ufunc
pbvv: numpy.ufunc
pbwa: numpy.ufunc
pdtr: numpy.ufunc
pdtrc: numpy.ufunc
pdtri: numpy.ufunc
pdtrik: numpy.ufunc
poch: numpy.ufunc
powm1: numpy.ufunc
pro_ang1: numpy.ufunc
pro_ang1_cv: numpy.ufunc
pro_cv: numpy.ufunc
pro_rad1: numpy.ufunc
pro_rad1_cv: numpy.ufunc
pro_rad2: numpy.ufunc
pro_rad2_cv: numpy.ufunc
pseudo_huber: numpy.ufunc
psi: numpy.ufunc
radian: numpy.ufunc
rel_entr: numpy.ufunc
rgamma: numpy.ufunc
round: numpy.ufunc
seterr: _cython_3_0_10.cython_function_or_method
shichi: numpy.ufunc
sici: numpy.ufunc
sindg: numpy.ufunc
smirnov: numpy.ufunc
smirnovi: numpy.ufunc
spence: numpy.ufunc
sph_harm: numpy.ufunc
stdtr: numpy.ufunc
stdtridf: numpy.ufunc
stdtrit: numpy.ufunc
struve: numpy.ufunc
tandg: numpy.ufunc
tklmbda: numpy.ufunc
voigt_profile: numpy.ufunc
wofz: numpy.ufunc
wright_bessel: numpy.ufunc
wrightomega: numpy.ufunc
xlog1py: numpy.ufunc
xlogy: numpy.ufunc
y0: numpy.ufunc
y1: numpy.ufunc
yn: numpy.ufunc
yv: numpy.ufunc
yve: numpy.ufunc
zetac: numpy.ufunc

class errstate:
    @overload
    def __init__(self, singular=...) -> Any: ...
    @overload
    def __init__(self, all=..., singular=...) -> Any: ...
    def __enter__(self): ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ): ...
