class _ScipyBackend:
    __ua_domain__: str
    @staticmethod
    def __ua_function__(method, args, kwargs): ...

def set_global_backend(backend, coerce: bool = False, only: bool = False, try_last: bool = False) -> None: ...
def register_backend(backend) -> None: ...
def set_backend(backend, coerce: bool = False, only: bool = False): ...
def skip_backend(backend): ...
