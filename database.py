import csv, sqlite3
import pandas as pd

path_base = (r'/home/chase/repos/DS--Data-Engineering-/cannabis.csv')
df = pd.read_csv('https://raw.githubusercontent.com/gptix/DS--Data-Engineering-/master/data/cannabis.csv')


col_list = list(df.columns)
col_list
to_db_cols_str = ""
for col in col_list:
    to_db_cols_str += f'i[\'{col}\'], '
to_db_cols_str = "to_db = [(" + to_db_cols_str[:-2] + ") for i in dr]"



col_string = str(list(df.columns))[1:-1]

create_table_string = f'CREATE TABLE IF NOT EXISTS cannabis ({col_string});'
print(create_table_string)
con = sqlite3.connect('cannabis.sqlite3')
cur = con.cursor()
cur.execute(create_table_string) 
with open(path_base,'r') as file_in:
    dr = csv.DictReader(file_in) 
    to_db = [(i['Strain'], i['Type'], i['Rating'], i['Effects'], i['Flavor'], i['Description']) for i in dr]

cur.executemany(f"INSERT INTO cannabis ({col_string}) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()



import os
os.getcwd()