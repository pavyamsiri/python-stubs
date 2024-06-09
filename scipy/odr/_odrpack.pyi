from _typeshed import Incomplete

__all__ = ['odr', 'OdrWarning', 'OdrError', 'OdrStop', 'Data', 'RealData', 'Model', 'Output', 'ODR', 'odr_error', 'odr_stop']

odr: Incomplete

class OdrWarning(UserWarning): ...
class OdrError(Exception): ...
class OdrStop(Exception): ...
odr_error = OdrError
odr_stop = OdrStop

class Data:
    x: Incomplete
    y: Incomplete
    we: Incomplete
    wd: Incomplete
    fix: Incomplete
    meta: Incomplete
    def __init__(self, x, y: Incomplete | None = None, we: Incomplete | None = None, wd: Incomplete | None = None, fix: Incomplete | None = None, meta: Incomplete | None = None) -> None: ...
    def set_meta(self, **kwds) -> None: ...
    def __getattr__(self, attr): ...

class RealData(Data):
    x: Incomplete
    y: Incomplete
    sx: Incomplete
    sy: Incomplete
    covx: Incomplete
    covy: Incomplete
    fix: Incomplete
    meta: Incomplete
    def __init__(self, x, y: Incomplete | None = None, sx: Incomplete | None = None, sy: Incomplete | None = None, covx: Incomplete | None = None, covy: Incomplete | None = None, fix: Incomplete | None = None, meta: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...

class Model:
    fcn: Incomplete
    fjacb: Incomplete
    fjacd: Incomplete
    extra_args: Incomplete
    estimate: Incomplete
    implicit: Incomplete
    meta: Incomplete
    def __init__(self, fcn, fjacb: Incomplete | None = None, fjacd: Incomplete | None = None, extra_args: Incomplete | None = None, estimate: Incomplete | None = None, implicit: int = 0, meta: Incomplete | None = None) -> None: ...
    def set_meta(self, **kwds) -> None: ...
    def __getattr__(self, attr): ...

class Output:
    beta: Incomplete
    sd_beta: Incomplete
    cov_beta: Incomplete
    stopreason: Incomplete
    def __init__(self, output) -> None: ...
    def pprint(self) -> None: ...

class ODR:
    data: Incomplete
    model: Incomplete
    beta0: Incomplete
    delta0: Incomplete
    ifixx: Incomplete
    ifixb: Incomplete
    job: Incomplete
    iprint: Incomplete
    errfile: Incomplete
    rptfile: Incomplete
    ndigit: Incomplete
    taufac: Incomplete
    sstol: Incomplete
    partol: Incomplete
    maxit: Incomplete
    stpb: Incomplete
    stpd: Incomplete
    sclb: Incomplete
    scld: Incomplete
    work: Incomplete
    iwork: Incomplete
    output: Incomplete
    def __init__(self, data, model, beta0: Incomplete | None = None, delta0: Incomplete | None = None, ifixb: Incomplete | None = None, ifixx: Incomplete | None = None, job: Incomplete | None = None, iprint: Incomplete | None = None, errfile: Incomplete | None = None, rptfile: Incomplete | None = None, ndigit: Incomplete | None = None, taufac: Incomplete | None = None, sstol: Incomplete | None = None, partol: Incomplete | None = None, maxit: Incomplete | None = None, stpb: Incomplete | None = None, stpd: Incomplete | None = None, sclb: Incomplete | None = None, scld: Incomplete | None = None, work: Incomplete | None = None, iwork: Incomplete | None = None, overwrite: bool = False) -> None: ...
    def set_job(self, fit_type: Incomplete | None = None, deriv: Incomplete | None = None, var_calc: Incomplete | None = None, del_init: Incomplete | None = None, restart: Incomplete | None = None) -> None: ...
    def set_iprint(self, init: Incomplete | None = None, so_init: Incomplete | None = None, iter: Incomplete | None = None, so_iter: Incomplete | None = None, iter_step: Incomplete | None = None, final: Incomplete | None = None, so_final: Incomplete | None = None) -> None: ...
    def run(self): ...
    def restart(self, iter: Incomplete | None = None): ...
