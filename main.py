import random


def retry(attempts=3, desired_value=None):
    def wrapper(func):
        nonlocal attempts
        nonlocal desired_value
        val = func()
        if attempts < 1:
            print('desired value was not achieved')
            return
        elif val == desired_value:
            print('desired value is ', val)
            return
        else:
            attempts -= 1
            return wrapper(func)
    return wrapper


def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


def get_random_values(choices=[1, 2, 3, 4], size=2):
    return random.choices(choices, k=size)


def print_square(n):
    def inner_space(m):
        if m == 2:
            return'*\n* '
        elif m < 2:
            return ''
        return inner_space(m-1) + ' '
    if n == 1:
        print('*')
    else:
        print('*' * (n-1) + inner_space(n-1) * (n-2) + '*\n*' + '*' * (n-1))

