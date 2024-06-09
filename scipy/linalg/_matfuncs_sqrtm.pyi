import numpy as np

__all__ = ['sqrtm']

class SqrtmError(np.linalg.LinAlgError): ...

def sqrtm(A, disp: bool = True, blocksize: int = 64): ...
