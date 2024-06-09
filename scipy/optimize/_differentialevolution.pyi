from _typeshed import Incomplete

__all__ = ['differential_evolution']

def differential_evolution(func, bounds, args=(), strategy: str = 'best1bin', maxiter: int = 1000, popsize: int = 15, tol: float = 0.01, mutation=(0.5, 1), recombination: float = 0.7, seed: Incomplete | None = None, callback: Incomplete | None = None, disp: bool = False, polish: bool = True, init: str = 'latinhypercube', atol: int = 0, updating: str = 'immediate', workers: int = 1, constraints=(), x0: Incomplete | None = None, *, integrality: Incomplete | None = None, vectorized: bool = False): ...

class DifferentialEvolutionSolver:
    mutation_func: Incomplete
    strategy: Incomplete
    callback: Incomplete
    polish: Incomplete
    vectorized: Incomplete
    scale: Incomplete
    dither: Incomplete
    cross_over_probability: Incomplete
    func: Incomplete
    args: Incomplete
    limits: Incomplete
    maxiter: Incomplete
    maxfun: Incomplete
    parameter_count: Incomplete
    random_number_generator: Incomplete
    integrality: Incomplete
    num_population_members: Incomplete
    population_shape: Incomplete
    constraints: Incomplete
    total_constraints: Incomplete
    constraint_violation: Incomplete
    feasible: Incomplete
    disp: Incomplete
    def __init__(self, func, bounds, args=(), strategy: str = 'best1bin', maxiter: int = 1000, popsize: int = 15, tol: float = 0.01, mutation=(0.5, 1), recombination: float = 0.7, seed: Incomplete | None = None, maxfun=..., callback: Incomplete | None = None, disp: bool = False, polish: bool = True, init: str = 'latinhypercube', atol: int = 0, updating: str = 'immediate', workers: int = 1, constraints=(), x0: Incomplete | None = None, *, integrality: Incomplete | None = None, vectorized: bool = False) -> None: ...
    population: Incomplete
    population_energies: Incomplete
    def init_population_lhs(self) -> None: ...
    def init_population_qmc(self, qmc_engine) -> None: ...
    def init_population_random(self) -> None: ...
    def init_population_array(self, init) -> None: ...
    @property
    def x(self): ...
    @property
    def convergence(self): ...
    def converged(self): ...
    def solve(self): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def __next__(self): ...

class _ConstraintWrapper:
    constraint: Incomplete
    fun: Incomplete
    num_constr: Incomplete
    parameter_count: Incomplete
    bounds: Incomplete
    def __init__(self, constraint, x0) -> None: ...
    def __call__(self, x): ...
    def violation(self, x): ...
