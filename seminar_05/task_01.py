# ✔ Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.

num_1, num_2, num_3, *num_4 = map(int, [num for num in input('Введите 4 и более числа разделенных символом “/”: ').split('/')])
dictionary = {num_2: num_1, num_3: tuple(num_4)}
print(dictionary)
# =============================
data = input('Введите 4 или более чисел, через "/": ')

value_1, key_1, key_2, *value_2 = map(int, data.split('/'))

res_dict = {key_1: value_1, key_2: tuple(value_2)}
print(res_dict)