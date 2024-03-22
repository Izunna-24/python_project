def upper_and_lower_case(sample):
    count_upper = 0
    count_lower = 0
    for letter in sample:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
    return count_upper, count_lower


