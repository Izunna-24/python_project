from time import time


def decorate(fn):
    def wrapper(*args, **kwargs):
        print("*************")
        print(fn(*args, **kwargs))
        print("*************")

    return wrapper


# keyword argument = kwargs


@decorate
def show_name(name):
    return name


show_name(name='People Of God')


# to know how long a function takes to run
def time_taken(func):
    def inner(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t2 - t1:.3f}ms to execute")
        return result

    return inner


@time_taken
def get_list(numbers):
    result = []
    for i in range(numbers):
        result.append(i)
    return result


get_list(100000000)
