class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.say_hello()
