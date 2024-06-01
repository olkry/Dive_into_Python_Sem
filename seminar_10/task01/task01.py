'''Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.'''
import math


class Circle:
    # pi = math.pi
    PI = 3.14
    def __init__(self, radius: int = 1):
        self.radius = radius

    def length_circle(self):
        return 2 * self.PI * self.radius

    def area_circ(self):
        return self.PI * (self.radius ** 2)


test_cir = Circle(666)

print(test_cir.length_circle())
print(test_cir.area_circ())
