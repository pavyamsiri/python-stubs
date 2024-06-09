from _typeshed import Incomplete

__all__ = [
    "multivariate_normal",
    "matrix_normal",
    "dirichlet",
    "dirichlet_multinomial",
    "wishart",
    "invwishart",
    "multinomial",
    "special_ortho_group",
    "ortho_group",
    "random_correlation",
    "unitary_group",
    "multivariate_t",
    "multivariate_hypergeom",
    "random_table",
    "uniform_direction",
    "vonmises_fisher",
]

class _PSD:
    eps: Incomplete
    V: Incomplete
    rank: Incomplete
    U: Incomplete
    log_pdet: Incomplete
    def __init__(
        self,
        M,
        cond: Incomplete | None = None,
        rcond: Incomplete | None = None,
        lower: bool = True,
        check_finite: bool = True,
        allow_singular: bool = True,
    ) -> None: ...
    @property
    def pinv(self): ...

class multi_rv_generic:
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    @property
    def random_state(self): ...
    @random_state.setter
    def random_state(self, seed) -> None: ...

class multi_rv_frozen:
    @property
    def random_state(self): ...
    @random_state.setter
    def random_state(self, seed) -> None: ...

class multivariate_normal_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
        seed: Incomplete | None = None,
    ): ...
    def logpdf(
        self,
        x,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
    ): ...
    def pdf(
        self,
        x,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
    ): ...
    def logcdf(
        self,
        x,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
        maxpts: Incomplete | None = None,
        abseps: float = 1e-05,
        releps: float = 1e-05,
        *,
        lower_limit: Incomplete | None = None,
    ): ...
    def cdf(
        self,
        x,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
        maxpts: Incomplete | None = None,
        abseps: float = 1e-05,
        releps: float = 1e-05,
        *,
        lower_limit: Incomplete | None = None,
    ): ...
    def rvs(
        self,
        mean: Incomplete | None = None,
        cov: int = 1,
        size: int = 1,
        random_state: Incomplete | None = None,
    ): ...
    def entropy(self, mean: Incomplete | None = None, cov: int = 1): ...
    def fit(
        self, x, fix_mean: Incomplete | None = None, fix_cov: Incomplete | None = None
    ): ...

multivariate_normal: Incomplete

class multivariate_normal_frozen(multi_rv_frozen):
    allow_singular: Incomplete
    maxpts: Incomplete
    abseps: Incomplete
    releps: Incomplete
    def __init__(
        self,
        mean: Incomplete | None = None,
        cov: int = 1,
        allow_singular: bool = False,
        seed: Incomplete | None = None,
        maxpts: Incomplete | None = None,
        abseps: float = 1e-05,
        releps: float = 1e-05,
    ) -> None: ...
    @property
    def cov(self): ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def logcdf(self, x, *, lower_limit: Incomplete | None = None): ...
    def cdf(self, x, *, lower_limit: Incomplete | None = None): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...

class matrix_normal_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        mean: Incomplete | None = None,
        rowcov: int = 1,
        colcov: int = 1,
        seed: Incomplete | None = None,
    ): ...
    def logpdf(
        self, X, mean: Incomplete | None = None, rowcov: int = 1, colcov: int = 1
    ): ...
    def pdf(
        self, X, mean: Incomplete | None = None, rowcov: int = 1, colcov: int = 1
    ): ...
    def rvs(
        self,
        mean: Incomplete | None = None,
        rowcov: int = 1,
        colcov: int = 1,
        size: int = 1,
        random_state: Incomplete | None = None,
    ): ...
    def entropy(self, rowcov: int = 1, colcov: int = 1): ...

matrix_normal: Incomplete

class matrix_normal_frozen(multi_rv_frozen):
    rowpsd: Incomplete
    colpsd: Incomplete
    def __init__(
        self,
        mean: Incomplete | None = None,
        rowcov: int = 1,
        colcov: int = 1,
        seed: Incomplete | None = None,
    ) -> None: ...
    def logpdf(self, X): ...
    def pdf(self, X): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...

class dirichlet_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(self, alpha, seed: Incomplete | None = None): ...
    def logpdf(self, x, alpha): ...
    def pdf(self, x, alpha): ...
    def mean(self, alpha): ...
    def var(self, alpha): ...
    def cov(self, alpha): ...
    def entropy(self, alpha): ...
    def rvs(self, alpha, size: int = 1, random_state: Incomplete | None = None): ...

dirichlet: Incomplete

class dirichlet_frozen(multi_rv_frozen):
    alpha: Incomplete
    def __init__(self, alpha, seed: Incomplete | None = None) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def mean(self): ...
    def var(self): ...
    def cov(self): ...
    def entropy(self): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class wishart_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        df: Incomplete | None = None,
        scale: Incomplete | None = None,
        seed: Incomplete | None = None,
    ): ...
    def logpdf(self, x, df, scale): ...
    def pdf(self, x, df, scale): ...
    def mean(self, df, scale): ...
    def mode(self, df, scale): ...
    def var(self, df, scale): ...
    def rvs(self, df, scale, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self, df, scale): ...

wishart: Incomplete

class wishart_frozen(multi_rv_frozen):
    def __init__(self, df, scale, seed: Incomplete | None = None) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def mean(self): ...
    def mode(self): ...
    def var(self): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...

class invwishart_gen(wishart_gen):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        df: Incomplete | None = None,
        scale: Incomplete | None = None,
        seed: Incomplete | None = None,
    ): ...
    def logpdf(self, x, df, scale): ...
    def pdf(self, x, df, scale): ...
    def mean(self, df, scale): ...
    def mode(self, df, scale): ...
    def var(self, df, scale): ...
    def rvs(self, df, scale, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self, df, scale): ...

invwishart: Incomplete

class invwishart_frozen(multi_rv_frozen):
    C: Incomplete
    log_det_scale: Incomplete
    def __init__(self, df, scale, seed: Incomplete | None = None) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def mean(self): ...
    def mode(self): ...
    def var(self): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...

class multinomial_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(self, n, p, seed: Incomplete | None = None): ...
    def logpmf(self, x, n, p): ...
    def pmf(self, x, n, p): ...
    def mean(self, n, p): ...
    def cov(self, n, p): ...
    def entropy(self, n, p): ...
    def rvs(
        self,
        n,
        p,
        size: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...

multinomial: Incomplete

class multinomial_frozen(multi_rv_frozen):
    def __init__(self, n, p, seed: Incomplete | None = None) -> None: ...
    def logpmf(self, x): ...
    def pmf(self, x): ...
    def mean(self): ...
    def cov(self): ...
    def entropy(self): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class special_ortho_group_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ): ...
    def rvs(self, dim, size: int = 1, random_state: Incomplete | None = None): ...

special_ortho_group: Incomplete

class special_ortho_group_frozen(multi_rv_frozen):
    dim: Incomplete
    def __init__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ) -> None: ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class ortho_group_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ): ...
    def rvs(self, dim, size: int = 1, random_state: Incomplete | None = None): ...

ortho_group: Incomplete

class ortho_group_frozen(multi_rv_frozen):
    dim: Incomplete
    def __init__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ) -> None: ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class random_correlation_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        eigs,
        seed: Incomplete | None = None,
        tol: float = 1e-13,
        diag_tol: float = 1e-07,
    ): ...
    def rvs(
        self,
        eigs,
        random_state: Incomplete | None = None,
        tol: float = 1e-13,
        diag_tol: float = 1e-07,
    ): ...

random_correlation: Incomplete

class random_correlation_frozen(multi_rv_frozen):
    tol: Incomplete
    diag_tol: Incomplete
    def __init__(
        self,
        eigs,
        seed: Incomplete | None = None,
        tol: float = 1e-13,
        diag_tol: float = 1e-07,
    ) -> None: ...
    def rvs(self, random_state: Incomplete | None = None): ...

class unitary_group_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ): ...
    def rvs(self, dim, size: int = 1, random_state: Incomplete | None = None): ...

unitary_group: Incomplete

class unitary_group_frozen(multi_rv_frozen):
    dim: Incomplete
    def __init__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ) -> None: ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class multivariate_t_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        loc: Incomplete | None = None,
        shape: int = 1,
        df: int = 1,
        allow_singular: bool = False,
        seed: Incomplete | None = None,
    ): ...
    def pdf(
        self,
        x,
        loc: Incomplete | None = None,
        shape: int = 1,
        df: int = 1,
        allow_singular: bool = False,
    ): ...
    def logpdf(self, x, loc: Incomplete | None = None, shape: int = 1, df: int = 1): ...
    def cdf(
        self,
        x,
        loc: Incomplete | None = None,
        shape: int = 1,
        df: int = 1,
        allow_singular: bool = False,
        *,
        maxpts: Incomplete | None = None,
        lower_limit: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...
    def entropy(self, loc: Incomplete | None = None, shape: int = 1, df: int = 1): ...
    def rvs(
        self,
        loc: Incomplete | None = None,
        shape: int = 1,
        df: int = 1,
        size: int = 1,
        random_state: Incomplete | None = None,
    ): ...

class multivariate_t_frozen(multi_rv_frozen):
    shape_info: Incomplete
    def __init__(
        self,
        loc: Incomplete | None = None,
        shape: int = 1,
        df: int = 1,
        allow_singular: bool = False,
        seed: Incomplete | None = None,
    ) -> None: ...
    def logpdf(self, x): ...
    def cdf(
        self,
        x,
        *,
        maxpts: Incomplete | None = None,
        lower_limit: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...
    def pdf(self, x): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...

multivariate_t: Incomplete

class multivariate_hypergeom_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(self, m, n, seed: Incomplete | None = None): ...
    def logpmf(self, x, m, n): ...
    def pmf(self, x, m, n): ...
    def mean(self, m, n): ...
    def var(self, m, n): ...
    def cov(self, m, n): ...
    def rvs(
        self,
        m,
        n,
        size: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...

multivariate_hypergeom: Incomplete

class multivariate_hypergeom_frozen(multi_rv_frozen):
    def __init__(self, m, n, seed: Incomplete | None = None) -> None: ...
    def logpmf(self, x): ...
    def pmf(self, x): ...
    def mean(self): ...
    def var(self): ...
    def cov(self): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...

class random_table_gen(multi_rv_generic):
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(self, row, col, *, seed: Incomplete | None = None): ...
    def logpmf(self, x, row, col): ...
    def pmf(self, x, row, col): ...
    def mean(self, row, col): ...
    def rvs(
        self,
        row,
        col,
        *,
        size: Incomplete | None = None,
        method: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...

random_table: Incomplete

class random_table_frozen(multi_rv_frozen):
    def __init__(self, row, col, *, seed: Incomplete | None = None) -> None: ...
    def logpmf(self, x): ...
    def pmf(self, x): ...
    def mean(self): ...
    def rvs(
        self,
        size: Incomplete | None = None,
        method: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...

class uniform_direction_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ): ...
    def rvs(
        self,
        dim,
        size: Incomplete | None = None,
        random_state: Incomplete | None = None,
    ): ...

uniform_direction: Incomplete

class uniform_direction_frozen(multi_rv_frozen):
    dim: Incomplete
    def __init__(
        self, dim: Incomplete | None = None, seed: Incomplete | None = None
    ) -> None: ...
    def rvs(
        self, size: Incomplete | None = None, random_state: Incomplete | None = None
    ): ...

class dirichlet_multinomial_gen(multi_rv_generic):
    __doc__: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(self, alpha, n, seed: Incomplete | None = None): ...
    def logpmf(self, x, alpha, n): ...
    def pmf(self, x, alpha, n): ...
    def mean(self, alpha, n): ...
    def var(self, alpha, n): ...
    def cov(self, alpha, n): ...

dirichlet_multinomial: Incomplete

class dirichlet_multinomial_frozen(multi_rv_frozen):
    alpha: Incomplete
    n: Incomplete
    def __init__(self, alpha, n, seed: Incomplete | None = None) -> None: ...
    def logpmf(self, x): ...
    def pmf(self, x): ...
    def mean(self): ...
    def var(self): ...
    def cov(self): ...

class vonmises_fisher_gen(multi_rv_generic):
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def __call__(
        self,
        mu: Incomplete | None = None,
        kappa: int = 1,
        seed: Incomplete | None = None,
    ): ...
    def logpdf(self, x, mu: Incomplete | None = None, kappa: int = 1): ...
    def pdf(self, x, mu: Incomplete | None = None, kappa: int = 1): ...
    def rvs(
        self,
        mu: Incomplete | None = None,
        kappa: int = 1,
        size: int = 1,
        random_state: Incomplete | None = None,
    ): ...
    def entropy(self, mu: Incomplete | None = None, kappa: int = 1): ...
    def fit(self, x): ...

vonmises_fisher: Incomplete

class vonmises_fisher_frozen(multi_rv_frozen):
    def __init__(
        self,
        mu: Incomplete | None = None,
        kappa: int = 1,
        seed: Incomplete | None = None,
    ) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def rvs(self, size: int = 1, random_state: Incomplete | None = None): ...
    def entropy(self): ...
