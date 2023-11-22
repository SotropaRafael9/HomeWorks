EXIT_OPTION = "0"
DISPLAY_ALL_PLAYERS_SORTED_BY_STRENGTH = "1"
DISPLAY_ALL_PLAYERS = "2"
FILTER_BY_FIRST_WORD_OPTION = "3"
UNDO_OPTION = "4"
class UI:
    def __init__(self, service) -> None:
        self._service = service

    @staticmethod
    def print_menu():
        print("0. Exit")
        print("1. DISPLAY ALL PLAYER SORTED IN DESCENDING ORDER")
        print("2. ")
        print("3. Filter by first name of the book")
        print("4. Undo the last operation")
        print(" ")


    def run(self):

        while True:
            UI.print_menu()
            your_choice = input("Enter your choice: ")
            try:
                if your_choice == EXIT_OPTION:
                    break
                elif your_choice == DISPLAY_ALL_PLAYERS_SORTED_BY_STRENGTH:
                    l = self._service.get_rep_service()
                    for item in l:
                        print(item)


            #     elif your_choice == FILTER_BY_FIRST_WORD_OPTION:
            #         self._service.remove_by_first_word(
            #             input("Enther the word to remove: "))
            #     elif your_choice == UNDO_OPTION:
            #         self._service.undo()
            #     else:
            #         print("Unknown command")
            except Exception as exception:
                print(exception)
