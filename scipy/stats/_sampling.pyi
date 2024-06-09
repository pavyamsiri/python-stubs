from _typeshed import Incomplete

__all__ = ["FastGeneratorInversion", "RatioUniforms"]

class CustomDistPINV:
    def __init__(self, pdf, args) -> None: ...
    def pdf(self, x): ...

class FastGeneratorInversion:
    def __init__(
        self,
        dist,
        *,
        domain: Incomplete | None = None,
        ignore_shape_range: bool = False,
        random_state: Incomplete | None = None,
    ) -> None: ...
    @property
    def random_state(self): ...
    @random_state.setter
    def random_state(self, random_state) -> None: ...
    @property
    def loc(self): ...
    @loc.setter
    def loc(self, loc) -> None: ...
    @property
    def scale(self): ...
    @scale.setter
    def scale(self, scale) -> None: ...
    def rvs(self, size: Incomplete | None = None): ...
    def ppf(self, q): ...
    def qrvs(
        self,
        size: Incomplete | None = None,
        d: Incomplete | None = None,
        qmc_engine: Incomplete | None = None,
    ): ...
    def evaluate_error(
        self,
        size: int = 100000,
        random_state: Incomplete | None = None,
        x_error: bool = False,
    ): ...
    def support(self): ...

class RatioUniforms:
    def __init__(
        self,
        pdf,
        *,
        umax,
        vmin,
        vmax,
        c: int = 0,
        random_state: Incomplete | None = None,
    ) -> None: ...
    def rvs(self, size: int = 1): ...
