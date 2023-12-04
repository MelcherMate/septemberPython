"""

Static methods

Useful if zou develop a utility solution, when you
DON'T WANNA USE THE ATTRIBUTES OF THE OBJECT

@staticmethod 
-> there is no self in it

Staticmethod => can not use the attributes of the objcet
"""

class FileHandler:

    def __init__(self):
        self.price = 10_000

        # here usually set store data we gonna use a lot in further development

    @staticmethod
    def get_data_from_txt(file_path):
        with open(file_path, "r", encoding = "UTF-8") as f:
            data = f.read()

        return data    


if __name__ == '__main__':
    file_path = r"/Users/matemelcher/Documents/How_to_python/12.alkalom/Data/A Tale of Two Cities.txt"
    file_path2 = r"/Users/matemelcher/Documents/How_to_python/12.alkalom/Data/other_book.txt"
    
    test = FileHandler()

    data = test.get_data_from_txt(file_path)
    data2 = test.get_data_from_txt(file_path2)

    print(data[0:10])
    print(data2[0:10])