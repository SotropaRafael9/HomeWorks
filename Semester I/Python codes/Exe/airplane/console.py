from repository import *

def run_console(repository):
    while True:
        line = input('>')
        words = line.split(' ')
        command = words[0]
        if command == 'add':
            try:
                add_flight(repository, words[1],int(words[2]) , words[3], words[4])
            except Exception as exception:
                print(exception)
        elif command == 'list':
            all = get_all(repository)
            for flight in repository:
                print(flight)
        elif command == 'update':
            try:

                update_duration(repository, words[1], int(words[2]))
            except Exception as exception:
                print(exception)
        elif command == 'sort':
            sort_by_duration(repository)
        elif command == 'remove':
            try:
                remove_by_date(repository, int(words[1]))
            except Exception as exception:
                print(exception)
        elif command == 'filter':
            try:
                filter_by_city(repository, words[1])
            except Exception as exception:
                print (exception)
        else:
            print("unknown command")
