import datetime
import os

file_name = 'logs_two.txt'

def path_to_log(path):
    def replacement(old_function):
        def new_function(*args, **kwargs):
            data = datetime.datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='UTF-8') as f:
                f.write(f'\nФункция с именем:  {func_name}\n '
                        f'вызвана: {data}\n '
                        f'аргументы: {args, kwargs}\n '
                        f'результат: {result}\n')
            file = os.path.abspath(path)
            return print(f'ПУТЬ ДО ЛОГА: {file}')
        return new_function
    return replacement

@path_to_log(file_name)
def summator(x, y):
    return x + y


@path_to_log(file_name)
def divider(z, c):
    return z / c


summator(9, 10)
divider(12, 3)