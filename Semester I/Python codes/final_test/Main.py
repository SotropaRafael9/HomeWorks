from UI.UI import UI   
from Services.functions import Services
from repository.file_repo import File_repo

repo = File_repo()
Service = Services(repo)
ui = UI(Service)

ui.play_game()