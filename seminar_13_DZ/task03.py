'''
В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.
'''


class InvalidNameError(Exception):
    """Исключение, выбрасываемое при некорректных именах."""

    def __init__(self, name):
        super().__init__(f'Invalid name: {name}. Name should be a non-empty string.')


class InvalidAgeError(Exception):
    """Исключение, выбрасываемое при некорректном возрасте."""

    def __init__(self, age):
        super().__init__(f'Invalid age: {age}. Age should be a positive integer.')


class InvalidIdError(Exception):
    """Исключение, выбрасываемое при некорректном ID."""

    def __init__(self, id):
        super().__init__(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')


class Person:
    """
    Класс, представляющий человека.

    Атрибуты:
    - last_name (str): фамилия
    - first_name (str): имя
    - middle_name (str): отчество
    - age (int): возраст
    """

    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._middle_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        """Увеличивает возраст человека на 1 год."""
        self.age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}, age: {self.age}'


class Employee(Person):
    """
    Класс, представляющий сотрудника.

    Атрибуты:
    - id (int): уникальный идентификационный номер сотрудника
    """

    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int, employee_id: int):
        super().__init__(last_name, first_name, middle_name, age)
        self.employee_id = employee_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not isinstance(value, int) or value < 100000 or value > 999999:
            raise InvalidIdError(value)
        self._employee_id = value

    def get_level(self):
        """Возвращает уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7)."""
        return sum(int(digit) for digit in str(self.employee_id)) % 7

    def __str__(self):
        return f'{super().__str__()}, ID: {self.employee_id}'


if __name__ == '__main__':
    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.age)
