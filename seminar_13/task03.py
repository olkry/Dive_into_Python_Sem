'''
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
'''


class MyException(Exception):
    pass


class LevelError(MyException):
    pass


class AccessError(MyException):
    pass
