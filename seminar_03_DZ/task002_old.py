#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

text = 'Hello world. Hello Python. Hello again.'

# Введите ваше решение ниже



import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if not word.isdigit()]
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)

    return top_words

result = top_10_words(text)
print(result)