"""
Stringek

A Stringek unmutable (megvaltoztathatatlan) adattipusok
A my_str valtozot lehet varialni, de egy a benne megadott adatot nem lehet megvaltoztatni

A Stringek iterálható objektumok
Egy String felbontható kisebb egységekre, karakterekre

Alapveto String muveletek:
-osszevonas
-osszehasonlitani (elagazasoknal majd elojon)
-slice-olni
-formazzuk oket

"""

my_str = 'Ez egy string'
my_str = "Ez is egy string"

#String összevonás

#1 + jellel
my_str = "alma"
my_str2 = "fa"
my_str3 = my_str + my_str2
print(my_str3)

my_str3 = my_str +"-"+ my_str2
print(my_str3)
#ezt string konkatenacionak hivjuk (erre lesz meg 5 modszer kesobb, 3 at ebben a fileban)

#String multiplikálás
my_str4 = 5 * my_str
print(my_str4)

#####################################################################################################
#slice-olni
#ez szeletelést jelent
#a stringben minden karakter kap egy indexszamot, a 0 val kezdve (pl az almaban az elso 'a' indexe 0)

"""
my_str = 'akarmi'

my_str = [honnan:meddig:lepes_merteke]
pl: my_str = [0:4:2]

a meddig eseteben azt a szamu karaktert mar amit oda irok mar nem fogja kiadni
"""
my_str = "indul a gorog aludni"
print(my_str[0:2:2])
print(my_str[0])
print(my_str[8:13])
#ha az utolso karaktert akarom kiiratni  (itt mar nem kell hozzaadni a plusz 1-et a meddighez)
print(my_str[19])
#ha az utolso szot akarok kiirni
print(my_str[14:])

print(my_str)
print(my_str[:])
print(my_str[::])
'''

#ha nem tudjuk, milyen hosszu a string
'''
my_str = "indul a gorog aludni"
print(my_str[-6:])
print(my_str[-1:-3:-1])
print(my_str[::-1])  #ezzel lehet megforditani a stringet

########################################################################################################

my_str = "indul a gorog aludni"

#my_str[3] = k  ez lenne az, hogy az ertek karakatere megvaltozzon
#hogy irom at a gorogot torokre?

my_str2 = 'torok'
my_str = my_str[0:8] + my_str2 + my_str[13:] 
# my_str = my_str[0:8] + 'torok' + my_str[13:]     igy is mukodne
print(my_str)

