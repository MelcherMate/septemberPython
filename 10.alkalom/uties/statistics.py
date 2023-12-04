# 1. possiple solution, but not nice
'''
if __name__ == '__main__':
    from file_handler import get_data_from_txt
else:
    from uties.file_handler import get_data_from_txt
'''
# 2. wrong solution for import, but works
"""
import sys
sys.path.append(r"/Users/matemelcher/Documents/Visual_Studio_Phyton/8.alkalom/Data/A Tale of Two Cities.txt")
from uties.file_handler import get_data_from_txt
"""

# but here we don't need to import the "get_data_from_txt"

def get_page_number(book_data):
    import math
    val = 10
    return math.ceil(len(book_data)/3000)

def get_release_date(book_data):
    release_date = book_data.splitlines()
    for item in release_date:
        if 'Release Date:' in item:
            return item.replace('Release Date:', '')

def get_book_title(book_data):
    title = book_data.split('Title: ')
    return title[1].split('\n')[0]

def count_words(book_data):
    words = book_data.split()
    return len(words)

def count_line(book_data):
    lines = book_data.splitlines()
    lines = [item for item in book_data.split('\n') if item != '']
    return len(lines)