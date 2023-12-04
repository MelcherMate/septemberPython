"""
Loop-ok - Ciklusok

Valahany darabszor szeretnenk bizonyos ciklusokat leforditani

2 fele ciklus letezik
    - for loop
    - while loop

while loop:
    - lassabb mint a for loop
    - tipikusan event alapu elemeknel szokas hasznalni
    - pl: addig fuss, ameddig veget nem er az adott kuldetes

for loop:
    - iterable object-ek bejarasa
    - van egy listam amibol ki akarok venni 1 tulajdonsagu elemeket
    - valahany darabszor fusson le 1 vagy tobb utasitas
    - ezt ajanlottabb hasznalni
    - egyszerubb a hasznalata

"""

#WHILE loop

"""
while feltetel_amig_igaz:
    futasi logika
"""
"""
num = 3

while num > 0:
    'print(f'{num}')'
    num = num - 1
"""
##############################
#FOR loop

"""

for cuklus_valtozo in iterabel_object:
    utasitasok

"""
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    # print(item)
    pass # ures utasitas

#print(Mate)

 #############################
my_list = ['Mate', 'Petra', 'Kinga', 'Zoli']

# ciklus vezerlese
# azt szeretnem, ha a ciklus eler egy adott elemig, akkor kilepjen a ciklus
# ezt a ciklust mar tovabb folytatni nem lehet itt

for item in my_list:
    #print(item)
    if item == 'Kinga':
        break


####
# contignue - a kovetkezo iteraciora ugrik
# itt at amikor elertem egy adott elemet, akkor azt kihagytam es folytattam a kovetkezo elemmel
my_list = ['Mate', 'Petra', 'Kinga', 'Zoli']

for item in my_list:
    if item == 'Petra':
        continue

    #print(item)


####

#ha tudni akarom, hanyadik elemnel jar a ciklusom

my_list = ['Mate', 'Petra', 'Kinga', 'Zoli']

# 1 lehetoseg, igye betettem egy szamlalot
cnt = 0
for item in my_list:
    cnt += 1
    #print(f"{cnt}. iteracio")

##################################################


## toroljunk minden paros szamot a listabol
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [2, 4, 3, 8, 5, 6, 7, 10, 9, 1]
# (item%2) ez a maradekot fogja visszaadni
# az enumerate fuggvenyt visszaadja, hogy (melyik_index, mennyi_az_erteke) tuple-okat hoza letre
# unpacking -> kicsomagolas   Azzal, hogy ket elemet tettem a ciklusba, szetszedte az ertekeket kulon elemekbe

temp = []
for idx, item in enumerate(my_list):
    #print(f"{item}: indexe {idx}")
    if (item%2)!=0:
        temp.append(item)
my_list = temp
#print(my_list)

#ha ciklussal vizsgalunk 1 listat, NEM SZABAD FUTASI IDOBEN TOROLNI A LISTABOL, mert az indexertekek miatt ki fog hagyni elemeket a listabol

############################################
# minden erteknek vagyuk a 3 szorosat

my_list = [2, 4, 3, 8, 5, 6, 7, 10, 9, 1]
my_list[0] = 6

for idx, item in enumerate(my_list):
    my_list[idx] = item * 3
#print(my_list)

##################################################################
# A LISTAKHOZ HA CSAK LEHET NEM ADOK HOZZA VAGY VESZEK EL ELEMET #
##################################################################

my_list = []

for item in my_list:
    print(item)
else:
    print("A lista ures")

# itt az else azt jelenti, hogy ha lefutott a for ciklus akkor a vegen csinalja amit irtunk oda
# ritkan hasznalatos, ha kesz a ciklus siman elvegezhetem az utana jovo muveletet kulon
 
print('###############################################')

my_list = []

for item in my_list:
    print(item)
    break
print("A lista ures")



