import os


def get_basename_from_path(path):
    """get basename from path

    Args:
        path (str): the path

    Returns:
        basename (str): the basename of path
    """
    assert isinstance(path, str)
    basename = os.path.basename(path)[:-4]  # without filename extension

    return basename
