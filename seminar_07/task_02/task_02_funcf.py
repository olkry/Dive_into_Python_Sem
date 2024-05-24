# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint

START, STOP = ord('A'), ord('Z')
glas = 'aeiouy'


def name_generator(number_of_names: int):
    count = 0
    while count != number_of_names:
        name = ''.join([char for char in (chr(randint(START, STOP)) for _ in range(randint(4, 7)))])
        for i in name.lower():
            if i in glas:
                count += 1
                with open('names.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{name.title()}\n')
                break


name_generator(10)

# ==============================

from string import ascii_lowercase
from random import choice, randint

MIN_LEN = 4
MAX_LEN = 7
# VOWELS = 'aeiou'
# CONSONANT = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)}
VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})
CONSONANT = ''.join(rus_alpha.difference(VOWELS))


def random_name():
    name = ''
    for position in range(randint(MIN_LEN, MAX_LEN)):
        if position % 2:
            name += choice(VOWELS)
        else:
            name += choice(CONSONANT)
    return name.capitalize()


def fill_file(count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count):
            f.write(random_name() + '\n')


fill_file(10, 'names.txt')
