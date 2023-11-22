from Services.functions import Services
class UI:
    def __init__(self, service : Services) -> None:
        self.__service = service

    def play_game(self):

        self.__service.select_sentence()
        self.__service.scramble_sentence()

        while True:
            print(self.__service.get_sentece())
            print(self.__service.get_scramble_sentence(), f"(Score is, {self.__service.get_score()}")

            comman = input(" >>>")

            command_arguments = comman.strip().split()

            for argum in command_arguments:
                argum.strip()
            

            if command_arguments[0] == 'swap':
                if len(command_arguments) != 6:
                    print("Invalid numbers of arguments !")
                    continue
                try:
                    word_1 = int(command_arguments[1])
                    letter_1 = int(command_arguments[2])

                    word_2 = int(command_arguments[4])
                    letter_2 = int(command_arguments[5])
                except ValueError:
                    print("invalid argument !")
                    continue
                try:
                    self.__service.make_swap(word_1, letter_1, word_2, letter_2)

                except ValueError as exception:
                    print(str(exception))
            else:
                print("Invalid command !")
            game_status = self.__service.is_over()
            if game_status == -1:
                print("You lost the game ! ")
                break
            elif game_status == 1:
                print(f"Vicotry ! (Score{self.__service.get_all()}")
                break
            


