# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

def key_params(**kwargs):
    dict_revers = {}
    for value, key in kwargs.items():
        if not isinstance(key, (int, float, bool, tuple)) and key is not None:
            key = str(key)
        dict_revers[key] = value
    return dict_revers


params = key_params(a=True, b=False, c=True, d=False)
print(params)


# ==============================


def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result
