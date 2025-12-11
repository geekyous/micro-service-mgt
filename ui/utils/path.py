import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))


def resource_path(file_name: str) -> str:
    base_path = os.path.join(ROOT_PATH, "ui", "resources")
    return os.path.join(base_path, file_name)
