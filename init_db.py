import sqlite3

connection = sqlite3.connect('database.db')

with open('LAB_sqlite_fixed.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()