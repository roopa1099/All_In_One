## Inheritance example
from abc import ABC, abstractmethod



class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
    
class Child(Parent):
    def __init__(self, name, age):
        #super() calls the constructor of the Parent class
        super().__init__(name)
        self.age = age

    def introduce(self):
        parent_greet = self.greet()
        return f"{parent_greet} I am {self.age} years old."
    
    def tell(self):
        self.introduce()
        return "This is a method specific to the Child class."

## abstraction example  
class TestAbstraction(ABC):  # Inherit from ABC

    @abstractmethod
    def hello_world(self):
        pass
    

class AnotherTestAbstraction(TestAbstraction):

    def hello_world(self):
        return "Hello, Universe!"
    
class YetAnotherTestAbstraction(TestAbstraction):

    def hello_world(self):
        return "Hello, World!"

def test_abstraction(testAbstractionInstance):
    testAbstractionInstance.hello_world()



child = Child("Alice", 10)
print(child.introduce())
print(child.greet())  # inherited method from Parent class
print("Child's Name:", child.name)  # inherited attribute from Parent class
print("Child's Age:", child.age)  # Child class attribute
anotherTestAbs = AnotherTestAbstraction()
test_abstraction(anotherTestAbs)