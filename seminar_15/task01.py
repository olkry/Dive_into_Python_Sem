'''
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
'''

import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_1.log', filemode='a', encoding='utf-8', format=FORMAT, style='{',
                    level=logging.WARNING)


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        logger.error(e)


print(division(3, 1))
print(division(3, 0))
