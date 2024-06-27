# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

# БЫЛО:
'''
def key_params(**kwargs):
    dict_revers = {}
    for value, key in kwargs.items():
        if not isinstance(key, (int, float, bool, tuple)) and key is not None:
            key = str(key)
        dict_revers[key] = value
    return dict_revers


params = key_params(a=True, b=False, c=True, d=False)
print(params)
print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))
print(key_params(a=42, b='hello', c=3.14, d='world'))
'''

# СТАЛО:
import ast
import logging
import argparse

FORMAT = '{levelname:<6} -- {asctime} Сообщение: {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=FORMAT, style='{')


# Вариант с записью в файл:
# logging.basicConfig(filename='./seminar_15_END_DZ/log.txt', encoding='utf-8', filemode='w', level=logging.INFO, format=FORMAT, style='{')

def key_params(**kwargs):
    logger.info(f'{'-' * 10} Начало работы программы {'-' * 10}')
    dict_revers = {}
    keys = []
    logger.info(f'Принят исходный словарь {kwargs} для обработки и реверсии.')
    for value, key in kwargs.items():
        if not isinstance(key, (int, float, bool, tuple)) and key is not None:
            key = str(key)
        dict_revers[key] = value
        logger.info(f'Ключ {value} и значение {key} успешно обработаны и приняты в работу')
        if key not in keys:
            keys.append(key)
    values = [i for i in dict_revers.values()]
    logger.info(f'Словарь успешно создан! Добавлены ключи {keys} содержащие значения {values}')
    logger.info(f'{'-' * 10} Завершение работы программы {'-' * 10}')
    return f'\nИтоговый словарь: {dict_revers}\n'


def main(args):
    try:
        kwargs = {}
        for item in args.params:
            key, value = item.split('=')
            # Попытка безопасно интерпретировать значения
            try:
                value = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                pass  # Если не удается интерпретировать, оставить как строку
            kwargs[key] = value
        logging.info(f"Обработка данных введенных с консоли: {kwargs}")
        params = key_params(**kwargs)
        print(params)
    except Exception as e:
        logging.error(f'При обработке данных возникла ошибка: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Обработка нескольких словарей")
    parser.add_argument('params', metavar='param', type=str, nargs='+', help='ключ=значение для обработки')
    dict_input = parser.parse_args()
    main(dict_input)

    # Для консоли:
    # python .\seminar_15_END_DZ\task01.py a=True, b=False, c=True, d=False
    # python .\seminar_15_END_DZ\task01.py a=1 b='hello' c=3.14 d='lol'
