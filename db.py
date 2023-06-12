import sqlite3
from sqlalchemy import create_engine, Column, Float, String, Date, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

#connection = sqlite3.connect("to-do_tasks.db")

#cursor = connection.cursor()

#cursor.execute("ANY SQLite3 Syntax")

#connection.commit()
#connection.close()

#  SQLAlchemy commands use without sqlite syntax

db_path = "tasks.db"
engine = create_engine(f'sqlite:///{db_path}', echo=True)
Base = declarative_base()


class Tasks(Base):
    __tablename__ = "Running tasks"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)
    progress = Column(Float)

    def __str__(self):
        return f'ID: {self.id}, TASK: {self.task}, DEADLINE: {self.deadline}, PROGRESS: {self.progress}'


# Create the tables
Base.metadata.create_all(engine)

#Session = sessionmaker(bind=engine)
#session = Session()


#def add_new_task(task_info, deadline, progress):
    #task = Tasks(task=task_info, deadline=deadline, progress=progress)  # here will be output from backend
    #session.add(task)
    #session.commit()
    #session.close()


def remove_task():
    pass

# Close the session



