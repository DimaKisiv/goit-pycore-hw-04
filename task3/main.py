from args import get_directory, Path
from colorama import Fore, Back

def main():
    directory = get_directory()
    if not directory:
        return
    draw_directory(directory, "")

def draw_directory(directory: Path, spaces: str):
    directories = [item for item in directory.iterdir() if item.is_dir()]
    files = [item for item in directory.iterdir() if item.is_file()]
    print(f"{Back.WHITE}{Fore.BLUE}{spaces}{directory.name}")
    for child_directory in directories:
        draw_directory(child_directory, spaces + "-")
    for file in files:
        print(f"{Back.WHITE}{Fore.YELLOW}{spaces + "-"}{file.name}")


    
if __name__ == '__main__':
    main()