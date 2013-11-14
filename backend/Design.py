from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

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
    student_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    def __init__(self, course, student):
        self.course_id = course.id
        self.student_id = student.id

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, name):
        self.name = name

#TODO Bruno, I don't understand this code -- Adam
user_has_exam = Table('user_has_exam', Base.metadata,
                      Column('user_id', Integer, ForeignKey('users.id')),
                      Column('exam_id', Integer, ForeignKey('exams.id')))


