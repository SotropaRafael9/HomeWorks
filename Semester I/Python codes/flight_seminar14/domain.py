class flight:
    def __init__(self, id_flight, departure_city, time, arrival_time) -> None:
        self._id_flight = id_flight
        self._departure_city = departure_city
        self._time = time
        self._arrival_time = arrival_time
    
    @property
    def id_flight(self):
        return self._id_flight
    
    @property
    def departure_city(self):
        return self._departure_city
    
    @property
    def time(self):
        return self._time
    
    @property
    def arrival_time(self):
        return self._arrival_time
    
    def __str__(self) -> str:
        return self._id_flight + " -> " + self._departure_city + " " + self._time + " " + self._arrival_time