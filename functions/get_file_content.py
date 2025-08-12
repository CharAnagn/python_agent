import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.abspath(full_path)

        if not absolute_file_path.startswith(absolute_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if os.path.getsize(absolute_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters.]'

        return file_content_string

    except Exception as e:
        return f"Error: {e}"
