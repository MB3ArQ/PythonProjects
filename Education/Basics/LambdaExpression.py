# Лямбда - выражения

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    if choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b

message = lambda: print("hello")
message()

do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)

operation = select_operation(1)
print(operation)
print(operation(10, 6))
