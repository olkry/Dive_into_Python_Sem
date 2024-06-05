'''
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
'''

from datetime import datetime


class MyString(str):

    def __new__(cls, value, name_autor, *args, **kwargs):
        instanse = super().__new__(cls, value)
        return instanse

    def __init__(self, value, name_autor):
        self.name_autor = name_autor
        self.time = datetime.now().time()


u_1 = MyString('Hello!', 'Gabriel Gasiya Markes')
print(u_1, u_1.name_autor, u_1.time, sep='\n')
