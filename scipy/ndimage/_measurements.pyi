from _typeshed import Incomplete

__all__ = [
    "label",
    "find_objects",
    "labeled_comprehension",
    "sum",
    "mean",
    "variance",
    "standard_deviation",
    "minimum",
    "maximum",
    "median",
    "minimum_position",
    "maximum_position",
    "extrema",
    "center_of_mass",
    "histogram",
    "watershed_ift",
    "sum_labels",
    "value_indices",
]

def label(
    input, structure: Incomplete | None = None, output: Incomplete | None = None
): ...
def find_objects(input, max_label: int = 0): ...
def value_indices(arr, *, ignore_value: Incomplete | None = None): ...
def labeled_comprehension(
    input, labels, index, func, out_dtype, default, pass_positions: bool = False
): ...
def sum(input, labels: Incomplete | None = None, index: Incomplete | None = None): ...
def sum_labels(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def mean(input, labels: Incomplete | None = None, index: Incomplete | None = None): ...
def variance(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def standard_deviation(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def minimum(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def maximum(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def median(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def minimum_position(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def maximum_position(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def extrema(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def center_of_mass(
    input, labels: Incomplete | None = None, index: Incomplete | None = None
): ...
def histogram(
    input,
    min,
    max,
    bins,
    labels: Incomplete | None = None,
    index: Incomplete | None = None,
): ...
def watershed_ift(
    input,
    markers,
    structure: Incomplete | None = None,
    output: Incomplete | None = None,
): ...
