"""
OOP - Object Oriented Programming


camel case - MyClass -> myClass

we gonna create classes which can be the following to types:
    - behavoural class -> when we create a class for "how the machine is going to function"
    - data related class -> we wanna create classes for datastructures

Development:
    1. I create a class -> definition
    2. I create an object from the class -> variable declaration

self.variable - instance variable - instance atribute

"""

#example
class MyClass:
    pass

my_test = MyClass() # -> this is variable declaration

"""
1. Abstraction: I hide the functioning logic of the object from the class in the class
"""

class Human:

    def __init__(self, name, age):      # the __init__ method is the constructor of the class
        self.name = name                # I need the __init__, if I wanna give valuses to atributes at declaration         
        self.age = age                  # the "self" is needed alway at first it is the declarated object
        self.sex = 'male'               # hard codeing

    def hello(self):
        print(f"Hellow {self.name}!")


test = Human('Mate', 23)                # I set the value after the function 
test2 = Human('Ricsi', 33)
test3 = Human("Viki", 22)

# print(test.age)
# print(test2.name)
# print(test3.sex)

# test.hello()                          # I can call the function from "test" cause Mate is created from the Human class

"""
I have to correct the hard code by creating a new variable named "sex"
"""

# if I wanna change a name of "test" object
test.name = "Feri"
print(test.name)

# WATCH OUT!
# I can give an instans atribute to the object
'''
test.salary = 10_000
print(test.salary)
'''


"""
Inheritance

We create parents - children pares between calsses
"""

'''
class Device:
    def __init__(self, device_name, price) -> None:     # the ->None is the return value (It shoes us whats the result gonna be)
        self.device_name = device_name
        self.price = price

class PC(Device):
    def __init__(self, device_name, price, type) -> None:
        Device.__init__(self, device_name, price)
        self.type = type

# Here the Device is the parent class and PC is the child class

test = PC('My Gamer', 100_000, 'Laptop')
'''



"""
Here is a more modern way for inheritance
"""

class Device:
    def __init__(self, device_name, price) -> None:     # the ->None is the return value (It shoes us whats the result gonna be)
        self.device_name = device_name
        self.price = price

    def price_net(self):
        return self.price * 0.73

class PC(Device):
    def __init__(self, device_name, price, type) -> None:
        super().__init__(device_name, price)
        self.type = type

    def price_net(self):
        return "Mate"

# Here the Device is the parent class and PC is the child class

test = PC('My Gamer', 100_000, 'Laptop')

print(test.price_net())


"""
Polimorphism

"""