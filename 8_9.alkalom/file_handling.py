"""
File operations

1. step:    somehow we need to open the file
2. step:    we do the file operation (pl: add data, delete some part)
3. step:    close the file when i finish

"""

# open the file
# open(file_name, 'opening_mode')
# we have 6 different opening modes (easy to find online)

# Python uses UNICODE caracters by default
# by encodeing we can give caracter basis to python

file_path = r"/Users/matemelcher/Documents/Visual_Studio_Phyton/8.alkalom/Data/A Tale of Two Cities.txt"
data = open(file_path,'r', encoding='utf-8')

book = data.read()

data.close()

print(book)

##############################################################################

# context manager #
# it takes over some task from us and does those for us
# should use: -> file operations, -> database connection management

with open(file_path,'r', encoding='utf-8') as f:
    book = f.read()

print(book[0:1000])
# this is a better, widely used method to open data
##############################################################################
