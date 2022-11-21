import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            nonlocal attempts
            nonlocal desired_value
            val = func(*args, **kwargs)
            if attempts < 1:
                print('desired value was not achieved')
                return
            elif val == desired_value:
                print('desired value is ', val)
                return
            else:
                print(val)
                attempts -= 1
                return inner_wrapper(*args, **kwargs)
        return inner_wrapper
    return wrapper


@retry(attempts=5, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=5, desired_value=[2])
def get_random_values(choices, size=2):
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


if __name__ == '__main__':
    get_random_values(choices=[1, 2, 3, 4], size=2)

