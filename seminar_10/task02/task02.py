'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
'''


class Rectangle:

    def __init__(self, sitd_a, sitd_b=None):
        self.sitd_a = sitd_a
        self.sitd_b = sitd_b if not sitd_b is None else sitd_a

    def perimeter(self):
        return (self.sitd_a + self.sitd_b) * 2

    def area(self):
        return self.sitd_b * self.sitd_a


if __name__ == '__main__':
    rectangle = Rectangle(5, 4)
    print(rectangle.perimeter())
    print(rectangle.area())
    square = Rectangle(6)
    print(square.perimeter())
    print(square.area())
