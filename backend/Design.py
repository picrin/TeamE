from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    idnumber = Column(String)
    password = Column(String)
    first_name = Column(String)
    surname = Column(String)
    student = Column(Boolean)
    lecturer = Column(Boolean)
    tutor = Column(Boolean)
    admin = Column(Boolean)
    def __init__(self, first_name, password, surname, idnumber, student=False, lecturer=False, tutor=False, admin=False):
        self.first_name = first_name 
        self.password = password
        self.surname = surname
        self.student = student
        self.lecturer = lecturer
        self.tutor = tutor
        self.idnumber = idnumber
        self.admin = admin

class UserHasCourse(Base):
    __tablename__ = 'users_has_course'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = Column(Boolean)
    lecturer = Column(Boolean)
    def __init__(self, user, course, student=False, lecturer=False):
        self.user_id = user.id
        self.course_id = course.id
        self.student = student
        self.lecturer = lecturer

class Exam(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    exam = Column(Boolean)
    assignment = Column(Boolean)
    course_id = Column(Integer, ForeignKey('courses.id'))
    def __init__(self, value, course, exam=False, assignment=False):
        self.value = value
        self.exam = exam
        self.assignment = assignment
        self.course_id = course.id

class UserHasExam(Base):
    __tablename__ = 'users_has_exams'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    exam_id = Column(Integer, ForeignKey('exams.id'))
    result = Column(Integer, nullable=True)
    def __init__(self, user, exam, result=None):
        self.user_id = user.id
        self.exam_id = exam.id
        self.result = result

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    idnumber = Column(String)
    name = Column(String)
    def __init__(self, idnumber, name):
        self.idnumber = idnumber
        self.name = name

class ClassSession(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    tutor_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)
    def __init__(self, course, name, start, end, tutor):
        self.course_id = course.id
        self.name = name
        self.start = start
        self.end = end
        self.tutor = tutor

class Attendance(Base):
    """Note: When a student enrols on a session, it is 
    stored on this table. After the session has happened
    the tutor updates the presence column"""
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_id = Column(Integer, ForeignKey('sessions.id'))
    presence = Column(String, nullable=True)
    def __init__(self, user, session, presence):
        self.user_id = user.id
        self.session_id = session.id
        self.presence = presence
