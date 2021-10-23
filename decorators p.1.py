import datetime
import os


def replacement(old_function):

    def new_function(*args, **kwargs):
        data = datetime.datetime.now()
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('logs.txt', 'a', encoding='UTF-8') as f:
            f.write(f'\nФункция с именем:  {func_name}\n '
                    f'вызвана: {data}\n '
                    f'аргументы: {args, kwargs}\n '
                    f'результат: {result}\n')

        return result

    return new_function


@replacement
def summator(x, y):
    return x + y


@replacement
def divider(z, c):
    return z / c


summator(9, 10)
divider(12, 3)
