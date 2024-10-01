from pathlib import Path


def normalize_path(path: str | Path, absolutize=False) -> Path:
    """
    Normalize a given path by resolving any symbolic links and converting it to
    an absolute path if required.

    Parameters:
    - path (str | Path): The path to be normalized. It can be either a string or a Path object.
    - absolutize (bool, optional): If True, the normalized path will be converted to an absolute path. Default is False.

    Returns:
    - Path: The normalized path as a Path object.
    """
    assert isinstance(path, Path) or isinstance(path, str), \
        'path must be a Path object or a string'
    result = Path(path).resolve()
    if absolutize:
        result = result.absolute()
    return result
