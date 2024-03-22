list1 = []
for number in range(1, 50, 5):
    list1.append(number)


def length_of_list(num):
    count = 0
    for counter in list1:
        count += 1
    return count


def sum_of_even_positions(num):
    count = 0
    for counter in list1[1::2]:
        count += counter
    return count


def sum_of_odd_positions(num):
    count = 0
    for counter in list1[::2]:
        count += counter
    return count


def return_list_of_string(words):
    results = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            results.append(word)
    return results


def multiply_elements_at_every_third_position(nums):
    numbers = 1
    for num in list1[2::3]:
        numbers *= num
    return numbers


def average_of_list_elements(nums):
    return sum(nums) / len(nums)


def get_the_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def get_the_smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

