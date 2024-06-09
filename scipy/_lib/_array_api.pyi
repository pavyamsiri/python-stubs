from _typeshed import Incomplete
from scipy._lib.array_api_compat import size as size

__all__ = ['array_namespace', '_asarray', 'size']

def array_namespace(*arrays): ...
def _asarray(array, dtype: Incomplete | None = None, order: Incomplete | None = None, copy: Incomplete | None = None, *, xp: Incomplete | None = None, check_finite: bool = False): ...
