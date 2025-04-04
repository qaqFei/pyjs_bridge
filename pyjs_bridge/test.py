from js_typehint import *

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

jack = Person("Jack", 25)
jack.say_hello()

print(f"{jack}")
