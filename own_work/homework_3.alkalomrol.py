# 1. feladat:
# lista műveletekkel adjatok az alább megadott üres listához tetszőleges értékeket
my_list = []
my_list.append(1)
my_list.extend(["Mate","Petra","Kinga"])
my_list.insert(2,(4,5,6))
'print(my_list)'

# 2. feladat:
# az utolsó 2 értéket módosísátok tetszőleges értékre
my_list = ["Ricsi", "Géza", "Karcsi", "Peti"]
my_list [-2] = "Ez"
my_list [-1] = "Az"
'print(my_list)'

# 3. feladat: irassátok ki a következő lista minden 2. elemét
my_list = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
my_list3 = my_list[1::2]
my_list3 = my_list [0:0:2]
'print(my_list3)'

# 4. feladat: a belső listához adjatok hozzá tetszőleges értékeket
my_list = ["Ricsi", "Peti", ["Almafa", "Peti"]]
my_list[2].append('Kortefa')
'print(my_list)'
# 4.1 a belső lista 2. elemét töröljétek
my_list[2].pop(2)
#my_list[2] = [my_list[2][0], my_list[2][1]]
'print(my_list)'

# 5. feladat: irassátok ki, hogy a 43 hanyadik indexen van
my_list = [32, 54, 43, 53, 64]
'print(my_list.index(43))'