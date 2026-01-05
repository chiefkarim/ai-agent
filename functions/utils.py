import os


def check_dir_within_working_dir_boundry(
    working_directory: str, file_path: str
) -> tuple[str, bool]:
    abs_working_dir = os.path.realpath(working_directory)
    abs_target_dir = os.path.realpath(os.path.join(abs_working_dir, file_path))
    valid_target_dir = abs_working_dir == os.path.commonpath(
        [abs_target_dir, abs_working_dir]
    )
    return abs_target_dir, valid_target_dir
