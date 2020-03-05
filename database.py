"""Convert CSV file into usable PostgreSQL database on Elephant SQL."""
import sqlite3
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Create postgres connection
pg_conn = psycopg2.connect(
    dbname=os.getenv("DBNAME"), user=os.getenv("USER"),
    password=os.getenv("PASSWORD"), host=os.getenv("HOST")
    )
pg_curs = pg_conn.cursor()


# list of dataset columns we want in the db
needed_columns = []


# importing the dataset
df = pd.read_csv('', sep='%')


df_new = pd.DataFrame()


# creating a dataframe with just the above columns
for item in needed_columns:
    df_new[item] = df[item]

# Replace NaNs with NULL to comply with SQL
df_new = df_new.fillna('NULL')

# initalizing the database
sl_conn = sqlite3.connect('med_cabinet.db3')
sl_curs = sl_conn.cursor()

# putting the trimmed dataframe into the database
df_new.to_sql('strain_info', con=sl_conn, if_exists='replace')

# sl_curs.close()
sl_conn.commit()

print('Conversion was successful!')

# Create queried object of all data
query = """ SELECT * FROM strain_info; """
strains_sql = sl_curs.execute(query).fetchall()

# Create insert debugger
# import pdb; pdb.set_trace()

# Create postgreSQL table
create_strains_table = """
    CREATE TABLE strains (
#  
# strain id (primary key)
# strain name 
# strain type 
# strain rating 
# strain description 
# strain effect 
# strain flavors        
    )
    """
pg_curs.execute(create_strains_table)
pg_conn.commit()

# Insert data into table
for strain in strains_sql:
    insert_strain = """
    I """ + str(strain) + ";"
    pg_curs.execute(insert_strain)

# Commit changes
pg_conn.commit()

print('PostgreSQL table creation was successful!')