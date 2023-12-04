# 1. feladat: Írjatok egy olyan old style formatting template-et,
# new style formattinggal
# f' stringgel is 
# ahol
# a következő mondatot kapjátok:
# Gizi fizetése heti 50_000 Ft.


name = 'Gizi'
salary = 50_000

#old style
my_str = '%s fizetese heti %i Ft.'
'print(my_str%(name, salary))'

#new style
my_str = '{nev} fizetese heti {fizetes} Ft.'
'print(my_str.format(nev=name, fizetes=salary))'

#f'style
my_str = f"{name} fizetese heti {salary} Ft."
'print(my_str)'

##################################################################
# 2. feladat: Töröljétek a stringból a megymag szavakat. Ne használjatok mást, csak slicingot.

my_str = "egy megymag meg két megymag"

my_str = my_str[0:3] + my_str[11:19]
'print(my_str)'

##################################################################
# 3. feladat: fordítsátok meg a mondatot

my_str = "indul a görög aludni"

my_str = my_str[::-1]
'print(my_str)'

##################################################################
# 4. feladat: Minden 3. karaktert töröljétek a stringből

my_str = "33 45 55 66 77 88 99 100"

my_str = my_str[0:5] + my_str[8:14] + my_str[17:]
'print(my_str)'

##################################################################
# 5. feladat: töröljétek a www.gutenberg.org/license részt a szövegből
# 5.1 minden 8. karaktert irassátok ki
# 5.2 minden 5. karaktert töröljétek a szövegből

my_str = """This eBook is for the use of
    anyone anywhere at no cost and with
    almost no restrictions whatsoever. 
    You may copy it, give it away or
    re-use it under the terms of the Project Gutenberg License included
    with this eBook or online at www.gutenberg.org/license"""

#5.
my_str_rev = my_str[::-1]
my_str_rev =  my_str_rev[25:]
my_str =  my_str_rev[::-1]
'print(my_str)'

#5.1
my_str = my_str[8::8]
'print(my_str)'

#5.2
my_str5 = my_str[5::5]