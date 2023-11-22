def add_phone(repository, manufacture, model, price):
    phone = {}
    phone['manufacture'] = manufacture
    phone['model'] = model
    phone['price'] = price
    veryfy_phone(phone)
    repository.append(phone)

def veryfy_phone(phone):
    if len(phone['manufacture']) < 3:
        raise ValueError("The phone has no manufacure ")
    if len(phone['model']) < 3:
        raise ValueError("The phone has no mdeol ")
    if len(phone['price']) < 3:
        raise ValueError("The phone price ")
    return True

def remove_by_manufacture(repository, manufacture):
    i = 0
    while i < len(repository):
        aux= repository[i]
        if aux['manufacture'] == manufacture:
            repository.pop(i)
        else:
            i = i+1

def filter_by_manufacture(repository, manufacture):
    for i in repository:
        if not i['manufacture'] == manufacture:
            remove_by_manufacture(repository, manufacture)

def get_all(repository):
    return repository

def update_price(repository, manufacture, model, new_price):
    is_phone(repository)
    for i in repository:
        if i['model'] == model:
            i['price'] = new_price
#do me some asserts for this program








# def is_phone(phone):
#     if len(phone['manufacure']) == 0:
#         raise ValueError("There is no phone in your list yet")
#     if len(phone['model']) == 0:
#         raise ValueError("There is no phone in your list yet")
#     if len(phone['price']) == 0:
#         raise ValueError("There is no phone in your list yet")
#     return True