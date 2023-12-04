"""
Zip function

it goes along the given objects and picks out 1 objects from each list
and puts them into tuples based on their indexes

it goes only until it reaches the end of the shortest list

"""

my_list = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8, 9, 10]

sol = list(zip(my_list, my_list2))
print(sol)

# i can make dictionaries out of it makeing key value pares

sol2 = dict(zip(my_list, my_list2))
print(sol2)