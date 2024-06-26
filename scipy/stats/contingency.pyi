from ._crosstab import crosstab as crosstab
from ._odds_ratio import odds_ratio as odds_ratio
from ._relative_risk import relative_risk as relative_risk
from _typeshed import Incomplete

__all__ = [
    "margins",
    "expected_freq",
    "chi2_contingency",
    "crosstab",
    "association",
    "relative_risk",
    "odds_ratio",
]

def margins(a): ...
def expected_freq(observed): ...
def chi2_contingency(
    observed, correction: bool = True, lambda_: Incomplete | None = None
): ...
def association(
    observed,
    method: str = "cramer",
    correction: bool = False,
    lambda_: Incomplete | None = None,
): ...
