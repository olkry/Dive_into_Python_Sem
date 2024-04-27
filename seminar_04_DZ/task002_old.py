# Введите ваше решение ниже
def key_params(**kwargs):
    return {str(value) if not isinstance(value, (int, float)) else value: key for key, value in kwargs.items()}

params = key_params(a = None, b = '', c = [], d = {})
print(params)