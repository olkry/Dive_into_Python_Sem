# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import randint, choice, randbytes

rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)}
VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})
CONSONANT = ''.join(rus_alpha.difference(VOWELS))


def random_name(min_len, max_len):
    name = ''
    for position in range(randint(min_len, max_len)):
        if position % 2:
            name += choice(VOWELS)
        else:
            name += choice(CONSONANT)
    return name.capitalize()


def create_file(extension, min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    for _ in range(file_count):
        with open(f'test_direct/{random_name(min_len, max_len)}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


def create_group_f(group_ext):
    for key, value in group_ext.items():
        create_file(key, file_count=value)


ext_group = {'txt': 3, 'png': 2, 'md': 2}
create_group_f(ext_group)
