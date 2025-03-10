# Замыкание

def outer():    # внешняя функция
    n = 5       # лексическое выражение - локальная переменная
    def inner():    # локальная функция
        nonlocal n
        n += 1      # операция с лексическим окружение 
        print(n)
    return inner

fn = outer()    # fn = inner, т.к. функция outer возвращает функцию inner
# Вызываем внутреннюю функцию inner
fn()    # 6
fn()    # 7
fn()    # 8

# Применение параметров
# Вариант 1
def multiply(n):
    def inner(m): return n * m
    return inner

# Вариант 2 через лямбда-выражение
def multiply(n): return lambda m: n * m

fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))