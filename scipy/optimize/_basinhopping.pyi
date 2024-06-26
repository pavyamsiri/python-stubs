from _typeshed import Incomplete

__all__ = ["basinhopping"]

class Storage:
    def __init__(self, minres) -> None: ...
    def update(self, minres): ...
    def get_lowest(self): ...

class BasinHoppingRunner:
    x: Incomplete
    minimizer: Incomplete
    step_taking: Incomplete
    accept_tests: Incomplete
    disp: Incomplete
    nstep: int
    res: Incomplete
    energy: Incomplete
    incumbent_minres: Incomplete
    storage: Incomplete
    def __init__(
        self, x0, minimizer, step_taking, accept_tests, disp: bool = False
    ) -> None: ...
    xtrial: Incomplete
    energy_trial: Incomplete
    accept: Incomplete
    def one_cycle(self): ...
    def print_report(self, energy_trial, accept) -> None: ...

class AdaptiveStepsize:
    takestep: Incomplete
    target_accept_rate: Incomplete
    interval: Incomplete
    factor: Incomplete
    verbose: Incomplete
    nstep: int
    nstep_tot: int
    naccept: int
    def __init__(
        self,
        takestep,
        accept_rate: float = 0.5,
        interval: int = 50,
        factor: float = 0.9,
        verbose: bool = True,
    ) -> None: ...
    def __call__(self, x): ...
    def take_step(self, x): ...
    def report(self, accept, **kwargs) -> None: ...

class RandomDisplacement:
    stepsize: Incomplete
    random_gen: Incomplete
    def __init__(
        self, stepsize: float = 0.5, random_gen: Incomplete | None = None
    ) -> None: ...
    def __call__(self, x): ...

class MinimizerWrapper:
    minimizer: Incomplete
    func: Incomplete
    kwargs: Incomplete
    def __init__(self, minimizer, func: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, x0): ...

class Metropolis:
    beta: Incomplete
    random_gen: Incomplete
    def __init__(self, T, random_gen: Incomplete | None = None) -> None: ...
    def accept_reject(self, res_new, res_old): ...
    def __call__(self, *, res_new, res_old): ...

def basinhopping(
    func,
    x0,
    niter: int = 100,
    T: float = 1.0,
    stepsize: float = 0.5,
    minimizer_kwargs: Incomplete | None = None,
    take_step: Incomplete | None = None,
    accept_test: Incomplete | None = None,
    callback: Incomplete | None = None,
    interval: int = 50,
    disp: bool = False,
    niter_success: Incomplete | None = None,
    seed: Incomplete | None = None,
    *,
    target_accept_rate: float = 0.5,
    stepwise_factor: float = 0.9,
): ...
