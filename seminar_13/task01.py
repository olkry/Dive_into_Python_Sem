'''
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения.

'''


def error_func():
    while True:
        try:
            user_inp = input('Введите число: ')
            return int(user_inp)
        except ValueError:
            try:
                return float(user_inp)
            except ValueError:
                print('Введи целое или десятичное число')


a = error_func()
print(a)
print(type(a))
