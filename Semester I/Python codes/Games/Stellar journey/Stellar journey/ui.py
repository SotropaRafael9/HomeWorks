from main import Board

class UI:

    def menu(self):
        print("Welcome to STELLAR JOURNEY! \n"
              "1. Warp <coordinate> \n"
              "2. Fire <coordinate> \n"
              "3. Cheat \n"
              "0. Exit")
        board = Board(8, 8, 1, 3, 10)
        board._place_enemy_ship()
        while True:
            command = input("Please make a choice >>")
            if command == "1":
                print(board)
                try:
                    coordinates = input("Choose the coordinate (A-H and 1-8) you want to move endeavour to: ")
                    if ord(coordinates[0]) - 65 < 0 or ord(coordinates[0]) - 65 > 7 or int(coordinates[1]) < 0 or int(coordinates[1]) > 7 or len((coordinates)) > 2:
                        raise ValueError
                    else:
                        if board._is_lose(ord(coordinates[0]) - 65, int(coordinates[1]) - 1):
                            print("YOU LOST!")
                            return
                        if board._move(ord(coordinates[0]) - 65, int(coordinates[1]) - 1):
                            print(board)
                            print("We warped successfully to", coordinates, "!")
                        else:
                            print("We cannot warp there!")
                except ValueError:
                    print("Please choose a valid coordinate!")
            elif command == "2":
                print(board)
                try:
                    coordinates = input("Choose the coordinate (A-H and 1-8) near the ship you want to shoot to: ")
                    end_row, end_col = board._get_position_of_endeavour()
                    if (abs(ord(coordinates[0]) - 65 - end_row) != 1 and abs(int(coordinates[1]) - 1 - end_col) != 1) or \
                            (abs(ord(coordinates[0]) - 65 - end_row) != 1 and int(coordinates[1]) - 1 == end_col) or \
                            (ord(coordinates[0]) - 65 == end_row  and abs(int(coordinates[1]) - 1 - end_col) != 1):
                        raise ValueError
                    else:
                        if board._fire(ord(coordinates[0]) - 65, int(coordinates[1]) - 1):
                            print("Hooray! You destroyed one enemy!")
                        else:
                            print("You fired at nothing!")
                        if board._is_win():
                            print("YOU WON!")

                except ValueError:
                    print("Please choose a valid coordinate near the ship!")
            elif command == "3":

                print(board._cheat_board())
            elif command == "0":
                return
            else:
                print("Invalid command!")

ui = UI()
ui.menu()