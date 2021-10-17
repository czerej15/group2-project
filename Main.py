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
		option = input("Press the respective key to navigate:")

		if option == '3': # exit
			print('Goodbye.')
			break 

		if option == '1': # student
			print("----------------------------------------")
			id = input("Enter student ID:")
			if checkStudentID(id): # returns true if valid
				student =  findStudentByID(id, student_list) #student_list is a list that just contains the Student instances. Probably created in "Inputing_Data.py"
				if student == False:
					print("Invalid ID")
					continue
				else:
					print("----------------------------------------")
					# print student info
					print("Name:", student.name)
					print("Student ID:", student.studentID)
					print("Date of Birth:", student.dob)
					#print(student.programCode)
					# student menu options
					print("1 - Display academic history and current enrolment")
					print("2 - Querying course or program information")
					print("3 - Enrol/UnEnrol in a current offering")
					print("4 - Exit")
					option = input("Press the respective key to navigate:")

				if option == 4:
					break


		if option == '2':
			# system login
			pass

	