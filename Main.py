from Classes import Course, Program, Semester, Student
from error_handling import *

def findStudentByID(id, student_list):
	for student in student_list:
		if student.studentID == id:
			return student
	return False

if __name__ == "__main__":

	#temporary test list
	ts1 = Student()
	ts1.name = 'James'
	ts1.studentID = 's3900781'
	ts1.dob = "17/03/02"
	ts2 = Student()
	ts2.name = 'Dani'
	ts2.studentID = 's1234567'
	ts2.dob = "01/07/01"
	student_list = [ts1,ts2]


	while True:
		print("----------------------------------------")
		print("Welcome to the J.I.K enrolment system!")
		print("1 - Student Login")
		print("2 - System Login ")
		print("3 - Exit ")
		main_opt = input("Press the respective key to navigate:")

		if not checkValidOptionNumb(main_opt, 3):
			continue

		if main_opt == '3': # exit
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
					id = input("Enter student ID:")
					if checkStudentID(id): # returns true if valid
						#student_list is a list that just contains the Student instances. Probably created in "Inputing_Data.py"
						student = findStudentByID(id, student_list)
						
						if student == False: # if student not returned
							print("Student not found.")
							continue
						
						print("----------------------------------------")
						# print student info
						print("Name:", student.name)
						print("Student ID:", student.studentID)
						print("Date of Birth:", student.dob)
						print("Student Menu:")
						#print(student.programCode)
						# student menu options
						print("1 - Display academic history and current enrolment")
						print("2 - Querying course or program information")
						print("3 - Enrol/UnEnrol in a current offering")
						print("4 - Exit")
						stud_opt = input("Press the respective key to navigate:")
						if not checkValidOptionNumb(stud_opt, 4):
							continue

						if stud_opt == 4: #exit
							break


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
				if admin_opt == '10':
					break

