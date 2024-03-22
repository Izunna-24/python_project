digits = list(range(1, 51))


# def check_even(number):
#   return number % 2 == 0

def jumoke(p):
    return p ** 2


# to use the filter higher order function on check_even call the ref not the method

# print(list(filter(check_even, digits)))
# print(list(filter(lambda number: number % 2 == 0, digits)))

print(list(map(jumoke, digits)))
