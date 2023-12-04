"""

Magic methods - double underscore - dunderscore methods

__method__

Every class's / every object's anchient class: object
"""

class Test:
    pass

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.__class__}:{self.name} object'

test = Human("Mate", 23)
test2 = Human("Lili", 33)

print(test)
print(test2)
