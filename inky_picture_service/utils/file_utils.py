import os


def get_file_basename_no_ext(fname: str) -> str:
    return os.path.basename(fname).rstrip(".jpg")


def get_root_path(path) -> str:
    # file_name = os.path.splitext(path)
    base_name = os.path.basename(path)
    return str(os.path.abspath(path)).rstrip(f'{base_name}')


def get_relative_path(path) -> str:
    return str(os.path.relpath(path))
