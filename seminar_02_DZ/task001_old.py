num = int(input("Введите число: "))
residue = 0
total = ''
cross = num

while cross >= 16:
    residue = cross % 16
    if residue == 1 or residue == 2 or residue == 3 or residue == 4 or residue == 5 or residue == 6 \
            or residue == 7 or residue == 8 or residue == 9 or residue == 0:
        total = str(residue) + total
    elif residue == 10:
        total = 'A' + total
    elif residue == 11:
        total = 'B' + total
    elif residue == 12:
        total = 'C' + total
    elif residue == 13:
        total = 'D' + total
    elif residue == 14:
        total = 'E' + total
    elif residue == 15:
        total = 'F' + total

    cross = cross // 16

if cross == 1 or cross == 2 or cross == 3 or cross == 4 or cross == 5 or cross == 6 \
        or cross == 7 or cross == 8 or cross == 9 or cross == 0:
    total = str(cross) + total
elif cross == 10:
    total = 'A' + total
elif cross == 11:
    total = 'B' + total
elif cross == 12:
    total = 'C' + total
elif cross == 13:
    total = 'D' + total
elif cross == 14:
    total = 'E' + total
elif cross == 15:
    total = 'F' + total

print('Шестнадцатеричное представление числа:', total if total != '0' else "")
print('Проверка результата:', hex(num))