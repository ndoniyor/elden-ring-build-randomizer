import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

incantations_connection = sql.connect(db_path)
incantations_c = incantations_connection.cursor()
incantations_c.execute('''CREATE TABLE incantations (name)''')

incantations_csv = pd.read_csv('../csv/incantations.csv')

incantations_csv.to_sql('incantations',incantations_connection, if_exists='replace', index=False)

