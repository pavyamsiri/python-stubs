from ._vertex import (
    VertexCacheField as VertexCacheField,
    VertexCacheIndex as VertexCacheIndex,
)
from _typeshed import Incomplete
from collections.abc import Generator

class Complex:
    dim: Incomplete
    domain: Incomplete
    bounds: Incomplete
    symmetry: Incomplete
    sfield: Incomplete
    sfield_args: Incomplete
    min_cons: Incomplete
    g_cons: Incomplete
    g_args: Incomplete
    gen: int
    perm_cycle: int
    H: Incomplete
    V: Incomplete
    V_non_symm: Incomplete
    def __init__(
        self,
        dim,
        domain: Incomplete | None = None,
        sfield: Incomplete | None = None,
        sfield_args=(),
        symmetry: Incomplete | None = None,
        constraints: Incomplete | None = None,
        workers: int = 1,
    ) -> None: ...
    def __call__(self): ...
    def cyclic_product(
        self, bounds, origin, supremum, centroid: bool = True
    ) -> Generator[Incomplete, None, Incomplete]: ...
    origin: Incomplete
    supremum: Incomplete
    cp: Incomplete
    triangulated_vectors: Incomplete
    def triangulate(
        self,
        n: Incomplete | None = None,
        symmetry: Incomplete | None = None,
        centroid: bool = True,
        printout: bool = False,
    ) -> None: ...
    rls: Incomplete
    def refine(self, n: int = 1) -> None: ...
    def refine_all(self, centroids: bool = True) -> None: ...
    def refine_local_space(
        self, origin, supremum, bounds, centroid: int = 1
    ) -> Generator[Incomplete, None, None]: ...
    def refine_star(self, v) -> None: ...
    def split_edge(self, v1, v2): ...
    def vpool(self, origin, supremum): ...
    def vf_to_vv(self, vertices, simplices) -> None: ...
    def connect_vertex_non_symm(self, v_x, near: Incomplete | None = None): ...
    def in_simplex(self, S, v_x, A_j0: Incomplete | None = None): ...
    def deg_simplex(self, S, proj: Incomplete | None = None): ...
