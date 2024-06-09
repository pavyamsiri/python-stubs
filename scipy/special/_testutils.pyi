from _typeshed import Incomplete

__all__ = ['with_special_errors', 'assert_func_equal', 'FuncData']

class MissingModule:
    name: Incomplete
    def __init__(self, name) -> None: ...

def with_special_errors(func): ...
def assert_func_equal(func, results, points, rtol: Incomplete | None = None, atol: Incomplete | None = None, param_filter: Incomplete | None = None, knownfailure: Incomplete | None = None, vectorized: bool = True, dtype: Incomplete | None = None, nan_ok: bool = False, ignore_inf_sign: bool = False, distinguish_nan_and_inf: bool = True) -> None: ...

class FuncData:
    func: Incomplete
    data: Incomplete
    dataname: Incomplete
    param_columns: Incomplete
    result_columns: Incomplete
    result_func: Incomplete
    rtol: Incomplete
    atol: Incomplete
    param_filter: Incomplete
    knownfailure: Incomplete
    nan_ok: Incomplete
    vectorized: Incomplete
    ignore_inf_sign: Incomplete
    distinguish_nan_and_inf: Incomplete
    def __init__(self, func, data, param_columns, result_columns: Incomplete | None = None, result_func: Incomplete | None = None, rtol: Incomplete | None = None, atol: Incomplete | None = None, param_filter: Incomplete | None = None, knownfailure: Incomplete | None = None, dataname: Incomplete | None = None, nan_ok: bool = False, vectorized: bool = True, ignore_inf_sign: bool = False, distinguish_nan_and_inf: bool = True) -> None: ...
    def get_tolerances(self, dtype): ...
    def check(self, data: Incomplete | None = None, dtype: Incomplete | None = None, dtypes: Incomplete | None = None): ...
