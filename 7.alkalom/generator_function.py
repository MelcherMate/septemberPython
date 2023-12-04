"""

A generator fuggvenyekben NEM return utasitassal adom vissza az ertekeket,
hanem yield utasitassal

A yield utasitas csak szunetelteti a fuggveny futasat, barmikor folytatni
tudom a fuggveny futasat, amennyiben a fuggveny tartalmaz meg tovabbi yield utasitasokat.
    -> a generator fuggvenyekben tobb utasitas is lehet, es az utasitasok kozott nem kell,
    hogy kapcsolat legyen
"""

'''
this is used rarely 

it saves memory BUT it's slower
'''

def my_gen_func():
    print("alma")
    yield 1
    ################
    print("korte")
    yield "hello"

temp = my_gen_func()

# print(next(temp))
# print(next(temp))
# print(next(temp))

for item in temp:
    print(item)





