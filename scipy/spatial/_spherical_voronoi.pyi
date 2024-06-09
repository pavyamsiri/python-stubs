from _typeshed import Incomplete

__all__ = ['SphericalVoronoi']

class SphericalVoronoi:
    radius: Incomplete
    points: Incomplete
    center: Incomplete
    def __init__(self, points, radius: int = 1, center: Incomplete | None = None, threshold: float = 1e-06) -> None: ...
    def sort_vertices_of_regions(self) -> None: ...
    def calculate_areas(self): ...
