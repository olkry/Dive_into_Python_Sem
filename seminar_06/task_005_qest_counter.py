# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.

from random import choice

_riddle_stat = {}


def riddle(riddle_text, answer_list, attempts):
    answer_list = list(map(lambda word: word.lower(), answer_list))
    print(riddle_text)
    count = 0
    while count < attempts:
        answer = input("Введите отгадку: ")
        count += 1
        if answer.lower() in answer_list:
            print(f"Вы угадали! Попытка номер {count}")
            return count
        print("Попробуйте еще раз!")
    print(f"Попытки закончились. Правильный ответ {choice(answer_list)}")
    return 0


def riddle_game(riddle_dictionary):
    for key, value in riddle_dictionary.items():
        stat_forming(key, riddle(key, value, 3))


def stat_forming(riddle_text, attempt):
    if riddle_text in _riddle_stat:
        _riddle_stat[riddle_text].append(attempt)
    else:
        _riddle_stat[riddle_text] = [attempt]


def print_stat():
    for text, attempts in _riddle_stat.items():
        for item in attempts:
            print(f'Загадка {text}, отгадана с попытки {item}')


def riddle_game(riddle_dictionary):
    for key, value in riddle_dictionary.items():
        stat_forming(key, riddle(key, value, 3))


if __name__ == '__main__':
    riddle_dictionary = {'Зимой и летом одним цветом?': ['ель', 'елка', 'елочка'],
                         'Зимой и летом одним цветом?1': ['ель', 'елка', 'елочка'],
                         'Зимой и летом одним цветом?2': ['ель', 'елка', 'елочка']}
    riddle_game(riddle_dictionary)
    print_stat()
