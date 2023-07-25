# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые данные из ранее созданных экземпляров 
# сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.

# class Archive:
#     list_number = []
#     list_string = []

#     def __init__(self, number, string):
#         self.number = number
#         self.string = string
#         self.list_number.append(number)
#         self.list_string.append(string)

# my_archive1 = Archive(15, 'Hello')
# print(my_archive1.list_number)
# print(my_archive1.list_string)

# my_archive2 = Archive(56, 'world')
# print(my_archive2.list_number)
# print(my_archive2.list_string)



class Archive:
    _instance = None

    def __new__(cls, number, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_number = []
            cls._instance.list_string = []

        cls._instance.list_number.append(number)
        cls._instance.list_string.append(string)     
        return cls._instance       


    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self):
        return f'Экземпляр класса Archive с номером {self.number} и строкой {self.string}'
    
    def __repr__(self):
        return f'Archive {self.number} {self.string}'


my_archive1 = Archive(15, 'Hello')
print(my_archive1.list_number)
print(my_archive1.list_string)

my_archive2 = Archive(56, 'world')
print(my_archive2.list_number)
print(my_archive2.list_string)

my_archive3 = Archive(60, 'people')
print(my_archive3.list_number)
print(my_archive3.list_string)

print(f'{my_archive1 = }')
# print(repr((my_archive1)))