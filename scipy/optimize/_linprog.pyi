from _typeshed import Incomplete

__all__ = ["linprog", "linprog_verbose_callback", "linprog_terse_callback"]

def linprog_verbose_callback(res): ...
def linprog_terse_callback(res) -> None: ...
def linprog(
    c,
    A_ub: Incomplete | None = None,
    b_ub: Incomplete | None = None,
    A_eq: Incomplete | None = None,
    b_eq: Incomplete | None = None,
    bounds=(0, None),
    method: str = "highs",
    callback: Incomplete | None = None,
    options: Incomplete | None = None,
    x0: Incomplete | None = None,
    integrality: Incomplete | None = None,
): ...
