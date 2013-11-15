from backend import User, Course, Exam, Session
from datetime import datetime
# quick crash course on working with the backend

# ================================ Example 1 ==================================
# this block automagically opens and closes the connection to the database.
# before closing the connection it automatically flushes all the files.
with Session() as s:

    users = [User(first_name='Adam',
                  surname='Kurkiewicz',
                  idnumber='0',
                  password='pass',
                  student=True),
             User(first_name='Bruno',
                  surname='Peres',
                  idnumber='1',
                  password='pass',
                  student=True),
             User(first_name='Gabrielius',
                  surname='Mickievicius',
                  idnumber='2',
                  password='pass',
                  student=True)]

    courses = [Course("CS1P", ""),
               Course("PL3", ""),
               Course("PSD3", "")]

    class_sessions = [ClassSession(courses[0],
                                   "Lab 1", 
                                   datetime.now(), 
                                   datetime.now())]

    # this is important. If you don't add the objects, they will be inevitably lost
    s.add(users + courses)

    # this is important as well. Because exams depend on users and courses, you
    # have to commit users and courses before you create exams. You might be
    # really surprised at the results if you don't.
    s.session.commit()
    
    # semantically -- Adam takes PL3, Bruno takes PS3, Gabrielius takes PS3.
    exams = [Exam(courses[2], users[1]),
             Exam(courses[1], users[0]),
             Exam(courses[2], users[2])]
    
    s.add(exams)

with Session() as s:
    #all students who take the PS3 course.
    who_takes_PS3 = s.students_by_exam("PS3")
    for instance in who_takes_PS3:
        print instance.first_name

# ================================ Example 2 ==================================

with Session() as s:
    #verifies the password
    print s.verify_password("Adam", "pass")
    print s.verify_password("Adam", "topecret")
