print("hello world!")

def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i))

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Alice", 30)
p.say_hello()

class Student:
    name: str
    age: int
    grade: int
    
    def __init__(self, name: str, age: int, grade: int):
        self: Student = Person.__init__(name, age)
        self.grade = grade

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am in grade {self.grade}.")

s = Student("Bob", 15, 9)
s.say_hello()

class Teacher:
    name: str
    age: int
    subject: str
    
    def __init__(self, name: str, age: int, subject: str):
        self: Teacher = Person.__init__(name, age)
        self.subject = subject

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I teach {self.subject}.")
    
    def teach(self, student: Student):
        print(f"{self.name} is teaching {student.name} {self.subject}.")

t = Teacher("Dr. Smith", 45, "Math")
t.say_hello()

def run_class(students: list[Student], teacher: Teacher):
    for student in students:
        teacher.teach(student)
    
    print(f"Class has {len(students)} students and {teacher.name} is the teacher, teaching {teacher.subject}.")

run_class([s, Student("Charlie", 16, 10)], t)

new_student_name = await input("Enter the name of the new student: ")

print("New student name:", new_student_name)
new_student = Student(new_student_name, 16, 10)

run_class([s, new_student], t)
