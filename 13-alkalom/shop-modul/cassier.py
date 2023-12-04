"""
This module represents my Cassier solution
"""

class Cassier:
    def __init__(self, warehouse):
        self.warehouse = warehouse

if __name__ == '__main__':
    
    from warehouse import Warehouse
    from products import Bread
    from products import Meat
    from products import Sampoo
    
    w = Warehouse()
    
    b = Bread("Paraszt", 899)
    sz = Bread("Szeletelt", 599)
    csm = Meat("Csirkemell", 1199)
    tf = Sampoo("Tusfurdo", 799)
    c = Cassier(w)
    
    c.warehouse.store_product(b, 50)
    c.warehouse.store_product(sz, 50)
    c.warehouse.store_product(csm, 25)
    c.warehouse.store_product(tf, 30)

    print(c.warehouse.storage)
    
    class Basket:

        def __init__(self, name, cnt):
            self.name = name
            self.cnt = cnt
    
    i1 = Basket("szeletelt", 2)
    i2 = Basket("csirkemell", 6)
    i3 = Basket("tusfurdo", 1)
    i4 = Basket("paraszt", 2)

    c.warehouse.decrease_product(sz, {i1.cnt})
    c.warehouse.decrease_product(b, {i4.cnt})
    c.warehouse.decrease_product(csm, {i2.cnt})
    c.warehouse.decrease_product(tf, {i3.cnt})
    print(c.warehouse.storage)

    import json

    #json.loads(f'{listofItems}')
"""
    fic. customer 1 bought:
        - 2 "szeletelt"
        - 3 "paraszt"
        - 6 "csirkemell"
        - 1 "tusfurdo"
"""