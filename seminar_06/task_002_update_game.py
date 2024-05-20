# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.


from random import randint as rnd
from sys import argv


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
    first, last, approach = 1, 100, 10
    inp_argv = list(map(int, argv[1:]))
    if len(inp_argv) >= 1:
        last = inp_argv[0]
    elif len(inp_argv) >= 2:
        last = inp_argv[1]
        first = inp_argv[0]
    elif len(inp_argv) >= 3:
        last = inp_argv[1]
        first = inp_argv[0]
        approach = inp_argv[2]
    game_hide_number(first, last, approach)
