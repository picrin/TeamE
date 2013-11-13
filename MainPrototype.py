import Login
import sys
import os

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
	while(menuOption!=0):
		clearScreen()
		if (menuOption==1):
			print "Please enter the course ID you wish to view or enter 0 to go back to the main menu."
			courseID=raw_input()
			#TODO check courseID
			clearScreen()
			print "Course ID: "+courseID+"\nWould you like to enter the attendence:\n1.Manually\n2.Barcode Scanner\n0:Main Menu\nPlease enter your choice:"
			manOrScan=input()
			while(manOrScan<0 or manOrScan>2):
				print "\nYou entered an invalid choice please try again:"
				manOrScan=input()
			if (manOrScan==1):
				print "Enter function for manual input of attendance."
			elif(manOrScan==2):
				print "Enter function for barcode scanner input of attendance."
		if(menuOption==2):
			print "What you would like to export:\n1.All student attendance records for a single course\n2.All recorded information for a single student\n0.Main Menu\nPlease enter your choice:"
			csvChoice=input()
			while(csvChoice<0 or csvChoice>2):
				print "\nYou entered an invalid choice please try again:"
				csvChoice=input()
			if (csvChoice==1):
				print "Enter function for by course csv export" #Print used as compiler didnt like only a comment here
			elif(csvChoice==2):
				print "Enter function for by student csv export."
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
	while(menuOption!=0):
		clearScreen()
		if (menuOption==1):
			print "Please enter the course ID you wish to view or enter 0 to go back to the main menu."
			courseID=raw_input()
			#TODO check courseID
			clearScreen()
			print "Course ID: "+courseID+"\nWould you like to enter the attendence:\n1.Manually\n2.Barcode Scanner\n0:Main Menu\nPlease enter your choice:"
			manOrScan=input()
			while(manOrScan<0 or manOrScan>2):
				print "\nYou entered an invalid choice please try again:"
				manOrScan=input()
			if (manOrScan==1):
				print "Enter function for manual input of attendance."
			elif(manOrScan==2):
				print "Enter function for barcode scanner input of attendance."
		clearScreen()
		print "Tutor Main Menu:\n1.Attendance Monitor\n0.Exit"
		print "\nPlease enter your choice:"
		menuOption=input()


############## Main Programme###########

#get user to login
clearScreen()
print "Welcome. Please enter your GUID username:"
username=raw_input()
print "\nPlease enter your password:"
password=raw_input()

#if user login credentials are correct display correct menu
if(Login.login(username,password)):
	print "\nLogin Successful."
	print "\nFor this test please enter which type of user you are. (admin/tutor)"	##TODO Need to make this work off user info.
	usertype=raw_input()
	while(usertype!="admin" and usertype!="tutor"):
		print "\nYou entered an invalid option. Please enter 'admin' or 'tutor':"
		usertype=raw_input()
	if(usertype=="admin"):
		adminMenu()
	elif(usertype=="tutor"):
		tutorMenu()
		
