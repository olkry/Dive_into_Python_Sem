# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются.

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
crossed = 0

for i in list1:
    if i in list2:
        crossed += 1
print(f'Количество совпадающих чисел: {crossed}')

# OLD+++++++++++++++++++++++++

counter = 0

for i in list1:
    for j in list2:
        if i == j:
            counter += 1

print('Количество совпадающих чисел:', counter)
