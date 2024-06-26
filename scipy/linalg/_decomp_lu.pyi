__all__ = ["lu", "lu_solve", "lu_factor"]

def lu_factor(a, overwrite_a: bool = False, check_finite: bool = True): ...
def lu_solve(
    lu_and_piv, b, trans: int = 0, overwrite_b: bool = False, check_finite: bool = True
): ...
def lu(
    a,
    permute_l: bool = False,
    overwrite_a: bool = False,
    check_finite: bool = True,
    p_indices: bool = False,
): ...
