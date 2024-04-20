
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

def calculate_fractions(frac1, frac2):
    # Разбиваем строки на числитель и знаменатель
    numerator1, denominator1 = map(int, frac1.split('/'))
    numerator2, denominator2 = map(int, frac2.split('/'))

    # Создаем объекты Fraction
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    # Вычисляем сумму и произведение дробей
    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    return sum_result, product_result


result_sum, result_product = calculate_fractions(frac1, frac2)
print('Сумма дробей:', result_sum)
print('Произведение дробей:', result_product)
print('Сумма дробей:', result_sum)
print('Произведение дробей:', result_product)