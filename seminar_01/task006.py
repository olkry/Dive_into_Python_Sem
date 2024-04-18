# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один prin

FOUR = 4
FOUR_HUNDRED = 400
HUNDRED = 100
GRIG_CAL = 1582
year = int(input("Please write year: "))
leap = False
flag = False

if year >= GRIG_CAL:
    flag = True
    if year % FOUR_HUNDRED == 0:
        leap = True
    elif year % FOUR == 0:
        if year % HUNDRED != 0:
            leap = True
print("Is year {} a leap year? {}".format(year, leap) if flag else "Year is not valid for task")
