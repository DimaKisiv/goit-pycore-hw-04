from colorama import Fore
from args import get_directory, Path

def main():
    directory = get_directory()
    if not directory:
        return
    draw_directory(directory, "")

def draw_directory(directory: Path, spaces: str):
    directories = [item for item in directory.iterdir() if item.is_dir()]
    files = [item for item in directory.iterdir() if item.is_file()]
    print(f"{Fore.BLUE}{spaces}{directory.name}/")
    for child_directory in directories:
        draw_directory(child_directory, spaces + "   ")
    for file in files:
        print(f"{Fore.GREEN}{spaces + "   "}{file.name}")

if __name__ == '__main__':
    main()