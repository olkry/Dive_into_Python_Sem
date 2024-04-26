# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

string_inp = 'fdglsjeikagsdqwerejklhfdjvbmxzfofbvhucxh'
dictionary = {}
dictionary_prim = {}

for el in set(string_inp):
    counter = string_inp.count(el)
    dictionary[el] = counter

for el in set(string_inp):
    count = 0
    for elements in string_inp:
        if el == elements:
            count += 1
    dictionary_prim[el] = count

print(dictionary)
print(dictionary_prim)

# ===================================
# text = input("Введите текст: ")
#
# dict_text = dict()
#
# for char in text:
#     if char in dict_text:
#         dict_text[char] += 1
# else:
#     dict_text[char] = 1
# print(dict_text)
# ======================================

text = input("Введите текст: ")

dict_text = dict()

for char in text:
    dict_text[char] = dict_text.get(char, 0) + 1
print(dict_text)