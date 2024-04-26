# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

string_input = sorted(input('Введите слова через пробел: ').split())
max_len = max(len(lon) for lon in string_input)
for i, item in enumerate(string_input, 1):
    print(f'{i} {item:>{max_len}}')

# ===============================

string = input("Введите текст: ").split()
string = sorted(string)
for i, item in enumerate(string, 1):
    print(f'{i}. {item:>{len(max(string, key=len))}}')
