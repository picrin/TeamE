import sqlalchemy
from Design import User, Course, Exam, Base
from sqlalchemy.orm import sessionmaker, relationship, join

# Change to True to print database changes
class Session(object):
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if Session.instance is None:
            Session.engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=False)
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
    
    def students_by_exam(self, exam_name):
        return self.session.query(User).\
                    select_from(join(User, Exam).join(Course)).\
                    filter(Course.name == exam_name)
    @property
    def users(self):
        return self.session.query(User)

    @property
    def exams(self):
        return self.session.query(Exam)
    
    @property
    def courses(self):
        return self.session.query(Courses)
    
