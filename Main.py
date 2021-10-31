from error_handling import *
from Inputing_Data import dictStudent, dictSubject, dictPrograms
from admin_menu import adminMenu
from student_menu import studentMenu


if __name__ == "__main__":

	while True:
		print("-----------------------------------------")
		print("Welcome to the J.I.K enrolment system!")
		print("1 - Student Login") # student and system seemed too similar so i changed one to admin, feel free to change it again tho - keely
		print("2 - Admin Login ")
		print("3 - Exit ")
		main_opt = input("Press the respective key to navigate:")

		if not checkValidOptionNumb(main_opt, 3):  # if input not valid, reprint menu 
			continue

		if main_opt == '3': # exit
			print("-----------------------------------------")
			print("Are you sure you want to exit? ")
			exit_inpt = input("(key 'y' for yes/ any other key for no):")
			if exit_inpt == "y": # if anything else, will naturally just continue while loop (reprint menu)
				print("-----------------------------------------")
				print('Goodbye.')
				break 

		if main_opt == '1': # student menu
			studentMenu()

		if main_opt == '2': # admin menu
			adminMenu()



