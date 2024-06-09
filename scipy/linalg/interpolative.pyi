from _typeshed import Incomplete

__all__ = [
    "estimate_rank",
    "estimate_spectral_norm",
    "estimate_spectral_norm_diff",
    "id_to_svd",
    "interp_decomp",
    "rand",
    "reconstruct_interp_matrix",
    "reconstruct_matrix_from_id",
    "reconstruct_skel_matrix",
    "seed",
    "svd",
]

def seed(seed: Incomplete | None = None) -> None: ...
def rand(*shape): ...
def interp_decomp(A, eps_or_k, rand: bool = True): ...
def reconstruct_matrix_from_id(B, idx, proj): ...
def reconstruct_interp_matrix(idx, proj): ...
def reconstruct_skel_matrix(A, k, idx): ...
def id_to_svd(B, idx, proj): ...
def estimate_spectral_norm(A, its: int = 20): ...
def estimate_spectral_norm_diff(A, B, its: int = 20): ...
def svd(A, eps_or_k, rand: bool = True): ...
def estimate_rank(A, eps): ...
