# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def char_dic(text: str):
    # unicodes = {}
    num_min, num_max = sorted(list(map(int, text.split())))

    # for num in range(num_min, num_max + 1):
    #     unicodes[chr(num)] = num
    # return unicodes
    return {chr(num): num for num in range(num_min, num_max)}


dic_out = char_dic(input('Введите 2 числа: '))
print(type(dic_out), dic_out, sep='\n')
