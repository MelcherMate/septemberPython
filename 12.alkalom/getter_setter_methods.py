"""
Python OOP getter - setter - deleter methods
"""

class Test:

    def __init__(self):
        self.__price = 10_000
        self.__name = "Lili"

    """
        This is not the getter - setter solution, it's just the method how it's gonna work
    """

    def set_price(self, price_value):
        self.__price = price_value
    
    def get_price(self):
        return self.__price
    
    #this is a garbage collector func
    def del_price(self):
        del self.__price

my_test = Test()
my_test.set_price(20_000)

# print(my_test.get_price())
###############################################


class Test:

    def __init__(self):
        self.__price = 10_000
        self.__name = "Lili"

    def __set_price(self, price_value):
        self.__price = price_value

    def __get_price(self):
        return self.__price
    
    def __del_price(self):
        del self.__price

    price = property(__get_price,__set_price,__del_price)

my_test = Test()        
my_test.price = 30_000

# print(my_test.price)
###############################################


class Test:

    def __init__(self):
        self.__price = 10_000
        self.__name = "Lili"

    @property
    def price(self):
        ...


    @price.getter
    def price(self):
        return self.__price

    @price.setter
    def price(self, price_value):
        self.__price = price_value

    @price.deleter
    def price(self):
        del self.__price

test = Test()
test.price = 30_000

print(test.price)