import sqlite3
from sqlalchemy import create_engine, Column, Float, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

connection = sqlite3.connect("to-do_tasks.db")

cursor = connection.cursor()

cursor.execute("ANY SQLite3 Syntax")

connection.commit()
connection.close()

#  SQLAlchemy commands use without sqlite syntax

db_path = ""
engine = create_engine(f'sqlite:////{db_path}', echo=True)
Base = declarative_base()


class Tasks(Base):
    __tablename__ = "Running tasks"
    task = Column(String)
    deadline = Column(Date)
    progress = Column(Float)






