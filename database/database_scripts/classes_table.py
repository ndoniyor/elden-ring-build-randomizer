import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

classes_connection = sql.connect(db_path)
classes_c = classes_connection.cursor()
classes_c.execute('''CREATE TABLE classes (name)''')

classes_csv = pd.read_csv('../csv/classes.csv')

classes_csv.to_sql('classes',classes_connection, if_exists='replace', index=False)

