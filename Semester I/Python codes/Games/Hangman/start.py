from repository import Sequence_repo
from console import Controller
from UI import UI
from Validator import Validator

if __name__ == '__main__':
    file_path = "text.txt"
    game_repo = Sequence_repo(file_path)

    game_controller = Controller(game_repo)

    validator = Validator(game_repo)
    ui = UI(game_controller, validator)

    ui.ui_start()