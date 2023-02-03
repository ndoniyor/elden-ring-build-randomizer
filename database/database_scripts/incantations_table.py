import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

if(path.exists(db_path)):
    remove(db_path)

incantations_connection = sql.connect('../db/incantations.db')
incantations_c = incantations_connection.cursor()
incantations_c.execute('''CREATE TABLE incantations (name)''')

incantations_csv = pd.read_csv('../csv/incantations.csv')
incantations_csv = incantations_csv.drop(["image"],axis=1)

incantations_csv.to_sql('incantations',incantations_connection, if_exists='replace', index=False)

