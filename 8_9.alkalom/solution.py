"""
Every .py file is an object
Every .py file is also a modul -> inportable codes and variables into an other file 

possible file routine fails:
1. the path does not exists
2. the file des not exists

"""
import os

def get_data_from_txt1(file_path):
    if os.path.exists(file_path):

        if os.path.isfile(file_path):
            
            with open(file_path,'r', encoding='utf-8') as f:
                book = f.read()
            
            return book



# it is a good solution but we need to reduse the number of indentation level if possible  
# with 'not' we can solve our problem with the indentation level
# with 'raise Exception' I can throw an Error with the text I want

    if not os.path.exists(file_path):
        raise Exception(f'Given pathway: "{file_path}" does not exists')
    if not os.path.isfile(file_path):
        return   
    with open(file_path,'r', encoding='utf-8') as f:
        book = f.read()
    return book

"""
Error solve:

try:
    try to run
exept:
    if there is an error what to do
finally:
    this is gonna run every time, no matter we do have an error or not

"""
def get_data_from_txt(file_path):
    book = None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            book = f.read()
    except OSError as o_er:
        print(f"OSError: {o_er}")        
    except Exception as err:
        #raise Exception(f"{err}")
        print(f'Exception: {err}')
    finally:
        print("Always runs even the program stopped before")

    return book

if __name__ == '__main__':
    file_path = r"/Users/matemelcher/Documents/Visual_Studio_Phyton/8.alkalom/Data/A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)





    
