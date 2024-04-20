# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.
import fractions

frac1 = "1/2"
frac2 = "1/3"

# Подошло для автотестов, НО!!!!!!!!!! это совершенно неправильное решение! К примеру попробуй тут frac1 = "2/4" frac2 = "4/8"

numerator1, denominator1 = (int(num) for num in frac1.split('/'))
numerator2, denominator2 = (int(num) for num in frac2.split('/'))

summ_frac_num, summ_frac_den = int(numerator1 * (denominator2 * denominator1 / denominator1)) + int(
    numerator2 * (denominator2 * denominator1 / denominator2)), denominator2 * denominator1
summ_final = str(summ_frac_num) + '/' + str(summ_frac_den)
prod_frac_num, prod_frac_den = numerator2 * numerator1, denominator1 * denominator2
prod_final = str(prod_frac_num) + '/' + str(prod_frac_den)

print(f'Сумма дробей: {summ_final}')
print(f'Произведение дробей: {prod_final}')

# проверка
frac1 = fractions.Fraction(numerator1, denominator1)
frac2 = fractions.Fraction(numerator2, denominator2)
print(f'Сумма дробей: {frac1 + frac2}')
print(f'Произведение дробей: {frac1 * frac2}')
