"""
Comprehension muveletek

3 fajtaja van:
    - list comprehension:  [ciklus_valtozo for ciklus_valtozo in iteralhato_object]
    - dict comprehension
    - generator comprehension

Egyszeru szureseknel hasznalhatoak jol!

"""

#elemekkel akarok feltolteni listakat
temp = []

for item in range(1, 101):
    if item%3 == 0:
        temp.append(item)
'print(temp)'

####
my_list_comprehension = [item for item in range(1, 101) if item%3 == 0]
'print(my_list_comprehension)'

############################################

# dict_comprehension

my_list = [1, 2, 3, 4, 5]
my_list2 = ['name', 'age', 'color', 'valami', 'valami2']

my_dict = {}

for idx, item in enumerate(my_list):
    my_dict.update({my_list2[idx]:item})

my_dict_comp = {my_list2[idx]:item for idx, item in enumerate(my_list)}

print(my_dict)
print(my_dict_comp)

# masik megoldas erre
my_dict_else = dict(zip(my_list2, my_list))
print(my_dict_else)

############################################

# generetor comprehension
"""
tulajdonsagok:

Lazy-evaluationt hasznal, ami azt jelenti, hogy nem ertekeli ki az utasitast, nem kerulnek a memoriaba az adatok
ez az objektum tarolja az utasitast, de nem futtatja
igy el tudok tenni benne ciklust, amit kesobb le lehet kerni

Memoriahatekony, de lassu. Nagy adatfeldolgozaskor hasznalatos, (big data science eszkoz)

"""
my_list = [item for item in range(1000)]
gen_comp = (item for item in range(1000))

#print(next(gen_comp))
#print(next(gen_comp))
#print(next(gen_comp))
#print(next(gen_comp))
#print(next(gen_comp))
#print(next(gen_comp))
#print(next(gen_comp))
for item in gen_comp:
    print(item)

#import sys

#print(sys.getsizeof(my_list))
#print(sys.getsizeof(gen_comp))