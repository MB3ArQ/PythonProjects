# Перегрузка операторов
from tabulate import tabulate

table_headers = ['Operation', 'Syntax', 'Function']
table_data = [
    ['Addition', 'a + b', '__add__(a, b)'],
    ['Union', 'seq1 + seq2', '__concat__(seq1, seq2)'],
    ['Exist Check', 'obj in seq', '__constains__(seq, obj)'],
    ['Dividing', 'a / b', '__truediv__(a, b)'],
    ['Dividing', 'a // b', '__floordiv__(a, b)'],
    ['&', 'a & b', '__and__(a, b)'],
    ['^', 'a ^ b', '__xor__(a, b)'],
    ['Inversion', '~ a', '__invert__(a)'],
    ['|', 'a | b', '__or__(a, b)'],    
    ['Degree', 'a ** b', '__pow__(a, b)'],
    ['Assignment Of Index', 'obj[k] = v', '__setitem__(obj, k, v)'],
    ['Delete Of Index', 'del obj[k]', '__delitem__(obj, k)'],
    ['Reference Of Index', 'obj[k]', '__getitem__(obj, k)'],
    ['Move Left', 'a << b', '__lshift__(a, b)'],
    ['Resudal of Division', 'a %< b', '__mod__(a, b)'],
    ['Multiplication', 'a * b', '__mul__(a, b)'],
    ['Matrix Multiplication', 'a @ b', '__matmul__(a, b)'],
    ['Arithmetic Negation', '-a', '__neg__(a)'],
    ['Logic Negation', 'not a', '__not__(a)'],
    ['Positive Value', '+a', '__pos__(a)'],
    ['Move Right', 'a >> b', '__rshift__(a, b)'],
    ['Range Definition', 'seq[i:j] = values', '__setitem__(seq, slice(i, j), values)'],
    ['Range Delete', 'del seq[i:j]', '__delitem__(seq, slice(i, j))'],
    ['Range Receipt', 'seq[i:j]', '__getitem__(seq, slice(i, j))'],
    ['Substract', 'a - b', '__sub__(a, b)'],
    ['True/False Check', 'abj', '__bool__(obj)'],
    ['Less Than', 'a < b', '__lt__(a, b)'],
    ['Less Or Equal Than', 'a <= b', '__le__(a, b)'],
    ['Equal', 'a == b', '__eq__(a, b)'],
    ['Not Equal', 'a != b', '__ne__(a, b)'],
    ['Greater Or Equal Than', 'a >= b', '__ge__(a, b)'],
    ['Greater Than', 'a > b', '__gt__(a, b)'],
    ['Addition With Assignment', 'a += b', '__iadd__(a, b)'],
    ['Union With Assignment', 'a += b', '__iconcat__(a, b)'],
    ['& With Assignment', 'a &= b', '__iand__(a, b)'],
    ['Dividing With Assignment', 'a //= b', '__ifloordiv__(a, b)'],
    ['Move Left With Assignment', 'a <<= b', '__ilshift__(a, b)'],
    ['Move Right With Assignment', 'a >>= b', '__irshift__(a, b)'],
    ['Resudal of Division With Assignment', 'a %= b', '__imod__(a, b)'],
    ['Multiplication With Assignment', 'a += b', '__imul__(a, b)'],
    ['Matrix Multiplication With Assignment', 'a @= b', '__imatmul__(a, b)'],
    ['| With Assignment', 'a |= b', '__ior__(a, b)'],
    ['Degree With Assignment', 'a **= b', '__ipow__(a, b)'],
    ['Substract With Assignment', 'a -= b', '__isub__(a, b)'],
    ['Dividing With Assignment', 'a /= b', '__itruediv__(a, b)'],
    ['^ With Assignment', 'a ^= b', '__ixor__(a, b)']    
]

print(tabulate(tabular_data=table_data, headers=table_headers, tablefmt="grid"))

class Counter:
    def __init__(self, value):
        self.value = value
    # переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other.value)
counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)   # 20

class Counter:
    def __init__(self, value):
        self.value = value
    # переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other)
counter1 = Counter(5)
counter3 = counter1 + 6
print(counter3.value)

# Истинность объекта
class Counter:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0
def test(counter):
    if counter: print("Counter = True")
    else: print("Counter = False")

counter1 = Counter(3)
test(counter1)          # Counter = True

counter2 = Counter(-3)
test(counter2)          # Counter = False

# Операторы, которые возвращают значение bool
class Counter:
    def __init__(self, value):
        self.value = value
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
counter1 = Counter(1)
counter2 = Counter(2)

if counter1 > counter2:
    print("counter1 больше чем counter2")
elif counter1 < counter2:
    print("counter1 меньше чем counter2")
else:
    print("counter1 и counter2 равны")

# Операции обращения по индексу
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __getitem__(self, prop):
        if prop == "name": return self.__name
        elif prop == "age": return self.__age
        return None
tom = Person("Tom", 39)
print("Name:", tom["name"]) # Name: Tom
print("Age:", tom["age"])   # Age: 39
print("Id:", tom["id"])     # Id: None

# Проверка наличия свойства
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __contains__(self, prop):
        if prop == "name" or prop == "age": return True
        return False
tom = Person("Tom", 39)
print("name" in tom)    # True
print("id" in tom)      # False

# Реализация операторов парами
class Counter:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other): return self.value == other.value
    def __ne__(self, other): return not(self == other)
    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return not(self > other)
    def __lt__(self, other): return self.value < other.value
    def __ge__(self, other): return not(self < other)
c1 = Counter(1)
c2 = Counter(2)

print(c1 == c2) # False
print(c1 != c2) # True
print(c1 < c2)  # True
print(c1 >= c2) # False
