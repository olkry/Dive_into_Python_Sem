'''Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.'''


def count(number):
    def some_decorator(func):
        result = []

        def wrapper(*args, **kwargs):
            for i in range(number):
                kwargs['k'] += 1
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return some_decorator


@count(5)
def func(*args, **kwargs):
    print(args, kwargs)
    return sum(args)


print(func(1, 4, 3, j=4, k=7))
