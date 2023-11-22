from domain import Question
from repository.repository import repo_exception
from service.functions import Services, Services_exception


class ui:
    def __init__(self) -> None:
        self._service = Services()

    
    def print_menu(self):
        print("1. Add question")
        print("2. Print all questions")
        print("3. Exit")

    def start(self):
        while True:
            command = input("Enter command: ")
            command = command.split(" ", maxsplit = 1)
            if command[0] == 'add':
                try:
                    string = command[1].split(";")
                    question = Question(string[0], string[1],[ string[2], string[3],string[4]], string[5], string[6])
                    self._service.add(question)
                except repo_exception as exception:
                    print(exception)
            if command[0] == 'get':
                for i in self._service.get_all():
                    print(i)
            if command[0] == 'create':
                try:
                    string_create = command[1].split(" ")
                    self._service.create_quiz(int(string_create[1]), string_create[0], string_create[2])
                except Services_exception as exception:
                    print(exception)
            if command[0] == 'exit':
                break



            


    
        