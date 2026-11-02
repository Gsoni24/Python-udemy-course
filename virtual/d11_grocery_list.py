db: dict[str, int] = dict()

def announcement(msg:str) -> None:
    print(f'System: {msg}')

def add_item() -> None:
    name: str = input('Enter an item: ').lower().strip()

    while True:
        try:
            quantity: int = int(input('Enter a quantity: '))
            db[name] = quantity
            announcement(f'Added {name} x {quantity}')
            break
        except ValueError:
            announcement('Error please enter a valid number.')

def remove_item() -> None:
    name: str = input('Enter an item: ').lower().strip()
    try:
        db.pop(name)
        announcement(f'Successfully removed {name}.')
    except KeyError:
        announcement(f'{name} is not found in the groceries.')

def read_list() -> None:
    if db:
        print('-'*20)
        for k, v in db.items():
            print(f'{k.capitalize()}: {v}')
        print('-'*20)
    else:
        announcement('There are no groceries to display.')

def display_options() -> None:
    print('Options:')
    print('0 - Display options')
    print('1 - Read list')
    print('2 - Add to list')
    print('3 - Remove from list')
    print('_')

def get_option(option: str) -> None:
    try:
        converted: int = int(option)
    except ValueError:
        announcement('Error, please enter a valid option.')
        return

    if  converted == 0:
        display_options()
    elif converted == 1:
        read_list()
    elif converted == 2:
        add_item()
    elif converted == 3:
        remove_item()


def main() -> None:
    display_options()

    while True:
        user_input: str = input('You: ')
        get_option(user_input)


if __name__ == '__main__':
    main()
