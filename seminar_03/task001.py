# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

list_input = [1, 3, 8, 4, 12, 65, 9, 4, 3, 2, 1, 8, 4, 6, 3, 8, 11, 46, 42, 12, 3, 1, 2, 2, 8, 9, 6]
print(list_input)
set_list = list(set(list_input))
print(set_list)
control_list = []
for el in list_input:
    if el not in control_list:
        control_list.append(el)

print(control_list)
