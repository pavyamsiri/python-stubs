from ._constraints import Bounds as Bounds, LinearConstraint as LinearConstraint
from ._optimize import OptimizeResult as OptimizeResult
from _typeshed import Incomplete
from scipy._lib._util import VisibleDeprecationWarning as VisibleDeprecationWarning
from scipy.sparse import csc_array as csc_array, issparse as issparse, vstack as vstack

def milp(c, *, integrality: Incomplete | None = None, bounds: Incomplete | None = None, constraints: Incomplete | None = None, options: Incomplete | None = None): ...
