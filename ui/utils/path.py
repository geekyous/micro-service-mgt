import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))


def resource_path(file_name: str) -> str:
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "resources", file_name)


if __name__ == "__main__":
    print(ROOT_PATH)
