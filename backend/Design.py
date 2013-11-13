from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=False) # Change to True to print database changes

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    password = Column(String)
    surname = Column(String)
    student = Column(Boolean)
    lecturer = Column(Boolean)
    tutor = Column(Boolean)

    def __init__(self, first_name, password, surname, student, lecturer, tutor):
                self.first_name = first_name 
                self.password = password
                self.surname = surname
                self.student = student
                self.lecturer = lecturer
                self.tutor = tutor

class Exam(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'))

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

user_has_exam = Table('user_has_exam', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('exam_id', Integer, ForeignKey('exams.id'))
)

# Creates the tables
Session = sessionmaker(bind=engine)
session_db = Session()          
Base.metadata.create_all(engine)