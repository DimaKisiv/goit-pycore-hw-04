from constants import Messages
from handlers import handle
from parser import parse_input
from validators import validate_input

def main():
    print(Messages.Wellcome)
    while True:
        command, *args = parse_input(input(Messages.EnterACommand))
        if not validate_input(command, args):
            continue
        if not handle(command, args):
            break

if __name__ == "__main__":
    main()