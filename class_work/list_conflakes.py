def my_new_list(numbers):
    numbers = []
    for number in range(1, 16):
        numbers.append(number)
    return numbers


my_list = my_new_list(15)
print(my_list)


def duplicate_my_new_list(numbers):
    numbers = []
    for number in range(1, 16):
        numbers.append(number)
    list_duplicates = numbers * 2
    return list_duplicates


list_new = duplicate_my_new_list(15)
print(list)


def eliminate_duplicates_in_my_list(numbers):
    numbers = []
    for number in range(1, 16):
        numbers.append(number)
    list_duplicates = numbers * 2
    list_eliminated = list(set(list_duplicates))
    return list_eliminated

