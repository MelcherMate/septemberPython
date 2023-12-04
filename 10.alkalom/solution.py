from uties import get_data_from_txt, write_json
from uties import (get_book_title,
                         get_page_number,
                         get_release_date,
                         count_line, 
                         count_words)

def main():
    file_path = r"/Users/matemelcher/Documents/Visual_Studio_Phyton/10.alkalom/Data/A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)
    print(data[0:10])
    statistic_dict = {
        "page_num" : get_page_number(data),
        "lines" : count_line(data),
        "words" : count_words(data),
        "release_date" : get_release_date(data),
        "title" : get_book_title(data) }

    write_json('statistic_json', statistic_dict)
if __name__ == '__main__':
    main()