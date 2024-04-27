# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def word_numerator(text: str):
    text = sorted(text.split())
    max_len = max(map(lambda x: len(x), text))
    for i, word in enumerate(text, 1):
        print(f'{i}. {word:>{max_len}}')


str_inp = 'привет о дивный новый мир в коем такая красота'

word_numerator(str_inp)
word_numerator(input('Введите текст: '))


# ==============================
def sort_text(text: str):
    text = sorted(text.split())
    for i, item in enumerate(text, 1):
        print(f'{i}. {item: >{len(max(text, key=len))}}')


sort_text(input('Введите текст: '))
