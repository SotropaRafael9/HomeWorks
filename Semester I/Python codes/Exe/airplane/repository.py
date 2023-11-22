from datetime import date

def add_flight(repository, code, duration, departure_city, destination_city):
    fly = {}
    fly['code'] = code
    fly['duration'] = duration
    fly['date'] = date.today().day
    fly['departure_city'] = departure_city
    fly['destination_city'] = destination_city
    validate_flight(fly)
    repository.append(fly)

def validate_flight(fly):
    if len(fly['code']) != 5:
        raise ValueError("Invalide code")
    if fly['destination_city'] == fly['departure_city']:
        raise ValueError("Invalide departure city or destination city")
    if len(fly['code'])<3:
        raise ValueError("Invalide code")
    if fly['duration'] <=25:
        raise ValueError("Invalide duration")
    return True

def update_duration(repository, code, new_duration):
    for i in repository:
        if i['code'] == code:
            i['destination'] = new_duration

def remove_by_date(repository, date):
    i = 0
    while i < len(repository):
        aux = repository[i]
        if date == aux['date']:
            repository.pop(i)
        else:
            i+=1


def get_all(repository):
    return repository

def sort_by_duration(repository):
    repository.sort(key = lambda x : x['duration'])

def filter_by_city(repository, city):
    for i in repository:
        if not( i['departure_city'] == city):
            remove_by_departure(repository,  city)


def remove_by_departure(repository, city):
    i = 0
    while i < len(repository):
        aux = repository[i]
        if aux['departure_city'] == city:
            repository.pop(i)
        else:
            i+= 1
