import numpy as np

__all__ = ["entropy", "differential_entropy"]

def entropy(
    pk: np.typing.ArrayLike,
    qk: np.typing.ArrayLike | None = None,
    base: float | None = None,
    axis: int = 0,
) -> np.number | np.ndarray: ...
def differential_entropy(
    values: np.typing.ArrayLike,
    *,
    window_length: int | None = None,
    base: float | None = None,
    axis: int = 0,
    method: str = "auto",
) -> np.number | np.ndarray: ...
