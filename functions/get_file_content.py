import os
from config import MAX_FILE_READ
from functions.utils import check_dir_within_working_dir_boundry


def get_file_content(working_directory, file_path):
    try:
        abs_target_dir, valid_target_dir = check_dir_within_working_dir_boundry(
            working_directory, file_path
        )

        if valid_target_dir != True:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        result = ""
        with open(abs_target_dir) as f:
            file_content = f.read(MAX_FILE_READ)
            if f.read(1):
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_FILE_READ} characters'
                )
            result += file_content

        return result
    except Exception as e:
        return f"Error: {e}"
