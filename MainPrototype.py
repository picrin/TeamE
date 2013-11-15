##from backend import Session
import sys
import os
import CsvExport

#######Functions########

def clearScreen():
	os.system('cls' if os.name=='nt' else 'clear')

def adminMenu():
	clearScreen()
	print "Admin Main Menu:\n1.Attendance Monitor\n2.CSV Export\n0.Exit"
	print "\nPlease enter your choice:"
	menuOption=input()
	while (menuOption<0 or menuOption>2):
		print "\nYou entered and invalid option. Please reenter:"
		menuOption=input()
	options={1:attendanceMonitor,
		2:CsvExport.menu,}
	while(menuOption!=0):
		clearScreen()
		options[menuOption]()
		clearScreen()
		print "Admin Main Menu:\n1.Attendance Monitor\n2.CSV Export\n0.Exit"
		print "\nPlease enter your choice:"
		menuOption=input()

def tutorMenu():
	print "\nTutor Main Menu:\n1.Attendance Monitor\n0.Exit"
	print "\nPlease enter your choice:"
	menuOption=input()
	while (menuOption<0 or menuOption>2):
		print "\nYou entered and invalid option. Please reenter:"
		menuOption=input()
	options={1:attendanceMonitor,}
	while(menuOption!=0):
		clearScreen()
		options[menuOption]()
		clearScreen()
		print "Tutor Main Menu:\n1.Attendance Monitor\n0.Exit"
		print "\nPlease enter your choice:"
		menuOption=input()

def attendanceMonitor():
	print "Please enter the course ID you wish to view or enter 0 to go back to the main menu."
	courseID=raw_input()
	#TODO check courseID
	clearScreen()
	print "Course ID: "+courseID+"\nWould you like to enter the attendence:\n1.Manually\n2.Barcode Scanner\n0:Main Menu\nPlease enter your choice:"
	manOrScan=input()
	while(manOrScan<0 or manOrScan>2):
		print "\nYou entered an invalid choice please try again:"
		manOrScan=input()
	if (manOrScan==1):	#TODO Finish this so that it gets sessions from courseID then gets the sessions depending on the week.
		print "\nPlease enter the week number you wish to look at:"#FUNCTION
		weekNum=input()
		#TODO Get all sessions for the week for that course.
		print "\nPlease select which session you want to edit the attendance for:"
		#TODO print each session with a number for the user to enter.
		sessionChoice=input()
		#TODO get session ID to pass to a function that handles the attendance stuff (Vlad and Arnas?)
	elif(manOrScan==2):
		print "\nEnter function for barcode scanner input of attendance." #FUNCTION


############## Main Programme###########

#get user to login
clearScreen()
print "Welcome. Please enter your GUID username:"
username=raw_input()
print "\nPlease enter your password:"
password=raw_input()

#if user login credentials are correct display correct menu
with Session() as s:
	if(s.verify_password(username,password)):
		print "\nLogin Successful."
		print "\nFor this test please enter which type of user you are. (admin/tutor)"	#TODO Need to make this work off user info.
		usertype=raw_input()
		while(usertype!="admin" and usertype!="tutor"):
			print "\nYou entered an invalid option. Please enter 'admin' or 'tutor':"
			usertype=raw_input()
		if(usertype=="admin"):
			adminMenu()
		elif(usertype=="tutor"):
			tutorMenu()
		
