from pathlib import Path

def get_cats_info(path):
    return read_data(path)

def read_data(path: str) -> list[dict[str, str]]:
    file = Path(path)
    if file.exists():
        return parse_cats(file.read_text(encoding="utf-8").splitlines())
    else:
        print("File not exists")
        return []
    
def parse_cats(lines: list[str]) -> list[dict[str, str]]:
    cats: list[dict[str, str]] = []
    for line in filter(str.strip, lines):
         split_result = line.split(",")
         if (len(split_result) == 3):
            cats.append({"id": split_result[0], "name": split_result[1], "age": split_result[2]})
    return cats


cats_info = get_cats_info("cats.txt")
print(cats_info)