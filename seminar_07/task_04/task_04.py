# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
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
        with open(f'test_dir/{random_name(min_len, max_len)}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


create_file('txt', file_count=3, max_size=512)
