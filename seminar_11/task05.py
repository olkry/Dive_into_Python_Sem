'''
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

from functools import total_ordering


@total_ordering
class Rectangle:

    def area(self):
        return self.hight * self.length

    def __init__(self, hight, length):
        self.hight = hight
        self.length = length

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.hight + other.hight, self.length + other.length)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            new_higth = self.hight - other.hight
            new_length = self.length - other.length
            if new_higth > 0 and new_length > 0:
                return Rectangle(new_higth, new_length)
            else:
                return 'Невозможное значение'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.hight} на {self.length}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return 'Невозможно сравнить разные объекты'

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return 'Невозможно сравнить разные объекты'


rec_1 = Rectangle(10, 20)
rec_2 = Rectangle(5, 10)
add_rec = rec_1 + rec_2
sub_rec = rec_1 - rec_2
err_rec = rec_2 - rec_1
eq_rec = rec_1 == rec_2
lt_rec_1 = rec_1 > rec_2
lt_rec_2 = rec_1 < rec_2
lt_rec_3 = rec_1 >= rec_2
print(rec_1, rec_2, 'Итог сложения', add_rec, 'Итог вычитания', sub_rec, 'Ошибка:', err_rec, sep='\n')
print('-' * 150)
print('Равенство прямоугольников по площади:', eq_rec, 'Первый больше?', lt_rec_1, 'Первый меньше?', lt_rec_2,
      lt_rec_3, sep='\n')
