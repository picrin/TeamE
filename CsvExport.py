def menu():
  print "What you would like to export:\n1.All student attendance records for a single course\n2.All recorded information for a single student\n0.Main Menu\nPlease enter your choice:"
  csvChoice=input()
  while(csvChoice<0 or csvChoice>2):
    print "\nYou entered an invalid choice please try again:"
    csvChoice=input()
  if (csvChoice==1):
    print "Enter function for by course csv export" #FUNCTION
  elif(csvChoice==2):
    print "Enter function for by student csv export."#FUNCTION
