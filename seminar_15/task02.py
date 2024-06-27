'''
На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
'''

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_2.log', filemode='w', encoding='utf-8', level=logging.INFO)


def dec_logger(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        logger_txt = f'{func.__name__}:{result}, arguments: {args}, {kwargs}'
        logger.info(logger_txt)
        return result
    return inner


@dec_logger
def division(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        logger.error(e)


print(division(4, 2))
print(division(4, 0))
