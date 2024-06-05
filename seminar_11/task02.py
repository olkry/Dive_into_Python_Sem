'''
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра

Добавьте к задачам 1 и 2 строки документации для классов.

Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
'''


class MyClass:
    '''Задача для семинара, добавляет св-ва к классу'''

    _my_list = []

    def __init__(self, number, my_str):
        self.number = number
        self.my_str = my_str

    def __new__(cls, *args, **kwargs):
        instanse = super().__new__(cls)
        instanse.archive = MyClass._my_list.copy()
        MyClass._my_list.append(instanse)
        return instanse

    def __repr__(self):
        return f'MyClass("{self.number}", "{self.my_str}")'

    def __str__(self):
        return f'Добавлены свойства экземпляра {self.number = } и {self.my_str = }'


cl_1 = MyClass('1', 'Hello')
cl_2 = MyClass('2', 'World')
cl_3 = MyClass('3', '!!!')

a = eval(cl_1.__repr__())

print(cl_1.archive, cl_2.archive, cl_3.archive, sep='\n')
print(cl_1, cl_2, cl_3, sep='\n')
print(a)
