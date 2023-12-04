 """
Dictionary = "szotar"
Akkor hasznaljuk, ha back end-bol az adott adatot szeretnenk majd a front end-nek odaadni szamukra erthetoen

my_dict = {} kulcs-ertek parokat adok meg

kulcs => mindig egyedi, nem lehet ugyan olyan nevu kulcs 1 szinten

mutable datatype:
    lehet hozzaadni kulcs-ertek parokat
    lehet torolni kulcs-ertek parokat
    lehet modositani kulcs-ertek parokat

Ez is iterable object
"""

my_dict = {
    "color" : "white",
    "brand" : "tesla",
    "price" : 48000,
}

'print(my_dict["brand"])'
'print(my_dict["color"])'
'print(my_dict[0])  '       #itt most a 0-adik elemre voltam kivancsi

####################################################################

#Manipulations:

####################################################################

# uj kulcs-ertek hozzaadasa
my_dict = {
    "color" : "white",
    "brand" : "tesla",
    "price" : 48000,
}
# 1. 
my_dict["shop"] = "Budapest"
'print(my_dict)'
# 2.
my_dict.update({"motor_type" : "benzin", "name" : "Mate"})
'print(my_dict)'

# meglevo kulcs modositasa
my_dict = {
    "color" : "white",
    "brand" : "tesla",
    "price" : 48000,
}
# 1.
my_dict["color"] = "red"
my_dict["Color"] = "yellow"
# 2.
my_dict.update({"brand" : "Mercedes", "price" : 200_000 })
'print(my_dict)'

#kulcs-ertek par torlese
my_dict = {
    "color" : "white",
    "brand" : "tesla",
    "price" : 48000,
}
# 1. 
'my_dict.clear()    #torli az osszes kulcserteket'
# 2. 
my_dict.pop("color")
# 3.
my_dict.popitem()  #az utolso kulcserteket torli
# 4.
del my_dict ['brand']
#print(my_dict)

####################################################################
#Bonyolultabb dictionary-k

my_dict = {
    "subjects": {
        "irodalom" :{
            "tanar" : "Kati neni",
            "orak" : ["hetfo, kedd"]  
            },
        "matek" :{
            "tanar" : "Feri ba",
            "orak" : ["kedd", "szerda"]
            },
        "tesi" :{
            "tanar" : "Joco ba",
            "orak" : ["hetfo","pentek"]
        }
    }  
}

#print(my_dict["subjects"]["matek"]["orak"][1])
#print(my_dict["subjects"]["tesi"]["tanar"])



# életszerű példát:
my_dict2 = {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}

print(my_dict2["problems"][0]["Diabetes"][0]["medications"][0]["medicationsClasses"][0]["className"][0]["associatedDrug"][0]["strength"])

print(my_dict.keys())
print(my_dict.values())