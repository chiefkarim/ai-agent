import os
from functions.utils import check_dir_within_working_dir_boundry


def write_file(working_dir: str, file_path: str, content: str):
    target_dir_abs, valid_dir = check_dir_within_working_dir_boundry(
        working_dir, file_path
    )

    if not valid_dir:
        return (
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory',
        )

    if os.path.isdir(target_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    last_sub_dir = target_dir_abs.split("/")
    last_sub_dir.pop()
    last_sub_dir = "/".join(last_sub_dir)
    os.makedirs(last_sub_dir)
    with open(target_dir_abs, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
