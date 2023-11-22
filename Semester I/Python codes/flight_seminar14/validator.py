from domain import flight
class ValidationError(Exception):
    pass

class FlightValidator:
    def __init__(self):
        pass
    def validate(self, flight:flight):
        try:
        # if True:
            assert type(flight) is flight
            assert (type(flight.id) is int )and flight.idx>0
            assert type(flight._time) is time
            assert type(flight.arrival_time)is time
            assert type(flight.departure_city) is str
            assert type(flight.arrival_city) is str
        except:
            raise ValidationError()


f=flight(1, "Vaslui", time(12,24,36,1212), "Budapesta", time(12,24,36,1212))
f.arrival_time=False
# print(f.arrival_time)
FlightValidator().validate(f)
# f.departure_time="sdf"