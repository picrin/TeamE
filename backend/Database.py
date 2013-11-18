import sqlalchemy
from Design import Base, User, Course, Exam, ClassSession, UserHasExam, Attendance, UserHasCourse
from sqlalchemy.orm import sessionmaker, relationship, join

# Change to True to print database changes
class Session(object):
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if Session.instance is None:
            Session.engine = sqlalchemy.create_engine('sqlite:///data_from_crash_course.db', echo=False)
            Session.instance = object.__new__(cls, *args, **kwargs)
            Session.session_factory = sessionmaker(bind=Session.engine)

            Base.metadata.create_all(Session.engine)
            
            return Session.instance
        else:
            return Session.instance
    
    def __init__(self):
        pass
    
    def __enter__(self):
        #db_session.configure(bind=Session.engine)
        self.session = Session.session_factory()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.commit()
        self.session.close()

    def add(self, add_list):
        self.session.add_all(add_list)
    
    def verify_password(self, first_name, password):
        query =  self.session.query(User).\
                 filter(User.first_name == first_name,
                        User.password == password).all()
        return not not query

    def sessions_by_tutor(self, tutorID):
        """Returns all the sessions tutored by an specific tutor"""
        return self.session.query(ClassSession).\
                filter(ClassSession.tutor_id == tutorID)

    def sessions_by_course(self, courseID):
        """Returns all the sessions of a specific course"""
        return self.session.query(ClassSession).\
                filter(ClassSession.course_id == courseID)

    def sessions_by_student(self, courseID):
        """Returns all the sessions one student has enrolled"""
        return self.session.query(ClassSession).\
                filter(ClassSession.course_id == courseID)

    def students_in_session(self, sessionID):
        return self.session.query(User).\
                join(Attendance).\
                filter(Attendance.session_id == sessionID)

    def set_attendance(self, studentID, sessionID, attendance=None):
        return self.session.query(Attendance).\
                filter(Attendance.user_id == studentID, Attendance.session_id == sessionID).\
                update({"presence": attendance})

    def students_by_course(self, courseIDnumber):
        """Returns all the courses taken by one student"""
        return self.session.query(User).\
                join(UserHasCourse).\
                join(Course).\
                filter(Course.idnumber == courseIDnumber)

    @property
    def users(self):
        return self.session.query(User)

    @property
    def exams(self):
        return self.session.query(Exam)
    
    @property
    def courses(self):
        return self.session.query(Course)

    @property
    def attendances(self):
        return self.session.query(Attendance)    

    @property
    def user_has_course(self):
        return self.session.query(User).join(UserHasCourse)
