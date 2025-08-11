import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        absolute_path = os.path.abspath(working_directory)

        if not os.path.abspath(full_path).startswith(absolute_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'


        list_content = os.listdir(full_path)

        message = []

        for dir in list_content:
            joint_path = os.path.join(full_path, dir)
            message.append(f"- {dir}: file_size={os.path.getsize(joint_path)} bytes, is_dir={os.path.isdir(joint_path)}")

        return "\n".join(message)
    except Exception as e:
        return f"Error: {e}"
