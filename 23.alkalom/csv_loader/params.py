import os

url = "postgresql://postgres:postgres@localhost/postgres"
folder_path = r"/Users/matemelcher/Documents/pythonBasics/septemberPython/23.alkalom/Data"

folder_path = os.path.dirname(__file__).replace('csv_loader', 'data')

print(folder_path)