"""
Data Engineering

It works with data integration

A data engineer developes data pipelines:
    - they send raw data into a database
    - the pipeline is the collection of code and tools used to develop de routes for data to database

Bach based processing:
    - disciplined processing (daily, monthly, ...

Realtime data integration (near realtime):
    - contignous data integration -> data streaming technology

Data processing also has 2 categories: (this step is when the data reaches the database)
    
    - ETL - Extract Transform Load
    - ELT - Extract Load Transform

    1, Extract: source data extraction: file, database etc. : when you bring the data for integration
    2, Transform:
        - data cleaning: ex: -what happens with missing data?
                             -date view settings
        - integrate the data into the datamodell
            - unique keys set up
            - child - parent connections 
    3, Load: Integrate the data into its final place ("insert" command)

"""

from sqlalchemy import create_engine, text

# 1st step: Connect the backEnd and the dataBase
# URI - URL
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

# 2nd step: create a session


'''
with engine.connect() as conn:
    conn.execute(text("create table if not exists python_test_tab (id serial, name text)"))

    for item in range(50):
        conn.execute(text("insert into python_test_tab (name) values ('Ripley')"))
    
    conn.commit()
'''



"""
Round trip: the SQL command goes to the database, than runs there at the database and comes back with the solution)
LESS roundtrips is BETTER
"""



"""
here is the solution for using only one roundtrip for the same problem
"""
import time 

start_t = time.time()
with engine.connect() as conn:
    # :name -> bind változó -> sql-ben ennek helyére tudsz behellyettesíteni adatot
    # így nem kell foglalkoznod az adat típussal
    insert_statement = "insert into python_test_tab (name) values (:valami)"
    name_dict = []
    for item in range(50):
        name_dict.append({"valami": 'Ripley'})
        
    conn.execute(text(insert_statement), name_dict)
    conn.commit()
    
    print(f"finished: {time.time() - start_t}")


select_statement = "select * from python_test_table"
with engine.connect() as conn:
    result = conn.execute(text(select_statement))
    data = result.fetchall()
    print(data[0:100])