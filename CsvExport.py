
def menu():
  print "What you would like to export:\n\
1. All student attendance records for a single course\n\
2. All recorded information for a single student\n\
0. Main Menu\n\
Please enter your choice:"

  while (True):
    choice=input()
    if (choice==0):
      break;
    if (choice==1):
      _menuSelectCourse()
      break
    elif(choice==2):
      print "Enter function for by student csv export."#FUNCTION
    else:
      print "\nYou entered an invalid choice please try again:"


def _menuSelectCourse():
  print
  with Session() as s:
    
    courses = s.courses
    for i in xrange(len(courses)):
      c = courses[i]
      print str(i) + '. ' + c.name + '(' + c.idnumber + ')\n'
    
    choice = input('\nSelect a course:')
    
