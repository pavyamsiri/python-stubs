from _typeshed import Incomplete
from scipy._lib._disjoint_set import DisjointSet as DisjointSet

__all__ = [
    "ClusterNode",
    "DisjointSet",
    "average",
    "centroid",
    "complete",
    "cophenet",
    "correspond",
    "cut_tree",
    "dendrogram",
    "fcluster",
    "fclusterdata",
    "from_mlab_linkage",
    "inconsistent",
    "is_isomorphic",
    "is_monotonic",
    "is_valid_im",
    "is_valid_linkage",
    "leaders",
    "leaves_list",
    "linkage",
    "maxRstat",
    "maxdists",
    "maxinconsts",
    "median",
    "num_obs_linkage",
    "optimal_leaf_ordering",
    "set_link_color_palette",
    "single",
    "to_mlab_linkage",
    "to_tree",
    "ward",
    "weighted",
]

class ClusterWarning(UserWarning): ...

def single(y): ...
def complete(y): ...
def average(y): ...
def weighted(y): ...
def centroid(y): ...
def median(y): ...
def ward(y): ...
def linkage(
    y, method: str = "single", metric: str = "euclidean", optimal_ordering: bool = False
): ...

class ClusterNode:
    id: Incomplete
    left: Incomplete
    right: Incomplete
    dist: Incomplete
    count: Incomplete
    def __init__(
        self,
        id,
        left: Incomplete | None = None,
        right: Incomplete | None = None,
        dist: int = 0,
        count: int = 1,
    ) -> None: ...
    def __lt__(self, node): ...
    def __gt__(self, node): ...
    def __eq__(self, node): ...
    def get_id(self): ...
    def get_count(self): ...
    def get_left(self): ...
    def get_right(self): ...
    def is_leaf(self): ...
    def pre_order(self, func=...): ...

def cut_tree(
    Z, n_clusters: Incomplete | None = None, height: Incomplete | None = None
): ...
def to_tree(Z, rd: bool = False): ...
def optimal_leaf_ordering(Z, y, metric: str = "euclidean"): ...
def cophenet(Z, Y: Incomplete | None = None): ...
def inconsistent(Z, d: int = 2): ...
def from_mlab_linkage(Z): ...
def to_mlab_linkage(Z): ...
def is_monotonic(Z): ...
def is_valid_im(
    R, warning: bool = False, throw: bool = False, name: Incomplete | None = None
): ...
def is_valid_linkage(
    Z, warning: bool = False, throw: bool = False, name: Incomplete | None = None
): ...
def num_obs_linkage(Z): ...
def correspond(Z, Y): ...
def fcluster(
    Z,
    t,
    criterion: str = "inconsistent",
    depth: int = 2,
    R: Incomplete | None = None,
    monocrit: Incomplete | None = None,
): ...
def fclusterdata(
    X,
    t,
    criterion: str = "inconsistent",
    metric: str = "euclidean",
    depth: int = 2,
    method: str = "single",
    R: Incomplete | None = None,
): ...
def leaves_list(Z): ...
def set_link_color_palette(palette) -> None: ...
def dendrogram(
    Z,
    p: int = 30,
    truncate_mode: Incomplete | None = None,
    color_threshold: Incomplete | None = None,
    get_leaves: bool = True,
    orientation: str = "top",
    labels: Incomplete | None = None,
    count_sort: bool = False,
    distance_sort: bool = False,
    show_leaf_counts: bool = True,
    no_plot: bool = False,
    no_labels: bool = False,
    leaf_font_size: Incomplete | None = None,
    leaf_rotation: Incomplete | None = None,
    leaf_label_func: Incomplete | None = None,
    show_contracted: bool = False,
    link_color_func: Incomplete | None = None,
    ax: Incomplete | None = None,
    above_threshold_color: str = "C0",
): ...
def is_isomorphic(T1, T2): ...
def maxdists(Z): ...
def maxinconsts(Z, R): ...
def maxRstat(Z, R, i): ...
def leaders(Z, T): ...
