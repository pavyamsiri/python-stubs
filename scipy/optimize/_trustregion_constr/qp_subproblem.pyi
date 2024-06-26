from _typeshed import Incomplete

__all__ = [
    "eqp_kktfact",
    "sphere_intersections",
    "box_intersections",
    "box_sphere_intersections",
    "inside_box_boundaries",
    "modified_dogleg",
    "projected_cg",
]

def eqp_kktfact(H, c, A, b): ...
def sphere_intersections(z, d, trust_radius, entire_line: bool = False): ...
def box_intersections(z, d, lb, ub, entire_line: bool = False): ...
def box_sphere_intersections(
    z, d, lb, ub, trust_radius, entire_line: bool = False, extra_info: bool = False
): ...
def inside_box_boundaries(x, lb, ub): ...
def modified_dogleg(A, Y, b, trust_radius, lb, ub): ...
def projected_cg(
    H,
    c,
    Z,
    Y,
    b,
    trust_radius=...,
    lb: Incomplete | None = None,
    ub: Incomplete | None = None,
    tol: Incomplete | None = None,
    max_iter: Incomplete | None = None,
    max_infeasible_iter: Incomplete | None = None,
    return_all: bool = False,
): ...
