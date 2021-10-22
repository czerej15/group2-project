from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff

if __name__ == "__main__":

	while True:
		print("----------------------------------------")
		print("Welcome to the J.I.K enrolment system!")
		print("1 - Student Login") # student and system seemed too similar so i changed one to admin, feel free to change it again tho - keely
		print("2 - Admin Login ")
		print("3 - Exit ")
		main_opt = input("Press the respective key to navigate:")

		if not checkValidOptionNumb(main_opt, 3):
			continue

		if main_opt == '3': # exit
			print("----------------------------------------")
			print('Goodbye.')
			break 

		if main_opt == '1': # student
			while True:
				print("----------------------------------------")
				print("1 - Enter student ID")
				print("2 - Exit")
				sID_opt = input("Press the respective key to navigate:")
				if not checkValidOptionNumb(sID_opt, 2):
					continue
				
				if sID_opt == '2': #exit
					break
				
				if sID_opt == "1":
					print("----------------------------------------")
					id = input("Enter student ID:")
					if checkStudentID(id): # returns true if valid
						if id not in dictStudent: # if student not returned
							print("Student not found.")
							continue
						
						student = dictStudent[id]
						
						while True:
							print("----------------------------------------")
							# print student info
							print("Name:", student.name)
							print("Student ID:", student.studentID)
							print("Date of Birth:", student.dob)
							print("Student Program:", student.programCode)
							print("Student Menu:")
							# student menu options
							print("1 - Display academic history and current enrolment")
							print("2 - Querying course or program information")
							print("3 - Enrol/UnEnrol in a current offering")
							print("4 - View current GPA") # in progress for extra functionalities
							print("5 - Exit")
							stud_opt = input("Press the respective key to navigate:")
							print(stud_opt)
							if not checkValidOptionNumb(stud_opt, 4):
								continue

							if stud_opt == "5": #exit
								break

							if stud_opt == "1": 
								pass

							if stud_opt == "2": 
								pass

							if stud_opt == "3": 
								pass

							if stud_opt == "4": # in progress, doesn't work - keely
								GPA = 0
								for acaRecord in student.academicHist:
									if acaRecord == 'HD':
										pass
									if acaRecord == 'DI': 
										pass
									if acaRecord == 'CR': 
										pass
									if acaRecord == 'PA':
										pass
									if acaRecord == 'NN':
										pass
										

		if main_opt == '2':
			while True:
				# system login
				print("----------------------------------------")
				print("Admin Menu:")
				print("1 - Add/Remove/Amend a student")
				print("2 - Add/Remove/Amend a course")
				print("3 - Add/Remove/Amend a program")
				print("4 - Add/Remove/Amend a semester")
				print("5 - Query student information")
				print("6 - Allow manual amendment of the study plan for a student")
				print("7 - Validating a student’s study plan")
				print("8 - Generate a study plan for a student")
				print("9 - Display list of student achievements for course")
				print("10 - Exit")
				admin_opt = input("Press the respective key to navigate:")
				if not checkValidOptionNumb(admin_opt, 10):
					continue

				if admin_opt == '10': #exit
					break

				if admin_opt == "1": 
					pass

				if admin_opt == "2": 
					pass

				if admin_opt == "3": 
					pass

				if admin_opt == "4": 
					pass

				if admin_opt == "5": 
					pass

				if admin_opt == "6": 
					pass

				if admin_opt == "7": 
					pass

				if admin_opt == "8": 
					pass

				if admin_opt == "9": 
					pass



