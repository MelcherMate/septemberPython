import test_modul

print("Ez az example.py")
print(test_modul.my_list)


# if I use *, I can overdefine object by acident
from test_modul import *

my_list = "Mate"

def my_func():
    return("almafa")

sol = my_func()

print(sol)