import pandas as pd

class FileHandler:
    def __init__(self):
        ...

    # instance method - instance function
    def get_data_from_csv(self, file_path):
        data = pd.read_csv(file_path)
        return data
    
    def map_dataframe_to_postgers (self, df: pd.DataFrame): # df -> DataFrame

        df = df.replace([r'\N'], None)
        columns = df.dtypes.to_dict()
        # print(columns)
        postgres_dtypes = {}
        for col, dtype in columns.items():
            if str(dtype) == 'int64':
                postgres_dtypes[col] = 'bigint'
            elif str(dtype) == 'object':
                # itt kellene dátumot megvizsgálni
                # itt kellene a float adattípust megvizsgálni
                try:
                    # integerré alakítom
                    df[col] = df[col].astype('int64', errors='raise')
                    postgres_dtypes[col] = 'bigint'
                    print(f"Siker integer: {col}")
                    continue
                except Exception as e:
                    # print(f"{col} - {str(e)}")
                    postgres_dtypes[col] = 'text'
                try:
                    # floatá alakítom
                    df[col] = df[col].astype('float')
                    postgres_dtypes[col] = 'numeric'
                    print(f"Siker float: {col}")
                    continue
                except Exception as e:
                    # print(f"{col} - {str(e)}")
                    postgres_dtypes[col] = 'text'
                try:
                    # dátummá alakítom
                    df[col] = df[col] = pd.to_datetime(df[col])
                    postgres_dtypes[col] = 'date'
                    print(f"Siker date: {col}")
                    continue
                except Exception as e:
                    # print(f"{col} - {str(e)}")
                    postgres_dtypes[col] = 'text'
        return postgres_dtypes, df
    
    def generate_create_and_insert_script(self, dtypes: dict):
        print("#######################################")
        create_script = "create table if not exists {table_name} ("
        insert_script = "insert into {table_name} ("
        insert_values = "values ("
        
        for col, dtype in dtypes.items():
            create_script += f"{col} {dtype},\n"
            insert_script += f"{col}, "
            insert_values += f":{col,} "
        
        create_script = create_script[0:-2] + ')'

        insert_statement = insert_script[0:-2] + ') \n' + insert_values[0:-2] + ')' 

        return create_script, insert_statement


if __name__ == '__main__':
    file_path = r"/Users/matemelcher/Documents/pythonBasics/septemberPython/23.alkalom/Data/circuits.csv"
    test = FileHandler()
    data = test.get_data_from_csv(file_path)

    pd_dtype = test.map_dataframe_to_postgers(data)
    
    cre_script, insert_script = test.generate_create_and_insert_script(pd_dtype)

    import os
    file_name = os.path.basename(file_path)[0:-4]

    print(file_name)

    cre_script = cre_script.format(table_name=file_name)
    insert_script = insert_script.format(table_name=file_name)
    
    print(cre_script)
    print(insert_script)
