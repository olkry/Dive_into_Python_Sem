# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input("Введите число: "))
num_work = num
hexagon = ''

while num_work:
    cross = num_work % 16
    num_work //= 16
    if cross == 10:
        cross = 'A'
    elif cross == 11:
        cross = 'B'
    elif cross == 12:
        cross = 'C'
    elif cross == 13:
        cross = 'D'
    elif cross == 14:
        cross = 'E'
    elif cross == 15:
        cross = 'F'
    hexagon += str(cross)

print(f'Шестнадцатеричное представление числа: {hexagon[::-1]}')
print(f'Проверка результата: {hex(num)}')
