# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint

START, STOP = ord('A'), ord('Z')
glas = 'aeiouy'


def name_generator(number_of_names: int):
    count = 0
    while count != number_of_names:
        name_gen = ''.join([char for char in (chr(randint(START, STOP)) for _ in range(randint(4, 7)))])
        for i in name_gen.lower():
            if i in glas:
                count += 1
                yield name_gen.title()
                break


with open('names.txt', 'a', encoding='utf-8') as f:
    for name in name_generator(10):
        print(name, file=f)
