# Область видимых значений

# Глобальный контекст

name = "Tom"
def say_hi():
    print("Hello", name)
def say_bye():
    print("Good bye", name)
say_hi()
say_bye()

# Локальный контекст
def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
def say_bye():
    name = "Tom"
    print("Good bye", name)
say_hi()
say_bye()

# Скрытие переменных
# --------------------
name = "Tom"
def say_hi():
    name = "Bob"    # Скрываем значение глобальной переменной
    print("Hello", name)
def say_bye():
    print("Good bye", name)
say_hi()
say_bye()
# --------------------
name = "Tom"
def say_hi():
    global name
    name = "Bob"    # Изменяем значение глобальной переменной
    print("Hello", name)
def say_bye():
    print("Good bye", name)
say_hi()
say_bye()

# nonlocal
def outer(): # внешняя функция
    n = 5
    def inner(): # вложенная функция
        nonlocal n # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)
    inner()
    print(n)
outer()

