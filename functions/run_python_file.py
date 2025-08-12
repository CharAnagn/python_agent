import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["uv", "run", abs_file_path, *args],
            cwd=abs_working_dir,
            capture_output=True,
            timeout=30,
            text=True
        )

        stdout_text = result.stdout or ""
        stderr_text = result.stderr or ""

        #No output at all
        if not result.stdout and not result.stderr:
            return "No output produced."

        output_message = f"STDOUT:\n{stdout_text}\nSTDERR:\n{stderr_text}"


        if result.returncode != 0:
            output_message += f"\nProcess exited with code {result.returncode}"

        return output_message

    except Exception as e:
         return f"Error: executing Python file: {e}"
