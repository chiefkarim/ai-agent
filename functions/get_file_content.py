import os
from config import MAX_FILE_READ


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.realpath(working_directory)
        abs_target_dir = os.path.realpath(os.path.join(abs_working_dir, file_path))
        valid_target_dir = abs_working_dir == os.path.commonpath(
            [abs_target_dir, abs_working_dir]
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
