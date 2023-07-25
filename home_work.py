# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


import random

class Matrix:
    """класс Матрица. формирование экземпляра класса происходит с помощью модуля random."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        output = ''
        for row in self.data:
            output += ' '.join(str(elem) for elem in row) + '\n'
        return output
    
    def __add__(self, other):
        """Метод для сложения двух матриц. Если матрицы разного размера, выйдет ошибка.
        В результате сложения получаем новую матрицу, которая является 
        экземпляром класса Matrix"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('матрицы не одного размера')
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """Метод для умножения двух матриц. Если матрицы разного размера, выйдет ошибка.
        В результате умножения получаем новую матрицу, которая является 
        экземпляром класса Matrix"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('матрицы не одного размера')
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * other.data[i][j]
        return result


    
    def __eq__(self, other):
        """метод сравнения двух матриц. сравниваются соответствующие элементы матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('матрицы не одного размера')

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    
    def __gt__(self, other):
        """метод для проверки, является ли первая матрица больше второй"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('матрицы не одного размера')

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] < other.data[i][j]:
                    return False
        return True



matrix_1 = Matrix(3, 3)
matrix_2 = Matrix(3, 3)
print(matrix_1)
print(matrix_2)
print(f'matrix_1 = matrix_2: {matrix_1 == matrix_2}\n')
print(f'matrix_1 > matrix_2: {matrix_1 > matrix_2}\n')
print(f'результат сложения двух матриц:\n{matrix_1 + matrix_2}')
print(f'результат умножения двух матриц:\n{matrix_1 * matrix_2}')
print(matrix_1.__doc__)
print(help(Matrix))