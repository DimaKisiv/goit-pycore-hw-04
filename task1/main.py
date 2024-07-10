from pathlib import Path

def total_salary(path):
    salaries = read_data(path)
    total = sum(salaries)
    average = (total // len(salaries))
    return (total, average)

def read_data(path: str) -> list[int]:
    file = Path(path)
    if file.exists():
        return parse_salaries(file.read_text(encoding="utf-8").splitlines())
    else:
        print("File not exists")
        return []

def parse_salaries(lines: list[str]) -> list[int]:
    salaries: list[int] = []
    for line in filter(str.strip, lines):
         split_result = line.split(",")
         if (len(split_result) > 1 and split_result[1].isdigit()):
            salary: int = int(split_result[1])  
            salaries.append(salary)
    return salaries
    

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")