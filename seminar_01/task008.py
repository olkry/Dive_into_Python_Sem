# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

rows = int(input('Количество рядов: '))
space = rows - 1
for i in range(rows):
    print(' ' * (space - i) + '*' * (1 + i * 2))

# ==============================
rows = int(input('Сколько рядов у ёлки: '))

for i in range(rows):
    print(f'{"*" * (1 + 2 * i):^{rows * 2 - 1}}')
