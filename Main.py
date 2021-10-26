from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms
from admin_menu import *
from student_menu import *


if __name__ == "__main__":

	while True:
		print("-----------------------------------------")
		print("Welcome to the J.I.K enrolment system!")
		print("1 - Student Login") # student and system seemed too similar so i changed one to admin, feel free to change it again tho - keely
		print("2 - Admin Login ")
		print("3 - Exit ")
		main_opt = input("Press the respective key to navigate:")

		if not checkValidOptionNumb(main_opt, 3):
			continue

		if main_opt == '3': # exit
			print("-----------------------------------------")
			print('Goodbye.')
			break 

		if main_opt == '1': # student
			sudentMenu()

		if main_opt == '2':
			adminMenu()



