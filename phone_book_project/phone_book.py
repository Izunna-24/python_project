contact_name = []
contact_number = []


def get_contact_name():
    return contact_name


def get_contact_number():
    return contact_number


def add_contact(name, number):
    contact_name.append(name)
    contact_number.append(number)


def delete_contact(name, number):
    contact_name.remove(name)
    contact_number.remove(number)


def search_contact(detail):
    for name in contact_name:
        if detail == name:
            return True
    return False
