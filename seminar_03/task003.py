# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

elements = (1, 3, 5, 'solec', 'nurb', 'glos', 4.12, 5.2, True, False, None, 4, 6, 2.3)
dictionary = dict()

for el in elements:
    if type(el) not in dictionary.keys():
        dictionary[type(el)] = [el]
    else:
        dictionary[type(el)].append(el)

print(dictionary)

# ================================

tp = (1, 2, 'st', 'fg', 4.5, 6.7, True, False)
dct = {}
for item in tp:
    if type(item) in dct:
        dct[type(item)].append(item)
    else:
        dct[type(item)] = [item]

print(dct)
