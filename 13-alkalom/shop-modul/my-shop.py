from products import Bread, Meat, Sampoo
from cassier import Cassier
from warehouse import Warehouse

def main():
    w = Warehouse()
    b = Bread("Paraszt", 899)
    sz = Bread("Szeletelt", 600)
    c = Cassier(w)
   
    c.warehouse.store_product(b, 3)
    c.warehouse.store_product(sz, 3)
    print(c.warehouse.storage)
   
    c.warehouse.decrease_product(b, 1)
    print(c.warehouse.storage)

if __name__ == '__main__':
    main()