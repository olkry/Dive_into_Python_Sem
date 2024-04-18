# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = 10
e = 4
summ = 0
count = 0

while count <= n:
    count += 2
    if count % e:  # Если True (не 0) то заходит, аналог count % e != 0
        summ += count

print(summ)
