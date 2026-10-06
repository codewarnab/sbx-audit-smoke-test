"""Image converter endpoint helper (SMOKE-TEST: intentionally vulnerable)."""
import subprocess

# SMOKE-TEST dummy credential (fake, deleted with this repo).
API_KEY = "sk-test-DUMMY-12345-NOT-REAL"


def convert_image(user_input, fmt="png"):
    # SMOKE-TEST BUG 1: unsanitized user input into shell=True (command injection).
    cmd = f"convert {user_input} output.{fmt}"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)


def get_file_preview(path):
    # SMOKE-TEST BUG 2: path traversal, no normalization or jail.
    with open("/data/gallery/" + path, "rb") as f:
        return f.read(4096)
