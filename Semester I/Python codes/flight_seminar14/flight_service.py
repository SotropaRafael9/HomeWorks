from domain import flight


class Service:

    def __init__(self, repository) -> None:
        self.__repository = repository

    def add_service(self, id_flight, departure_city, time, arrival_time):
        self.save_to_history()
        new_flight = flight(id_flight, departure_city, time, arrival_time)
        self.__repository.add(new_flight)

    def get_rep_service(self):
        return self.__repository.get_all()

