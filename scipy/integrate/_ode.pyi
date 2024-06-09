from _typeshed import Incomplete

__all__ = ["ode", "complex_ode"]

class ode:
    stiff: int
    f: Incomplete
    jac: Incomplete
    f_params: Incomplete
    jac_params: Incomplete
    def __init__(self, f, jac: Incomplete | None = None) -> None: ...
    @property
    def y(self): ...
    t: Incomplete
    def set_initial_value(self, y, t: float = 0.0): ...
    def set_integrator(self, name, **integrator_params): ...
    def integrate(self, t, step: bool = False, relax: bool = False): ...
    def successful(self): ...
    def get_return_code(self): ...
    def set_f_params(self, *args): ...
    def set_jac_params(self, *args): ...
    def set_solout(self, solout) -> None: ...

class complex_ode(ode):
    cf: Incomplete
    cjac: Incomplete
    def __init__(self, f, jac: Incomplete | None = None) -> None: ...
    @property
    def y(self): ...
    def set_integrator(self, name, **integrator_params): ...
    tmp: Incomplete
    def set_initial_value(self, y, t: float = 0.0): ...
    def integrate(self, t, step: bool = False, relax: bool = False): ...
    def set_solout(self, solout) -> None: ...

class IntegratorConcurrencyError(RuntimeError):
    def __init__(self, name) -> None: ...

class IntegratorBase:
    runner: Incomplete
    success: Incomplete
    istate: Incomplete
    supports_run_relax: Incomplete
    supports_step: Incomplete
    supports_solout: bool
    integrator_classes: Incomplete
    scalar = float
    handle: Incomplete
    def acquire_new_handle(self) -> None: ...
    def check_handle(self) -> None: ...
    def reset(self, n, has_jac) -> None: ...
    def run(self, f, jac, y0, t0, t1, f_params, jac_params) -> None: ...
    def step(self, f, jac, y0, t0, t1, f_params, jac_params) -> None: ...
    def run_relax(self, f, jac, y0, t0, t1, f_params, jac_params) -> None: ...

class vode(IntegratorBase):
    runner: Incomplete
    messages: Incomplete
    supports_run_relax: int
    supports_step: int
    active_global_handle: int
    meth: int
    with_jacobian: Incomplete
    rtol: Incomplete
    atol: Incomplete
    mu: Incomplete
    ml: Incomplete
    order: Incomplete
    nsteps: Incomplete
    max_step: Incomplete
    min_step: Incomplete
    first_step: Incomplete
    success: int
    initialized: bool
    def __init__(
        self,
        method: str = "adams",
        with_jacobian: bool = False,
        rtol: float = 1e-06,
        atol: float = 1e-12,
        lband: Incomplete | None = None,
        uband: Incomplete | None = None,
        order: int = 12,
        nsteps: int = 500,
        max_step: float = 0.0,
        min_step: float = 0.0,
        first_step: float = 0.0,
    ) -> None: ...
    rwork: Incomplete
    iwork: Incomplete
    call_args: Incomplete
    def reset(self, n, has_jac) -> None: ...
    istate: Incomplete
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): ...
    def step(self, *args): ...
    def run_relax(self, *args): ...

class zvode(vode):
    runner: Incomplete
    supports_run_relax: int
    supports_step: int
    scalar = complex
    active_global_handle: int
    zwork: Incomplete
    rwork: Incomplete
    iwork: Incomplete
    call_args: Incomplete
    success: int
    initialized: bool
    def reset(self, n, has_jac) -> None: ...

class dopri5(IntegratorBase):
    runner: Incomplete
    name: str
    supports_solout: bool
    messages: Incomplete
    rtol: Incomplete
    atol: Incomplete
    nsteps: Incomplete
    max_step: Incomplete
    first_step: Incomplete
    safety: Incomplete
    ifactor: Incomplete
    dfactor: Incomplete
    beta: Incomplete
    verbosity: Incomplete
    success: int
    def __init__(
        self,
        rtol: float = 1e-06,
        atol: float = 1e-12,
        nsteps: int = 500,
        max_step: float = 0.0,
        first_step: float = 0.0,
        safety: float = 0.9,
        ifactor: float = 10.0,
        dfactor: float = 0.2,
        beta: float = 0.0,
        method: Incomplete | None = None,
        verbosity: int = -1,
    ) -> None: ...
    solout: Incomplete
    solout_cmplx: Incomplete
    iout: int
    def set_solout(self, solout, complex: bool = False) -> None: ...
    work: Incomplete
    iwork: Incomplete
    call_args: Incomplete
    def reset(self, n, has_jac) -> None: ...
    istate: Incomplete
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): ...

class dop853(dopri5):
    runner: Incomplete
    name: str
    def __init__(
        self,
        rtol: float = 1e-06,
        atol: float = 1e-12,
        nsteps: int = 500,
        max_step: float = 0.0,
        first_step: float = 0.0,
        safety: float = 0.9,
        ifactor: float = 6.0,
        dfactor: float = 0.3,
        beta: float = 0.0,
        method: Incomplete | None = None,
        verbosity: int = -1,
    ) -> None: ...
    work: Incomplete
    iwork: Incomplete
    call_args: Incomplete
    success: int
    def reset(self, n, has_jac) -> None: ...

class lsoda(IntegratorBase):
    runner: Incomplete
    active_global_handle: int
    messages: Incomplete
    with_jacobian: Incomplete
    rtol: Incomplete
    atol: Incomplete
    mu: Incomplete
    ml: Incomplete
    max_order_ns: Incomplete
    max_order_s: Incomplete
    nsteps: Incomplete
    max_step: Incomplete
    min_step: Incomplete
    first_step: Incomplete
    ixpr: Incomplete
    max_hnil: Incomplete
    success: int
    initialized: bool
    def __init__(
        self,
        with_jacobian: bool = False,
        rtol: float = 1e-06,
        atol: float = 1e-12,
        lband: Incomplete | None = None,
        uband: Incomplete | None = None,
        nsteps: int = 500,
        max_step: float = 0.0,
        min_step: float = 0.0,
        first_step: float = 0.0,
        ixpr: int = 0,
        max_hnil: int = 0,
        max_order_ns: int = 12,
        max_order_s: int = 5,
        method: Incomplete | None = None,
    ) -> None: ...
    rwork: Incomplete
    iwork: Incomplete
    call_args: Incomplete
    def reset(self, n, has_jac) -> None: ...
    istate: Incomplete
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): ...
    def step(self, *args): ...
    def run_relax(self, *args): ...
