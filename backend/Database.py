import sqlalchemy
from Design import Base, User, Course, Exam, ClassSession, UserHasExam, Attendance, UserHasCourse
from sqlalchemy.orm import sessionmaker, relationship, join

# Change to True to print database changes
class Session(object):
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if Session.instance is None:
            Session.engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
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
    
    def students_by_course(self, course_idnumber):
        return self.session.query(Course).\
                    join(UserHasCourse).\
                    filter(Course.id == course_idnumber)
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
