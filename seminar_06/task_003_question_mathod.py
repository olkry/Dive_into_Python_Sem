# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


from random import choice


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


riddle(
    'Зимой и летом одним цветом?',
    ['ель', 'елка', 'елочка'],
    3
)
