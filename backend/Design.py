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
    result = Column(Integer)
    def __init__(self, user, exam, result):
        self.user_id = user.id
        self.exam_id = exam.id
        self.result = result

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    idnumber = Column(String)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    tutor_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    def __init__(self, idnumber, name, lecturer=None, tutor=None):
        if lecturer == None:
            lecturer_id = None
        else:
            lecturer_id = lecturer.id
        if tutor == None:
            tutor_id = None
        else:
            tutor_id = tutor.id
        self.idnumber = idnumber
        self.name = name
        self.lecturer_id = lecturer_id
        self.tutor_id = tutor_id

class ClassSession(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    name = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)
    def __init__(self, course, name, start, end):
        self.course_id = course.id
        self.name = name
        self.start = start
        self.end = end

class Attendance(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_id = Column(Integer, ForeignKey('sessions.id'))
    presence = Column(String)
    def __init__(self, user, session, presence):
        self.user_id = user.id
        self.session_id = session.id
        self.presence = presence
