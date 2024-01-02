import os

from csv_loader.file_handler import FileHandler
from csv_loader.db_handler import DatabaseHandler
from csv_loader.params import url, folder_path


def main():

    file = FileHandler()
    sql = DatabaseHandler(url)

    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)

        data = file.get_data_from_csv(file_path)

        pd_dtype, df = file.map_dataframe_to_postgers(data)
        
        cre_script, insert_script = file.generate_create_and_insert_script(pd_dtype)

        file_name = os.path.basename(file_path)[0:-4]

        print(file_name)

        cre_script = cre_script.format(table_name=file_name)
        insert_script = insert_script.format(table_name=file_name)
        
        sql.run_sql(cre_script)
        sql.run_sql(insert_script, df.to_dict(orient="records"))


if __name__ == '__main__':
    main()