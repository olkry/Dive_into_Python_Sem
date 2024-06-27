'''
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
'''

import logging
import functools

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция ' \
         'в {created} секунд записала сообщение: {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_3.log', filemode='w', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')


def dec_logger(func):
    @functools.wraps(func)
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