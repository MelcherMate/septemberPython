"""
Ezek lesznek az elagazasok

Ha vizsgalok valamit es el kell dontenem, hogy teljseul e a feltetelem vagy sem es utana mi tortenjen

if feltetel_vizsgalat
    utasitasok
elif masodik_feltetel_vizsgalat
    utasitasok
else:
    utasitasok

a : utan sorban a beljebb kezdest indentacionak nevezzuk 

indentacio a kovetkezo helyeken fordul elo
    -if else agak
    -ciklusok
    -fuggvenyek
    -osztalyok
az indentacio alapertelmezetten 4db space vagy 1db tabulator


"""

num = 5
num2 = 5

if num < num2:
    print(f"A {num} kissebb mint {num2}")
elif num > num2:
    print(f'A {num} nagyobb mint {num2}')
else:
    print(f"A {num} es {num2} egyenlo")

num = 6
num2 = 7
num3 = 8
if num3 > num and num2 > num3:
    print("yessir")