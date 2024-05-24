# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

START = -1000
STOP = 1000


def random_couples(add_lines: int, file_name: str):
    with open(file_name, 'a+', encoding='utf-8') as f:
        for _ in range(add_lines):
            f.write(f'{randint(START, STOP):>4} | {uniform(START, STOP)}\n')


random_couples(10, 'task_01.txt')

# ====================================

#
# from random import randint, uniform
#
# MIN_LIMIT = -1000
# MAX_LIMIT = +1000
#
#
# def fill_file(lines_num, file_name):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         for _ in range(lines_num):
#             int_num = randint(MIN_LIMIT, MAX_LIMIT)
#             float_num = uniform(MIN_LIMIT, MAX_LIMIT)
#             f.write(f'{int_num}|{float_num}\n')
#
#
# fill_file(10, 'test.txt')
