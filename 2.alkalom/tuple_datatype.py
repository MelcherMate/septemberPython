'''
TUPLE

Egy osszetett adattipus

inmutable
iteralhato
indexei vannak   -> sliceolni lehet
lehet benne kulonbozo tipusu adatfajta   ugy kell elkepzelni mint egy kosarat

nem lehet
-elemet hozzaadni
-elemet modositani
-elemeto torolni


'''
#vegyuk ki a Matet
import sys

my_val = 3
my_val2 = 3
my_tup = (1, my_val2, 'Mate', 'Ricsi')

#my_tup = my_tup[0:2] + (my_tup[-1],)

my_val=4
my_val2=10

print(id(my_val))
print(id(my_val2))
print(id(my_tup[1]))
