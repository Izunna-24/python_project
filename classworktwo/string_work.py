def count_digits_and_letters(value):
    count_digit = 0
    count_letter = 0
    for char in value:
        if char.isalpha():
            count_letter += 1
        elif char.isdigit():
            count_digit += 1
    return count_digit, count_letter


