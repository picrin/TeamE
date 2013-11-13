from sqlalchemy import Table, Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base)
	__tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    password = Column(String)
    surname = Column(String)
    student = Column(Boolean)
    lecturer = Column(Boolean)
    tutor = Column(Boolean)

class Exam(Base)
	__tablename__ = 'exams'
    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'))

class Course(Base)
	__tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

user_has_exam = Table('user_has_exam', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('exam_id', Integer, ForeignKey('exam.id'))
)