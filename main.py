import sys

contacts = {}
exit_comands = ["good bye", "close", "exit"]
greetings = ["hello", "hi", "good day", "good morning", "good evening", "ave"]


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."

    return wrapper


@input_error
def hello_command():
    return "How can I help you?"


@input_error
def add_command(name, phone):
    contacts[name.title()] = phone
    return "Contact added."


@input_error
def change_command(name, phone):
    contacts[name.title()] = phone
    return "Contact updated."


@input_error
def phone_command(name):
    return contacts[name.title()]


@input_error
def show_all_command():
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def exit_command():
    print("Goodbye!")
    sys.exit(0)


def parse_command(command):
    parts = command.strip().split(" ", 1)
    if len(parts) == 1:
        return parts[0], None
    return parts[0], parts[1]


def process_command(command):
    command = command.lower()
    if command in greetings:
        return hello_command()
    elif command.startswith("add"):
        _, args = parse_command(command)
        if args is None:
            raise ValueError
        name, phone = args.split(" ", 1)
        return add_command(name, phone)
    elif command.startswith("change"):
        _, args = parse_command(command)
        if args is None:
            raise ValueError
        name, phone = args.split(" ", 1)
        return change_command(name, phone)
    elif command.startswith("phone"):
        _, args = parse_command(command)
        if args is None:
            raise ValueError
        return phone_command(args)
    elif command == "show all":
        return show_all_command()
    elif command in exit_comands:
        exit_command()
    else:
        raise ValueError


def main():
    print("Welcome!")
    while True:
        try:
            command = input("> ")
            result = process_command(command)
            print(result)
        except ValueError:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
