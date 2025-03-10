# Атрибуты классов и статические методы

# Атрибуты класса
class Person:
    type = "Person"
    description = "Describes a person"
print(Person.type)  # Person
print(Person.description)   # desctive a person

Person.type = "Class Person"
print(Person.type)  # Class Person

# Атрибуты класса могут применяться для таких ситуаций, когда нам надо определить некоторые общие данные для всех объектов
class Person:
    defaault_name = "Undefined"
    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.defaault_name

tom = Person("Tom")
bob = Person("")
print(tom.name) # Tom
print(bob.name) # Undefined

# Атрибут класса
class Person:
    name = "Undefined"
    def print_name(self):
        print(self.name)
tom = Person()
bob = Person()
tom.print_name()    # Underfined
bob.print_name()    # Underfined
bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined

# Пример 2
tom = Person()
bob = Person()
tom.print_name()    # Underfined
bob.print_name()    # Underfined
Person.name = "Some Person" # меняем значение атрибут класса
bob.name = "Bob"            # устанавливаем атрибут объекта
bob.print_name()    # Bob
tom.print_name()    # Some Person

# Статические методы
class Person:
    __type = "Person"
    @staticmethod
    def print_type():
        print(Person.__type)
Person.print_type() # Person - обращение к статическому методу через имя класса
tom = Person()
tom.print_type()    # Person - обращение к статическому методу через имя объекта
