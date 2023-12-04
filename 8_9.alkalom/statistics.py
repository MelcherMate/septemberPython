'''

Statistics:
    - how many pages does the book have? (1 page 3000 caracters)
    - when was the book publised?
    - what is the TITLE of the book?
    - how much world does the book contains?
    - how much rows does the book have?

prototype function example:    
def get_page_number():
    pass

    
If I inport a modul in a function I only can use the modul in that function.
If I want to use the modul again, I need to import it again
This is called LOCAL and GLOBAL import


 '''
from solution import get_data_from_txt

def get_page_number(book_data):
    import math
    return math.ceil (len(book_data)/3000)

def get_release_date(book_data):
    #release_date = book_data.split('Release Date:')
    #print(release_date[1].split('\n')[0])
    
    release_date = book_data.splitlines()

    for item in release_date:
        if 'Release Date:' in item:
            return item.replace('Release Date:', '')

def get_book_title(book_data):
    title = book_data.split('Title: ')
    print(title[1].split('\n')[0])
    return len(title)

def count_words(book_data):
    words = book_data.split()
    return len(words)

def count_line(book_data):
    lines = book_data.splitlines()
    return len(lines)


if __name__ == '__main__':
    file_path = r"/Users/matemelcher/Documents/Visual_Studio_Phyton/8.alkalom/Data/A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)

    page_num = get_page_number(data)
    lines = count_line(data)
    words = count_words(data)
    title = get_book_title(data)
    release_date = get_release_date(data)



