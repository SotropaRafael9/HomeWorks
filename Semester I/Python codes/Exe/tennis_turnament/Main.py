# 4. Books
# Manage a list of books. Each book has an isbn (string, unique), an author and a title (strings). Provide the following features:

# Add a book. Book data is read from the console.
# Display the list of books.
# Filter the list so that book titles starting with a given word are deleted from the list.
# Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.
from UI.main import UI
from repository.fille_text import player_repository_memory
from service.functions import Service


def main():
    repository = player_repository_memory()
    service = Service(repository)
    ui = UI(service)
    ui.run()


main()
