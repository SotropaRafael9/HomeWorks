from services import ServiceReservation
from validator import Validate
from repository.repository import RepositoryFile
from UI.ui import ApplicationUI
from entities import Room, Reservation

repositoryRoom = RepositoryFile("rooms.txt", Room.read_mode, None)
repositoryReservation = RepositoryFile("reservations.txt", Reservation.read_mode, Reservation.write_mode)

validator = Validate()

serviceReservation = ServiceReservation(repositoryRoom, repositoryReservation, validator)

ui = ApplicationUI(serviceReservation)
ui.start_application()