# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_LIMIT = 1
MAX_LIMIT = 1000
TEN = 10
HUNDRED = 100
TWO = 2

while True:
    input_num = int(input("Type number: "))
    if MIN_LIMIT <= input_num < MAX_LIMIT:
        break
if input_num < TEN:
    input_num = input_num ** TWO
elif input_num < HUNDRED:
    input_num = (input_num // TEN) * (input_num % TEN)
else:
    input_num = input_num % TEN * HUNDRED + input_num // TEN % TEN * TEN + input_num // HUNDRED

print(input_num)
