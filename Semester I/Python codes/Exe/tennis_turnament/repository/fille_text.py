from domain.player_class import player

class player_repository_memory:
    def __init__(self) -> None:
        self._data =[player("100", "Alice", "46"), player("101", "Bob", "34"), player("102", "Eve", "68"), player("103", "Carla", "56"), player("104","James", "33" ) , player("105", "Migue","36"), player("106", "Robby", "90"), player("107"," Johnny", "33"), player("108", "Radu", "89"), player("109", "Dave", "60"), player("110", "Andrea", "59"), player("111", "Rafa","99"), player("112", "Dorian", "74")]

    def add(self, new_player:player):

        if new_player.player_id in self._data:
            raise ValueError("Player is already introduce")

        self._data.append(new_player)

    def get_all(self):
        return self._data
    

class player_repository_text_fille(player_repository_memory):
    def __init__(self, file_name="player.txt") -> None:
        super(player_repository_text_fille).__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        lines = []

        try:
            file_open = open(self._file_name, "Read Text")
            lines = file_open.readlines()
            file_open.close()
        except IOError("input output error"):
            pass

        for line in lines:
            current_line = line.split(",")
            line_0 = current_line[0]
            line_1 = current_line[1]
            line_2 = current_line[2]
            line_3 = current_line[3]
            # we we had in begining spaces or at the end strip delit it
            new_player = player(line_0.strip(), line_1.strip(),
                            line_2.strip(), line_3.strip())
            super().add(new_player)

    def _save_file(self):
        file_out = open(self._file_name, "Rewrite text file model")
        for book in self.get_all():
            player_string = str(book.book_id) + "," + \
                str(book.author) + "," + str(book.title) + "\n"
            file_out.write(player_string)
        file_out.close()

    def add(self, new_player: player):
        super().add(new_player)
        self._save_file()
    


    