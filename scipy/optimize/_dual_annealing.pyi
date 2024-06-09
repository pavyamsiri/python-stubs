from _typeshed import Incomplete

__all__ = ["dual_annealing"]

class VisitingDistribution:
    TAIL_LIMIT: float
    MIN_VISIT_BOUND: float
    rand_gen: Incomplete
    lower: Incomplete
    upper: Incomplete
    bound_range: Incomplete
    def __init__(self, lb, ub, visiting_param, rand_gen) -> None: ...
    def visiting(self, x, step, temperature): ...
    def visit_fn(self, temperature, dim): ...

class EnergyState:
    MAX_REINIT_COUNT: int
    ebest: Incomplete
    current_energy: Incomplete
    current_location: Incomplete
    xbest: Incomplete
    lower: Incomplete
    upper: Incomplete
    callback: Incomplete
    def __init__(self, lower, upper, callback: Incomplete | None = None) -> None: ...
    def reset(self, func_wrapper, rand_gen, x0: Incomplete | None = None) -> None: ...
    def update_best(self, e, x, context): ...
    def update_current(self, e, x) -> None: ...

class StrategyChain:
    emin: Incomplete
    xmin: Incomplete
    energy_state: Incomplete
    acceptance_param: Incomplete
    visit_dist: Incomplete
    func_wrapper: Incomplete
    minimizer_wrapper: Incomplete
    not_improved_idx: int
    not_improved_max_idx: int
    temperature_step: int
    K: Incomplete
    def __init__(
        self,
        acceptance_param,
        visit_dist,
        func_wrapper,
        minimizer_wrapper,
        rand_gen,
        energy_state,
    ) -> None: ...
    def accept_reject(self, j, e, x_visit) -> None: ...
    energy_state_improved: bool
    def run(self, step, temperature): ...
    def local_search(self): ...

class ObjectiveFunWrapper:
    func: Incomplete
    args: Incomplete
    nfev: int
    ngev: int
    nhev: int
    maxfun: Incomplete
    def __init__(self, func, maxfun: float = 10000000.0, *args) -> None: ...
    def fun(self, x): ...

class LocalSearchWrapper:
    LS_MAXITER_RATIO: int
    LS_MAXITER_MIN: int
    LS_MAXITER_MAX: int
    func_wrapper: Incomplete
    kwargs: Incomplete
    jac: Incomplete
    minimizer: Incomplete
    lower: Incomplete
    upper: Incomplete
    def __init__(self, search_bounds, func_wrapper, *args, **kwargs) -> None: ...
    def local_search(self, x, e): ...

def dual_annealing(
    func,
    bounds,
    args=(),
    maxiter: int = 1000,
    minimizer_kwargs: Incomplete | None = None,
    initial_temp: float = 5230.0,
    restart_temp_ratio: float = 2e-05,
    visit: float = 2.62,
    accept: float = -5.0,
    maxfun: float = 10000000.0,
    seed: Incomplete | None = None,
    no_local_search: bool = False,
    callback: Incomplete | None = None,
    x0: Incomplete | None = None,
): ...
