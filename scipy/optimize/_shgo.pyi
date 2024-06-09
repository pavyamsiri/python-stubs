from _typeshed import Incomplete

__all__ = ["shgo"]

def shgo(
    func,
    bounds,
    args=(),
    constraints: Incomplete | None = None,
    n: int = 100,
    iters: int = 1,
    callback: Incomplete | None = None,
    minimizer_kwargs: Incomplete | None = None,
    options: Incomplete | None = None,
    sampling_method: str = "simplicial",
    *,
    workers: int = 1,
): ...

class SHGO:
    func: Incomplete
    bounds: Incomplete
    args: Incomplete
    callback: Incomplete
    dim: Incomplete
    constraints: Incomplete
    min_cons: Incomplete
    g_cons: Incomplete
    g_args: Incomplete
    minimizer_kwargs: Incomplete
    f_min_true: Incomplete
    minimize_every_iter: bool
    maxiter: Incomplete
    maxfev: Incomplete
    maxev: Incomplete
    maxtime: Incomplete
    minhgrd: Incomplete
    symmetry: Incomplete
    infty_cons_sampl: bool
    local_iter: bool
    disp: bool
    min_solver_args: Incomplete
    stop_global: bool
    break_routine: bool
    iters: Incomplete
    iters_done: int
    n: Incomplete
    nc: int
    n_prc: int
    n_sampled: int
    fn: int
    hgr: int
    qhull_incremental: bool
    HC: Incomplete
    iterate_complex: Incomplete
    sampling_method: Incomplete
    qmc_engine: Incomplete
    sampling: Incomplete
    sampling_function: Incomplete
    stop_l_iter: bool
    stop_complex_iter: bool
    minimizer_pool: Incomplete
    LMC: Incomplete
    res: Incomplete
    def __init__(
        self,
        func,
        bounds,
        args=(),
        constraints: Incomplete | None = None,
        n: Incomplete | None = None,
        iters: Incomplete | None = None,
        callback: Incomplete | None = None,
        minimizer_kwargs: Incomplete | None = None,
        options: Incomplete | None = None,
        sampling_method: str = "simplicial",
        workers: int = 1,
    ) -> None: ...
    init: Incomplete
    f_tol: Incomplete
    def init_options(self, options) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def iterate_all(self) -> None: ...
    f_lowest: Incomplete
    x_lowest: Incomplete
    def find_minima(self) -> None: ...
    def find_lowest_vertex(self) -> None: ...
    def finite_iterations(self): ...
    def finite_fev(self): ...
    def finite_ev(self) -> None: ...
    def finite_time(self) -> None: ...
    def finite_precision(self): ...
    hgrd: Incomplete
    def finite_homology_growth(self): ...
    def stopping_criteria(self): ...
    def iterate(self) -> None: ...
    def iterate_hypercube(self) -> None: ...
    Ind_sorted: Incomplete
    Tri: Incomplete
    points: Incomplete
    def iterate_delaunay(self) -> None: ...
    minimizer_pool_F: Incomplete
    X_min: Incomplete
    X_min_cache: Incomplete
    def minimizers(self): ...
    def minimise_pool(self, force_iter: bool = False) -> None: ...
    ind_f_min: Incomplete
    def sort_min_pool(self) -> None: ...
    def trim_min_pool(self, trim_ind) -> None: ...
    Y: Incomplete
    Z: Incomplete
    Ss: Incomplete
    def g_topograph(self, x_min, X_min): ...
    def construct_lcb_simplicial(self, v_min): ...
    def construct_lcb_delaunay(self, v_min, ind: Incomplete | None = None): ...
    def minimize(self, x_min, ind: Incomplete | None = None): ...
    def sort_result(self): ...
    def fail_routine(self, mes: str = "Failed to converge") -> None: ...
    C: Incomplete
    def sampled_surface(self, infty_cons_sampl: bool = False) -> None: ...
    def sampling_custom(self, n, dim): ...
    def sampling_subspace(self) -> None: ...
    Xs: Incomplete
    def sorted_samples(self): ...
    def delaunay_triangulation(self, n_prc: int = 0): ...

class LMap:
    v: Incomplete
    x_l: Incomplete
    lres: Incomplete
    f_min: Incomplete
    lbounds: Incomplete
    def __init__(self, v) -> None: ...

class LMapCache:
    cache: Incomplete
    v_maps: Incomplete
    xl_maps: Incomplete
    xl_maps_set: Incomplete
    f_maps: Incomplete
    lbound_maps: Incomplete
    size: int
    def __init__(self) -> None: ...
    def __getitem__(self, v): ...
    def add_res(self, v, lres, bounds: Incomplete | None = None) -> None: ...
    def sort_cache_result(self): ...
