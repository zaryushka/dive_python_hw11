# Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади. Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self.width = length
        else:
            self.width = width
        self.length = length

    def get_perimetr(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        width = self.width
        perimetr = self.get_perimetr() + other.get_perimetr()
        length = (perimetr - 2 * width) / 2
        return Rectangle(width, length)

    def __sub__(self, other):
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


rect1 = Rectangle(30, 5)
rect2 = Rectangle(26, 6)
rect3 = rect1 - rect2
print(rect1.get_area(), rect2.get_area())
print(rect1 == rect2)
print(rect1 > rect2)
print(rect1 < rect2)
print(rect1 >= rect2)
print(rect1 <= rect2)
print(rect1 != rect2)