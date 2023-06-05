import sqlite3
from sqlalchemy import create_engine

connection = sqlite3.connect("to-do_tasks.db")

cursor = connection.cursor()

cursor.execute("ANY SQLite3 Syntax")

connection.commit()
connection.close()

#  SQLAlchemy commands use without sqlite syntax
