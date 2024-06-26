from _typeshed import Incomplete

class CensoredData:
    def __init__(
        self,
        uncensored: Incomplete | None = None,
        *,
        left: Incomplete | None = None,
        right: Incomplete | None = None,
        interval: Incomplete | None = None,
    ) -> None: ...
    def __sub__(self, other): ...
    def __truediv__(self, other): ...
    def __len__(self) -> int: ...
    def num_censored(self): ...
    @classmethod
    def right_censored(cls, x, censored): ...
    @classmethod
    def left_censored(cls, x, censored): ...
    @classmethod
    def interval_censored(cls, low, high): ...
