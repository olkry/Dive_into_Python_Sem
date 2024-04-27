# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unicod_sorted(text: str):
    unicods = sorted(map(lambda x: ord(x), text), reverse=True)
    print(*unicods)
    print(*map(lambda x: chr(x), unicods))


str_inp = 'Здарова'

unicod_sorted(str_inp)


# ===============================

def text_list(text: str):
    res = set()
    for i in text:
        res.add(ord(i))
    return sorted(res, reverse=True)


in_text = input("Введите текст: ")

print(text_list(in_text))


# ================================

def text_list(text: str):
    return sorted([ord(i) for i in set(text)], reverse=True)


in_text = input("Введите текст: ")

print(text_list(in_text))
