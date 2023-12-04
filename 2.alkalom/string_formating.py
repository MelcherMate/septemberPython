#STRING FORMAZASA

# 1. formazasi modszer          'old' style formatting
'''
# Mate vagyok es 23 eves
name = "Mate"
age = 23
#ezt a modszert onnan ismerjuk meg, hogy % jelek vannnak a kodban
my_str = "%s vagyok es %f eves"
print(my_str %(name, age))
'''
##################################################################################################################
# 2. formazasi modszer          'new' style formatting

name = 'mate'
age = 23
 
my_str = "{nev} vagyok es {kor} eves"

print(my_str.format(nev=name, kor=age))
#ennek az elonye, hogy a nevhez koti a valtozot, igy nem kell a sorrendre figyelni

##################################################################################################################
# 3. formazasi modszer          'String interpolacio'   f'string

name = 'mate'
age = 23
 
my_str = f"{name} vagyok es {age} eves"
my_str = f"{name} vagyok es {5*age} eves"

print(my_str)

'''
Ha mar van valtozom akkor az f'string et erdemes hasznalni, ha majd kesobb akarok erteket adni a valtozonak akkor a new style celszerubb
'''

