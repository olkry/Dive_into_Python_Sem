# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint as rnd


def game_hide_number(first: int, last: int, approach: int):
    hidden_number = rnd(first, last)
    count = approach
    while count != 0:
        print()
        print(f'Осталось попыток - {count} ')
        trial = int(input(f'Введите число в диапазоне от {first} до {last}: '))
        if trial > hidden_number:
            print('Загаданное число меньше.')
        elif trial < hidden_number:
            print('Загаданное число больше.')
        else:
            print(f'Поздравляем, Вы угадали число {hidden_number} за {approach - count + 1} попытки.')
            break
        count -= 1
    else:
        print()
        print(f'Попытки закончились, было загадано число {hidden_number}')


if __name__ == '__main__':

    game_hide_number(1, 100, 10)

