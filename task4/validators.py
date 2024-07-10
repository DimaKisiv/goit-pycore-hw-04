from constants import Commands, Messages

def validate_input(command, args):
    if command not in vars(Commands).values():
        print(Messages.InvalidCommand)
        return False
    if command in [Commands.ALL, Commands.HELLO] and len(args) != 0:
        print(Messages.WrongParameters)
        return False
    elif command == Commands.PHONE and len(args) != 1:
        print(Messages.WrongParameters)
        return False
    elif command in [Commands.ADD, Commands.CHANGE] and len(args) != 2:
        print(Messages.WrongParameters)
        return False
    return True