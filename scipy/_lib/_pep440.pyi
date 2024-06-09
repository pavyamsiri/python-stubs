from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['parse', 'Version', 'LegacyVersion', 'InvalidVersion', 'VERSION_PATTERN']

class Infinity:
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __neg__(self): ...

class NegativeInfinity:
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __neg__(self): ...

class _Version(NamedTuple):
    epoch: Incomplete
    release: Incomplete
    dev: Incomplete
    pre: Incomplete
    post: Incomplete
    local: Incomplete

def parse(version): ...

class InvalidVersion(ValueError): ...

class _BaseVersion:
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __ne__(self, other): ...

class LegacyVersion(_BaseVersion):
    def __init__(self, version) -> None: ...
    @property
    def public(self): ...
    @property
    def base_version(self): ...
    @property
    def local(self) -> None: ...
    @property
    def is_prerelease(self): ...
    @property
    def is_postrelease(self): ...

VERSION_PATTERN: str

class Version(_BaseVersion):
    def __init__(self, version) -> None: ...
    @property
    def public(self): ...
    @property
    def base_version(self): ...
    @property
    def local(self): ...
    @property
    def is_prerelease(self): ...
    @property
    def is_postrelease(self): ...