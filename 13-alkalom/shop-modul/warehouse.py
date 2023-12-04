"""
This module represents the warehouse of our shop.
Warehouse needs: store and decrease the product number

"""


class Warehouse:
    def __init__(self):
        self.storage = {}

    def store_product(self, product, cnt):
        self.storage[product] = cnt

    def decrease_product(self, product, cnt):
        self.storage[product] -= cnt



if __name__ == '__main__':
    from products import Bread

    w = Warehouse()


    b = Bread("Paraszt", 899)
    sz = Bread("Szeletelt", 599)
    k = Bread("Kovaszos", 499)
    zs = Bread("Zsomle", 89)

    w.store_product(b, 50)
    w.store_product(sz, 50)
    w.store_product(k, 50)
    w.store_product(zs, 100)

    from products import Meat

    csm = Meat("Csirkemell", 1199)
    csc = Meat("Csirkecomb", 1099)
    pm = Meat("Pulykamell", 1699)
    csfh = Meat("Csirkefarhat", 1299)

    w.store_product(csm, 25)
    w.store_product(csc, 40)
    w.store_product(pm, 15)
    w.store_product(csfh, 50)

    from products import Sampoo
    
    sp = Sampoo("Sampon", 599)
    tf = Sampoo("Tusfurdo", 799)
    hk = Sampoo("Haj koncicionalo", 899)
    szp = Sampoo("Szappan", 299)

    w.store_product(sp, 20)
    w.store_product(tf, 30)
    w.store_product(hk, 10)
    w.store_product(szp, 50)
    
    print(w.storage)
    # w.decrease_product(b, 1)
    # print(w.storage)
