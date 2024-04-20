# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

EIGHT = 8
TWO = 2
NEGATIVE_ONE = -1

number = int(input("Введите число: "))
work_num = number
binar = ''
octogon = ''

while work_num:
    binar += str(work_num % TWO)
    work_num //= TWO

print(binar[::NEGATIVE_ONE])
print(bin(number))
work_num = number

while work_num:
    octogon += str(work_num % EIGHT)
    work_num //= EIGHT

print(octogon[::NEGATIVE_ONE])
print(oct(number))
