from constants import Commands, Messages

def validate_input(command, args):
    if command not in vars(Commands).values():
        return Messages.InvalidCommand
    if command in [Commands.ALL, Commands.HELLO] and len(args) != 0:
        return Messages.WrongParameters
    elif command == Commands.PHONE and len(args) != 1:
        return Messages.WrongParameters
    elif command in [Commands.ADD, Commands.CHANGE] and len(args) != 2:
        return Messages.WrongParameters
    return None