"""
Python funcions development

funcions starts with def fuggveny_neve(opcionalis parameterlista):
    commands
    optional return_value

Mire valo a fuggveny?
Ismertlodo muveletek eseten a redundancia azaz ismetlodes megszuntetesere.
A mar lefejlesztett fuggvenyt barmikor ujra tudom hasznalni, komplex logikat tudok benne megvalositani. 
A futtatasa soran lehetoseg van ezt a logikat elfedni.



"""
a = 10

def my_func():
    print("Hello")

# my_func()

def my_func():
    print("almafa")

# when we type my_func() for python it means: "create an object, named my_func"
# meaning: run commands in my_func

# you can give a new meaning for an existing funcion it is POSSIBE BUT NOT RECOMMENDED# A PYTHON MEGENGEDI, HOGY BEEPITETT FUGGVENYEKET ES MODULOKBOL SZARMAZO FUGGVENYEKET IS FELUL TUDJUNK DEFINIALNI
#### DO NOT DO THIS ####
'''
def print():
    10 + 20

print("Szia")
'''



"""
funcion parameters

In python funcions can have start arguments, there are no name, type or value limit for start arguments
"""
# must give parameters
# we must give values aslo 'a' and 'b' cause they are divided by ','
def add_numbers(a, b):
    print(a + b)

# position based argument (in order is important)
add_numbers(10, 20)

# keyword argument (in order is not important)
'add_numbers(a=15, b=25)'
'add_numbers(b=25, a=15)'

########################################################################

'''
Parameters with start values
'''
# if I don`t necessary wanna give 2 values (here I gave a start value to num2)
# if a parameter gets start value than i must give start value to the following ones
def add_numbers(num1, num2=0):
    print(num1 + num2)

add_numbers(10)

########################################################################

"""
Type hint

def my_func(a: int, b: str):
    pass
we can help the function defineing what kind of parameters
we want for an object

hint does not effect the work of the fuction

it is used when someone else gonna use the code and i wanna help him
it is just for beauty
"""

# def my_func(a int = "Mate", b: str = 10):

########################################################################

'''
Funcions return value

every funcion has a return value

If you do not have return vakue, you are going to get None value
If i use "return" i can give return value
Right after 'return' you can not use code again. You can go back to runing code
'''
# wrong example
def add_numbers(a, b):
    #print(a + b)
    pass

temp = add_numbers(10, 20)

print(temp)

# good example
def add_numbers (a, b):
    if a > b:
        return a + b
    return {"osszeg": a + b}
    print("barmint")
temp = add_numbers(10,20)

print(temp)

# it is going to use packing
# by adding to variables to save the 2 values what the funcion gives us, we can avoid pacing and tuples
# * - is asterix operator
# * ahead of a variable means PACK IN!

def add_numbers(a, b):
    #packing
    return a + b, {"value": a + b}
#unpacking
temp, *temp2 = add_numbers(10, 20)

print(temp, temp2)
#this way it made a tuple

########################################################################

'''
Funcion overolading

used when we need more funcions under a same valuable, wich we can use separetly

Function overloading is a feature of object-oriented programming where two or more functions can have the same name but different parameters
In python it is not possible by default

but we have a solution for this problem
'''
# *args - packs positions based parameters into tuples
def my_func(*args):
    if len(args) == 1:
        print('1 item')
    else:
        print(f"{len(args)} item")    

# if we give values with "," it is a positions based value giving
my_func(2,4,3,5,6,7,8,9,10)

###############

# **kwargs - based on keyword arguments
def my_func (**kwargs):
    if kwargs.get('name'):
        print(kwargs.get('name'))
    
    if kwargs.get('color'):
        print('Nincs benne a color')

my_func( a=10, name="Mate", age=23, salary=None)

########################################################################

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
my_func(1, 2, 3, 4, name="Mate", price=50_000)
