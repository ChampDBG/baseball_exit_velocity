import os


def check_dir(path, mkdir_flag=True, overwrite=False):
    """Check the directory is exists or not

    Args:
        path (str): path for checking
        mkdir_flag (bool, optional): Create dir by path. Defaults to True.
        overwrite (bool, optional): Overwrite dir by path. Defaults to False.

    Returns:
        (bool): path exists or not
    """
    assert isinstance(path, str)

    path_existed = os.path.exists(path)

    if not mkdir_flag:
        return path_existed

    if overwrite:
        if path_existed:
            os.remove(path)
        os.mkdir(path)
        return True

    if not path_existed:
        os.mkdir(path)
        return True

    return True
