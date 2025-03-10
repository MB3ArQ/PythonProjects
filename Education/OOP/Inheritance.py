# Наследование

# Множественное наследование

# класс работника
class Employee:
    def work(self):
        print("Employee works")
# класс студента
class Student:
    def study(self):
        print("Student studies")

class WorkingStudent(Employee, Student):    # Наследование от классов Employee и Student
    pass

# класс работающего студента
tom = WorkingStudent()
tom.work()  # Emplyee works
tom.study() # Student studies

# Однако если оба наследуемых класс содержать методы/атрибуты с одинаковыми именами, то это может привести к путанице
class Employee:
    def do(self):
        print("Employee works")
class Student:
    def do(self):
        print("Student studies")
class WorkingStudent(Employee, Student):
    pass
tom = WorkingStudent()
tom.do()    #?