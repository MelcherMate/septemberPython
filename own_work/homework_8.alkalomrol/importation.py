"""
iport the book
"""

def get_data_from_txt(file_path):
    book = None
    with open(file_path, "r", encoding="utf-8") as f:
            book = f.read()
    return book

file_path = r"/Users/matemelcher/Documents/How_to_python/data_files/data/Adventures of Huckleberry Finn.txt"
data = get_data_from_txt(file_path)
