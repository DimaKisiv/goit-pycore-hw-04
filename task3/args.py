import sys
from pathlib import Path

def get_directory() -> Path:
    directory_path = get_directory_path()
    if (directory_path is None):
        return None
    directory = Path(directory_path)
    if not directory.exists():
        print("Directory does not exist")
        return None
    if not directory.is_dir():
        print("It is not a directory")
        return None
    return directory

def get_directory_path() -> str:
    if(len(sys.argv)) > 1:
        return sys.argv[1]
    else:
        print("Please provide directory path")
        return None