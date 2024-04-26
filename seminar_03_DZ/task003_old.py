#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#lst = [1, 1, 2, 2, 3, 3]

# Введите ваше решение ниже


def get_duplicates(lst):
    seen = {}
    duplicates = []

    for item in lst:
        if item in seen:
            seen[item] += 1
            if seen[item] == 2:
                duplicates.append(item)
        else:
            seen[item] = 1

    return duplicates

result = get_duplicates(lst)
print(result)