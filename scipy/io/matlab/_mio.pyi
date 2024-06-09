from _typeshed import Incomplete

__all__ = ["mat_reader_factory", "loadmat", "savemat", "whosmat"]

def mat_reader_factory(file_name, appendmat: bool = True, **kwargs): ...
def loadmat(
    file_name, mdict: Incomplete | None = None, appendmat: bool = True, **kwargs
): ...
def savemat(
    file_name,
    mdict,
    appendmat: bool = True,
    format: str = "5",
    long_field_names: bool = False,
    do_compression: bool = False,
    oned_as: str = "row",
) -> None: ...
def whosmat(file_name, appendmat: bool = True, **kwargs): ...
