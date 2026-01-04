import os


def get_files_info(working_directory: str, directory: str = "."):
    try:
        result = (
            "Result for current directory:\n"
            if directory == "."
            else f"Result for '{directory}' directory:\n"
        )
        abs_working_dir = os.path.realpath(working_directory)
        abs_target_dir = os.path.realpath(os.path.join(abs_working_dir, directory))
        if not os.path.isdir(abs_target_dir):
            return result + f'Error: "{directory}" is not a directory'

        valid_target_dir = abs_working_dir == os.path.commonpath(
            [abs_target_dir, abs_working_dir]
        )
        if valid_target_dir != True:
            return (
                result
                + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )

        with os.scandir(abs_target_dir) as it:
            for item in it:
                result += f"- {item.name}: file_size={item.__sizeof__()} bytes, is_dir={item.is_dir()}\n"
        return result[: len(result) - 1]
    except Exception as e:
        return f"Error: {e}"
