'''
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
'''
import json
import os


def some_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        data_json = {}
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data_json = json.load(f)
        data_json[result] = {'args': args, **kwargs}
        with open(file_name, 'w') as f:
            json.dump(data_json, f)

    return wrapper


@some_decorator
def func(*args, **kwargs):
    print(args, kwargs)
    return sum(args)


func(9, 8, 4, jk=12, r=7)
