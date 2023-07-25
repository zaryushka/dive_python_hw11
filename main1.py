# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)

import time

class MyStr(str):
    """
    Класс моя строка, где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания
    """
    def __new__(cls, value, name):
        """дандр метод new, наследуем свойства класса строка"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance
    
my_str1 = MyStr('Hello world', 'Monika')
# print(my_str1.upper())
# print(my_str1.name)
# print(my_str1.time)

# print(help(MyStr))
print(my_str1.__doc__)