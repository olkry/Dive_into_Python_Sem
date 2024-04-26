# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

input_date = input('Введите данные: ')
flag = False
while True:
    if '.' in input_date:
        flot_cor = input_date.split('.')
        if len(flot_cor) == 2:
            if flot_cor[0].isdigit() and flot_cor[1].isdigit():
                input_date = float(input_date)
                break

    if input_date.isdigit():
        input_date = int(input_date)
        break

    else:
        for el in input_date:
            if el.upper() == el and el.isalpha():
                flag = True

    if flag:
        input_date = input_date.lower()
        break
    else:
        input_date = input_date.upper()
        break

print(type(input_date), input_date)

# +++++++++++++++++++++++++++++++++++++++++

value = input('Введите данные: ')

try:
    if not value.isdigit():
        value = float(value)
    elif value.isdigit() and int(value) > 0:
        value = int(value)
except:
    if not value.islower():
        value = value.upper()
    else:
        value = value.lower()

print(value)
print(type(value))
