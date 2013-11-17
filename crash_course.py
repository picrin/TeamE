from backend import User, Course, Exam, Session, ClassSession, UserHasExam, Attendance, UserHasCourse
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
                  student=True),
             User(first_name='Sample',
                  surname='Tutor',
                  idnumber='3',
                  password='pass',
                  tutor=True,
                  student=True)]

    courses = [Course("CS1P", ""),
               Course("PL3", ""),
               Course("PS3", "")]

    # CS1P has 1 Lab that starts and ends now and the tutor is the Sample Tutor
    class_sessions = [ClassSession(courses[0],
                                   "Lab 1", 
                                   datetime.now(), 
                                   datetime.now(),
                                   users[3]),
                      ClassSession(courses[2],
                                   "Lab 1 PSD", 
                                   datetime.now(), 
                                   datetime.now(),
                                   users[3]),]


    # this is important. If you don't add the objects, they will be inevitably lost
    s.add(users + courses + class_sessions)

    # this is important as well. Because exams depend on users and courses, you
    # have to commit users and courses before you create exams. You might be
    # really surprised at the results if you don't.
    s.session.commit()
    
    # semantically -- Adam takes PL3, Bruno takes PS3, Gabrielius takes PS3.
    user_has_courses = [UserHasCourse(users[0], courses[1], student=True),
                        UserHasCourse(users[1], courses[2], student=True),
                        UserHasCourse(users[2], courses[2], student=True)]

    # semantically -- CS1P has one assignment worth 10 and one exam worth 80
    exams = [Exam(80, courses[0], exam=True),
             Exam(10, courses[0], assignment=True)]

    # semantically -- Adam has taken PS3's exam, so did Bruno
    user_has_exams = [UserHasExam(exams[0], users[1]),
                      UserHasExam(exams[0], users[0])]

    s.add(user_has_courses + exams + user_has_exams)

with Session() as s:
    #all students who take the PS3 course.
    who_takes_PS3 = s.students_by_course("PS3")
    for instance in who_takes_PS3:
        print instance.first_name

with Session() as s:
    #all sessions tutored by tutor 4
    sessions_tutor1_tutors = s.sessions_by_tutor(4)
    for instance in sessions_tutor1_tutors:
        print instance.name

# Sample queries
s.sessions_by_tutor(4)
s.sessions_by_course(1)
s.sessions_by_student(1)
s.students_in_session(1)
s.set_attendance(1, 1, "presence")
s.students_by_course("PS3")

# ================================ Example 2 ==================================

with Session() as s:
    #verifies the password
    print s.verify_password("Adam", "pass")
    print s.verify_password("Adam", "topecret")
