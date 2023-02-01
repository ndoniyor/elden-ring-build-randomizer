import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/talismans.db'

if(path.exists(db_path)):
    remove(db_path)

#id,name,image,description,attack,defence,scalesWith,requiredAttributes,category,weight
talismans_connection = sql.connect('../db/talismans.db')
talismans_c = talismans_connection.cursor()
talismans_c.execute('''CREATE TABLE talismans (name)''')

talismans_csv = pd.read_csv('../csv/talismans.csv')
talismans_csv = talismans_csv.drop(["image"],axis=1)

talismans_csv.to_sql('talismans',talismans_connection, if_exists='replace', index=False)

