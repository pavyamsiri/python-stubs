from _typeshed import Incomplete

__all__ = ['boxcar', 'triang', 'parzen', 'bohman', 'blackman', 'nuttall', 'blackmanharris', 'flattop', 'bartlett', 'barthann', 'hamming', 'kaiser', 'kaiser_bessel_derived', 'gaussian', 'general_cosine', 'general_gaussian', 'general_hamming', 'chebwin', 'cosine', 'hann', 'exponential', 'tukey', 'taylor', 'dpss', 'get_window', 'lanczos']

def general_cosine(M, a, sym: bool = True): ...
def boxcar(M, sym: bool = True): ...
def triang(M, sym: bool = True): ...
def parzen(M, sym: bool = True): ...
def bohman(M, sym: bool = True): ...
def blackman(M, sym: bool = True): ...
def nuttall(M, sym: bool = True): ...
def blackmanharris(M, sym: bool = True): ...
def flattop(M, sym: bool = True): ...
def bartlett(M, sym: bool = True): ...
def hann(M, sym: bool = True): ...
def tukey(M, alpha: float = 0.5, sym: bool = True): ...
def barthann(M, sym: bool = True): ...
def general_hamming(M, alpha, sym: bool = True): ...
def hamming(M, sym: bool = True): ...
def kaiser(M, beta, sym: bool = True): ...
def kaiser_bessel_derived(M, beta, *, sym: bool = True): ...
def gaussian(M, std, sym: bool = True): ...
def general_gaussian(M, p, sig, sym: bool = True): ...
def chebwin(M, at, sym: bool = True): ...
def cosine(M, sym: bool = True): ...
def exponential(M, center: Incomplete | None = None, tau: float = 1.0, sym: bool = True): ...
def taylor(M, nbar: int = 4, sll: int = 30, norm: bool = True, sym: bool = True): ...
def dpss(M, NW, Kmax: Incomplete | None = None, sym: bool = True, norm: Incomplete | None = None, return_ratios: bool = False): ...
def lanczos(M, *, sym: bool = True): ...
def get_window(window, Nx, fftbins: bool = True): ...
