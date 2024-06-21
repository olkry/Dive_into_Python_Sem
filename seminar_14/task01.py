'''
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
'''
from string import ascii_letters


def del_symbol(my_str: str):
    result = ''
    for char in my_str:
        if char in ascii_letters or char == ' ':  # (char.isascii() and char.isalpha()) or char == ' ':
            result += char
    return result.lower()


if __name__ == '__main__':
    wtf_letter = 'dsGFJdh..fg fdF??j !!!!!9453hGGf 09erщПВПРвп заВПп09gfDGdВПsr'
    print(del_symbol(wtf_letter))
