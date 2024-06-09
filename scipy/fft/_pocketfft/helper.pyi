from .pypocketfft import good_size as good_size
from collections.abc import Generator

__all__ = ["good_size", "set_workers", "get_workers"]

def set_workers(workers) -> Generator[None, None, None]: ...
def get_workers(): ...
