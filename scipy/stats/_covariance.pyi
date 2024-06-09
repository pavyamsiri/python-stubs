from _typeshed import Incomplete

__all__ = ['Covariance']

class Covariance:
    def __init__(self) -> None: ...
    @staticmethod
    def from_diagonal(diagonal): ...
    @staticmethod
    def from_precision(precision, covariance: Incomplete | None = None): ...
    @staticmethod
    def from_cholesky(cholesky): ...
    @staticmethod
    def from_eigendecomposition(eigendecomposition): ...
    def whiten(self, x): ...
    def colorize(self, x): ...
    @property
    def log_pdet(self): ...
    @property
    def rank(self): ...
    @property
    def covariance(self): ...
    @property
    def shape(self): ...

class CovViaPrecision(Covariance):
    def __init__(self, precision, covariance: Incomplete | None = None) -> None: ...

class CovViaDiagonal(Covariance):
    def __init__(self, diagonal) -> None: ...

class CovViaCholesky(Covariance):
    def __init__(self, cholesky) -> None: ...

class CovViaEigendecomposition(Covariance):
    def __init__(self, eigendecomposition) -> None: ...

class CovViaPSD(Covariance):
    def __init__(self, psd) -> None: ...
