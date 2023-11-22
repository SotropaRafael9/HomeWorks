from repository import *
def run_console(repository):
    while True:
        line = input(">")
        words = line.split(' ')
        command = words[0]
        if command == 'add':
            try:
                add_phone(repository, words[1], words[2], words[3])
            except Exception as exception:
                print(exception)
        elif command == 'filter':
            filter_by_manufacture(repository, words[1])
        elif command == 'list':
            try:
                all = get_all(repository)
                for i in repository:
                    print(i)
            except Exception as exception:
                print(exception)
        elif command == 'update':
            update_price(repository, words[1], words[2], int(words[3]))
        else:
            print("Unknown command")