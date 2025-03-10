# Декораторы

# определение функции декоратора
def select(input_func):
    def output_func():  # определяет функцию, которая будет выполняться вместо оригинальной
        print("*" * 18) # перед выводом оригинальной функии выводим всякую звездочки
        input_func()    # вызов оригинальной функции
        print("*" * 18) # после вывода оригинальной функции выводим всякую звездочки
    return output_func  # возвращаем новую функцию

# определение оригинальной функции
@select # применение декоратора select
def hello():    # оригинальная функция, вызывающаяся на строке 3
    print("Hello METANIT.COM")

# вызов оригинальной функции
hello()

# Получение параметров функции в декораторе

# определение функции декоратора

# Вариант 1
def check(input_func):
    def output_func(*args):
        input_func(*args)  # Через *args получаем значения параметров оригинальной функции
    return output_func  # возвращаем новую функцию

# Вариант 2
def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]           # получаем значение второго параметра
        if age < 0: age = 1     # если возраст отрицательный, изменяем его значение на 1
        input_func(name, age)   # передаем функции значения для параметров
    return output_func

# определение оригинальной функции
@check
def print_person(name, age):
    print(f"Name: {name} Age: {age}")

# вызов оригинальной функции
print_person("Tom", 38)
print_person("Bob", -5)

# Получение результата функции

# определение функции декоратора
def check(input_func):
    def output_func(*args):
        result = input_func(*args)  # передаем функции значения для параметров
        if result < 0: result = 0   # если результат функции меньше нуля, то возвращаем 0
        return result
    return output_func

# определение оригинальной функции
@check
def sum(a, b):
    return a + b

# вызов оригинальной функции
result1 = sum(10, 20)
print(result1)

result2 = sum(10, -20)
print(result2)