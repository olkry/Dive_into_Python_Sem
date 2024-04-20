# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [5, 8, 12, 'gd', 'bp', 3.14, 8.12, 42, True, False, None, 5, 'gd', True]

for i, element in enumerate(data, 1):
    print(i, element, id(element), sys.getsizeof(element), hash(element), 'Целое число' if type(element) is int else '',
          'Строка' if type(element) is str else '')

# ===============================

data = [1, 2, 2.5, None, True, False, 'Hello']
for i in range(len(data)):
    print(f'Номер {i + 1}, значение {data[i]}, id {id(data[i])}, размер {data[i].__sizeof__()} '
        f'Хэш {hash(data[i])}, {"Целое число" if isinstance(data[i], int) else ""},'
        f'{"Строка" if isinstance(data[i], str) else ""}')