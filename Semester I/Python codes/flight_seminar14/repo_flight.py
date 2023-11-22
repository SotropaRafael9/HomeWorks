from domain import flight
class flight_repo:
    def __init__(self) -> None:
        self._data = [flight("1.", "Jules Verne", "2000 de leghe sub mari"),
                      flight("2.", "Harper Lee", "sa ucizi o pasare cantatoare"),
                      flight("3", "Honore de Balzac", "Comedie Umana"),
                      flight("4", "Euripide", "Omul Invizibil"),
                      ]

    def add(self, new_flight: flight):
        if new_flight in self._data:
            raise ValueError("Flight is already introduce")
        self._data.append(new_flight)

    def get_all(self):
        return self._data

class flight_repository_text_file(flight_repo):
    def __init__(self, file_name="flight.txt") -> None:
        super(flight_repository_text_file).__init__()
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
            new_book = flight(line_0.strip(), line_1.strip(),
                            line_2.strip(), line_3.strip())
            super().add(new_book)

    def _save_file(self):
        file_out = open(self._file_name, "Rewrite text file model")
        for flight in self.get_all():
            flight_string = str(flight.id_flight) + "," + \
                str(flight.author) + "," + str(flight.title) + "\n"
            file_out.write(flight_string)
        file_out.close()

    def add(self, new_flight: flight):
        super().add(new_flight)
        self._save_file()



