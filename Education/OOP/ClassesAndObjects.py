# Классы и объекты

# Конструкторы
class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")

tom = Person()

# Атрибуты объекта
class Person:
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age      # возраст человека
tom = Person("Tom", 22)
# обращение к атрибутам
# получение значений
print(tom.name) # Tom
print(tom.age)  # 22
# изменение значения
tom.age = 37
print(tom.age)  # 37

# tom.company = "Microsoft"
# print(tom.company)  # Microsoft

# Методы классов
class Person:   # определение класса Person
    def say_hello(self):
        print("Hello")
tom = Person()
tom.say_hello() # Hello

class Person:   # определение класса Python
    def say(self, message): # метод
        print(message)
tom = Person()
tom.say("Hello METANIT.COM")    # hello METANIT.COM

class Person:
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age      # возраст человека
    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")
tom = Person("Tom", 22)
tom.display_info()  # Name: Tom Age: 22
bob = Person("Bob", 43)
bob.display_info()  # Name: Bob Age: 43

# Деструкторы
class Person:
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
    # деструктор
    def __del__(self):
        print("Удален человек с именем", self.name)
tom = Person("Tom")
