'''
List - type

osszetett adattipus

listaban lehet
-hozzaadni elemeket
-torolni elemeket
-modositani elemeket

'''
my_list = [1,2,3, 'Mate', (1,2,3), [1,2,'Macko']]

my_list = []



##################################################
#elem hozzaadasa listahoz

#1      egyszerre 1 elemet ad hozzza           .append
my_list.append(10)
'print(my_list)'

#2      tobb elem hozzaadasa                   .extend
my_list.extend([(1,2,3,"Macko", 'Mate')])
'print(my_list)'

#3       megadott helyre egy elem beszurasa    .insert  (ez "koltseges muvelet")
my_list.insert(0, ("barack",11,7))
'print(my_list)'



##################################################
#elemek torlese
my_list = [1,2,3,4,5,6,7,8,9,10]

#index menten torles                            .pop     ha nem kap erteket, utolso elemet amugy az indexet torli
my_list.pop()
my_list.pop(4)
'print(my_list)'
del my_list[5:8]
'print(my_list)'

#ertek menten valo torles                       .remove egy utasitas csak az elso elofordulo olyan elemet torol ki
my_list.remove(1)
'print(my_list)'

#letezik meg a .clear, de az kiuriti a teljes listat



##################################################
#meglevo elem modositasa
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list[4] = "Mate"              # type: ignore A 4 indexet kicserelte
'print(my_list)'

my_list[0:3] = "korte"           # type: ignore A 0:3 indexu elemet torli es beteszi a helyere amit mi akarunk
'print(my_list)'

my_list[7:9] = ["barack","alma"] # type: ignore A 7:9 helyre betesz tobb elemet is
'print(my_list)'

##################################################
"""
a=10
b=a

print(a)
print(b)
print(id(a))
print(id(b))
"""
##################################################

#itt a masodik lista is viszi a valtozast, mert az elso listara mutat a masodik, nem az elemeire

my_list = [1,2,3,4,5]
my_list2= my_list

my_list.append(10)
my_list2.pop(0)

'print(id(my_list[1]))'
'print(id(my_list2[0]))'

##################################################

my_tup = (1,2,3,[3,4,5])

my_tup[3][1] = 10
'print(my_tup)'

##################################################

#lista a listaban

my_list = [1,2,3, ["Mate","Ricsi"], ["Mate", "Ricsi"]]
'print(id(my_list[3]))'
'print(id(my_list[4]))'
#nem egyezik meg, a ket ugyan olyan lista

my_list[3][0] = "Pisti"
'print(my_list)'

'print(id(my_list[3][1]))'
'print(id(my_list[4][1]))'

##################################################

# torold a 3-as ertekeket
my_list = [4,5,6,3,1,2,3]
my_list.remove(3)

# a 3-as ertekeket modositani 7-re
my_list = [4,5,6,3,1,2,3]
idx = my_list.index(3, 4)
my_list[idx] = 7
'print(my_list)'

