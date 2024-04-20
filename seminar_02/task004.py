# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой

from math import pi

diameter = float(input('Введите диаметр окружности: '))
print(f'Длинна окружности: {2 * pi * (diameter / 2):.42f}')

# =================================

import decimal
from math import pi

decimal.getcontext().prec = 42

diameter = decimal.Decimal(input('Введите диаметр окружности: '))
print(f'Длинна окружности: {2 * decimal.Decimal(pi) * (diameter / 2)}')
