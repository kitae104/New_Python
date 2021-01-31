import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("test.db")
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()