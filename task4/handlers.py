from constants import Messages, Commands
import repository

def handle(command, args):
    match command:
        case Commands.HELLO:
            print(Messages.HowCanIHelpYou)
        case Commands.ADD:
            add_contact(args)
        case Commands.CHANGE:
            change_contact(args)
        case Commands.DELETE:
            delete_contact(args)
        case Commands.PHONE:
            show_phone(args)
        case Commands.ALL:
            show_all()
        case Commands.CLOSE:
            print(Messages.GoodBye)
            return False
        case Commands.EXIT:
            print(Messages.GoodBye)
            return False
    return True

def add_contact(args):
    name, phone = args
    if name in repository.contacts:
        print(Messages.ContactAlreadyExists)
        return
    repository.contacts[name] = phone
    print(Messages.ContactAdded)

def change_contact(args):
    name, phone = args
    if name not in repository.contacts:
        print(Messages.ContactDoesNotExist)
        return
    repository.contacts[name] = phone
    print(Messages.ContactChanged)

def show_phone(args):
    name = args[0]
    if name not in repository.contacts:
        print(Messages.ContactDoesNotExist)
        return
    print(repository.contacts[name])

def show_all():
    print(repository.contacts)

def delete_contact(args):
    name = args[0]
    if name not in repository.contacts:
        print(Messages.ContactDoesNotExist)
        return
    repository.contacts.pop(name)
    print(Messages.ContactDeleted)