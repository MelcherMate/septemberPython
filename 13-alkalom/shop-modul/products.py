"""
This module handle products
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self): 
        return f"{self.name} object - {self}"
    
    def __repr__(self): 
        return f"'{self.name}' {self}"

class Bread(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "bread"

class Meat(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "meat"

class Sampoo(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "sampoo"




if __name__ == '__main__':
    p = Product("Bread", 899)
