import os

from functions.utils import check_dir_within_working_dir_boundry


def get_files_info(working_directory: str, directory: str = "."):
    try:
        result = (
            "Result for current directory:\n"
            if directory == "."
            else f"Result for '{directory}' directory:\n"
        )
        abs_target_dir, valid_target_dir = check_dir_within_working_dir_boundry(
            working_directory, directory
        )
        if valid_target_dir != True:
            return (
                result
                + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(abs_target_dir):
            return result + f'Error: "{directory}" is not a directory'

        with os.scandir(abs_target_dir) as it:
            for item in it:
                result += f"- {item.name}: file_size={item.__sizeof__()} bytes, is_dir={item.is_dir()}\n"
        return result[: len(result) - 1]
    except Exception as e:
        return f"Error: {e}"
