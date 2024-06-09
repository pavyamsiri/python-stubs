__all__ = ['central_diff_weights', 'derivative', 'ascent', 'face', 'electrocardiogram']

def central_diff_weights(Np, ndiv: int = 1): ...
def derivative(func, x0, dx: float = 1.0, n: int = 1, args=(), order: int = 3): ...
def ascent(): ...
def face(gray: bool = False): ...
def electrocardiogram(): ...