# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list_inp = [1, 2, 3, 7, 8, 9, 2, 8, 1, 1, 7, 7, 9]

for el in list_inp:
    count = list_inp.count(el)
    if count == 2:
        list_inp.remove(el)
        list_inp.remove(el)

print(list_inp)
# == == == == == == == == == == == == == == == == == == == == == =
sample_list = [1, 2, 1, 1, 2]

for item in set(sample_list):
    if sample_list.count(item) == 2:
        sample_list.remove(item)
        sample_list.remove(item)
print(sample_list)
