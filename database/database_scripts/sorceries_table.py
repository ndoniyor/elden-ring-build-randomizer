import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'


sorceries_connection = sql.connect(db_path)
sorceries_c = sorceries_connection.cursor()
sorceries_c.execute('''CREATE TABLE sorceries (name)''')

sorceries_csv = pd.read_csv('../csv/sorceries.csv')

sorceries_csv.to_sql('sorceries',sorceries_connection, if_exists='replace', index=False)

