'''
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
'''

from random import randint


def zagadayka(a: int, b: int):
    number = randint(1, a)
    count = b

    def game():
        nonlocal number, count
        for i in range(count):
            a = int(input('Введите число от 1 до 100:'))
            if a == number:
                print('Вы угадали')
                return i + 1
            elif a < number:
                print('Загаданное число больше.')
            else:
                print('Загаданное число меньше.')
            return False

    return game


start_game = zagadayka(100, 10)
start_game()
