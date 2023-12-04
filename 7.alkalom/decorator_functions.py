"""
Decorator functions

Decorator functions gives extra attribut to other functions without
changeing the original functions

When should we use it???

    i wanna create automated log
    i wanna mesure runtime 
    debug
    i wanna make the run slower
    caching mechaics

"""
'print()' # instantiation

'printer = print' # give value -> reference
                #            -> I can append functions to variables
                #            -> I can give funcitons as reference to other functions
'printer(1)' # printer calls the print function and works just as print

#def my_func(func, val):
#    func(val)

#my_func(print, "Mate")



#######################################
######## function in function #########

"""
i can't call the inner fucntion from outside
"""
# HF A MASIK 3 ALAP MATEK MUVELET

def calculator(num1, num2, operand):
    def add():
        return num1 + num2
    
    if operand == '+':
        return add()

temp = calculator(10, 5, '+')
print(temp)


######## decorator functions #########

def start_end_decor(func):
    def wrapper():
        print("strat")
        func()
        print("end")
    wrapper()

### this move is the function decoration
'''
@start_end_decor
def my_func():
    num = 10
    while num > 0:
        print()
        num -= 1


start_end_decor(my_func)
'''

###########################################
####### type cast #######
# hol long is my list?
def how_long(func):
    def wrapper(*args, **kwargs):
        sol = func(*args, **kwargs)
        print(len(list(kwargs.values())[0]))
        if len(args) > 0:
            length = (len(args[0]))
        else:
            length = len(list(kwargs.values())[0])
        print(f"A func paremeter hossza {length}")
        
        return sol
    return wrapper

@how_long
def my_func(my_list):
    temp = []
    for item in my_list:
        if not item%2 == 0:
            temp.append(item)
    return temp

list1 = [1, 2, 3, 4, 5, 6]

# args based
sol = my_func(list1)
print(sol)

# kwargs based
sol = my_func(my_list=list1)
print(sol)