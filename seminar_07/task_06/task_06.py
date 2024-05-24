# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import randint, choice, randbytes
from pathlib import Path
import os

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


def create_file(extension, path='test_dir', min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    path_exist(path)
    for i in range(file_count):
        file_name = os.path.join(path, random_name(min_len, max_len)) + '.' + extension
        if os.path.exists(file_name):
            file_name = os.path.join(path, random_name(min_len, max_len)+str(i)) + '.' + extension
        with open(file_name, 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


def create_group_f(group_ext):
    for key, value in group_ext.items():
        create_file(key, file_count=value)


def path_exist(path):
    if not os.path.exists(path):
        Path(path).mkdir()


ext_group = {'txt': 3, 'png': 2, 'md': 2}
create_group_f(ext_group)
