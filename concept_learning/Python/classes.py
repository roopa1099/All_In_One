class Employee:


# construtor
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)


employee = Employee(101, "Roopa", 25)
employee.display()
print(employee.name)


## Instance. class, static  methods

class Dog:
    strVar = "I am a dog class variable"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"
    

    @classmethod 
    def get_info(cls):
        print("Dog name : ",cls.strVar) # this is a class level variable not instance level variable. AttributeError if not defined.

    @staticmethod
    def hello(messge):
        print("Hello from Dog class: ", messge)
        print(Dog.strVar)  # accessing class variable inside static method

Dog.get_info()
Dog.hello("Welcome!")
dog1 = Dog("Buddy", "Golden Retriever")
dog1.hello("Static method called by instance")