'''
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

На входе:


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)
На выходе:


True
True
Формат JSON файла определён следующим образом:

[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]
'''

from random import choice, randint
import csv
import json


def csv_reader(path: str = 'input_data.csv') -> list[tuple]:
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, dialect='excel', delimiter=';')
        for row in reader:
            if row:
                result.append(tuple(map(float, row)))
    return result


def json_writer(result: dict, path: str = 'results.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def save_to_json(func):
    def inner():
        root = func
        json_writer(root)
        return root

    return inner()


def deco_abc(func):
    abc_list = csv_reader()

    def inner():
        result = {}
        for abc in abc_list:
            roots = func(abc)
            a, b, c = abc
            result[f'{a=}, {b=}, {c=}'] = roots
        return result

    return inner()


def generate_csv_file(file_name, count: int = 100):
    final_abc = []
    for _ in range(count):
        final_abc.append((choice([*range(-100, 0), *range(1, 101)]), randint(-100, 100), randint(-100, 100)))
    with open(file_name, 'w', encoding='utf-8') as file:
        wr = csv.writer(file, dialect='excel', delimiter=';')
        wr.writerows(final_abc)


@save_to_json
@deco_abc
def find_roots(abc: tuple[int, int, int]) -> tuple:
    a, b, c = abc
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discr == 0:
        return (round(-b / (2 * a), 2),)
    else:
        return (None,)


generate_csv_file('input_data.csv', 1000)
find_roots()
