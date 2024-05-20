# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

from random import choice
import task_005_qest_counter


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


riddle_dict = {'Зимой и летом одним цветом?': ['ель', 'елка', 'елочка'],
                     'Зимой и летом одним цветом?1': ['ель', 'елка', 'елочка'],
                     'Зимой и летом одним цветом?2': ['ель', 'елка', 'елочка']}


def riddle_game(riddle_dictionary):
    for key, value in riddle_dictionary.items():
        task_005_qest_counter.stat_forming(key, riddle(key, value, 3))

# riddle_game(riddle_dict)
