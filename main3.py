# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника. 
# Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений.


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
        # width = min(self.width, self.length, other.width, other.length)
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    


rect1 = Rectangle(30, 5)
rect2 = Rectangle(26, 6)
rect3 = rect1 - rect2
print(rect3.get_perimetr())
print(rect3.length)
print(rect3.width)