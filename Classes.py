class Course:
	# The Course class is used to store course related information, this would include: 
	# course code, title, credit points, prerequisites, available semesters 
	# (takes a list of semesters as its value, 
	# e.g., [S1] indicades S1 only, [S2] indicates S2 only, and [S1,S2] means available in both semesters). 
	# For instance, a sample list of courses, their information including 
	# name, course code, pre-requisite and available semesters are available in your enrolment online systems as well as course guides.
	def __init__(self, code, title, credit):
		self.code = code
		self.title = title
		self.credit = credit
		self.prerequisites = []
		self.semesters = [] #e.g. [S1] or [S1, S2] or [S2]

	def addSemester(self, semester):
		self.semesters.append(semester)

	def removeSemester(self, semester):
		self.semesters.remove(semester)

	def addPreq(self, preq):
		self.semesters.append(preq)

	def removePreq(self, preq):
		self.semesters.remove(preq)

class Program: 
	# This is the class of an academic program, like the Bachelor of Computer Science (BP094) and Bachelor of Software Engineering (BP096). 
	# Each program consists of program code, credit points 
	# (e.g.,BP094 requires completion of 288 credit points upon graduation),
	# a list of core courses (mandatory requirements) and a list of programe lective courses.
	# In this system prototype, to make it simple, we can ignore the possibilities of a university elective, 
	# i.e., a program can only containcore and elective courses.
	def __init__(self, code, points):
		self.code = code
		self.points = points # e.g. 288
		self.core_courses = []
		self.electives = []
	
	def add_elective(self,elective):
		self.electives.append(elective)
	
	def add_core(self,core):
		self.core_courses.append(core)
	
	def remove_core(self, core):
		self.core_courses.remove(core)
	
	def remove_elective(self,elective):
		self.electives.remove(elective)
	
	def __str__(self):
		print("Code:", self.code)
		print("Credit Points:", self.points)
		print("Core Course:")
		for core in self.core_courses:
			print(core)
		print("Electives:")
		for elective in self.electives:
			print(elective)
	

class CourseOffering():
	""" This class is to be used for the Semester class """
	def __init__(self, course_name, max_students):
		self.name = course_name
		self.cap = max_students
		self.enrolled_students = []

class Semester: # James
	# The Semester class contains its identity, e.g., S22021, and a list of course offerings in the semester.
	# For each course offering, it also contains the maximum student number 
	# (aka. Cap, assume each course only allows a certain number of students to enrol),
	# and a list of enrolled students
	# (i.e., the list of currently enrolled students). 
	# The Semester class should provide constructor, string methods, getter and setters, as well as methods to add or remove a student from a course offering. 
	# When adding a student into an offering, the system should first check whether the cap has been reached, in which case,the student cannot enrol.

	def __init__(self, identity):
		self.identity = identity #e.g., S22021
		self.course_offerings = []
	
	def add_course_offering(self, name, cap):
		self.course_offerings.append(CourseOffering(name, cap))

	def add_student(self, course, student):
		if len(course.enrolled_students) < course.cap:
			course.enrolled_students.append(student)
		else:
			print("Can't add, cap reached.")

	def remove_student(self, course, student):
		course.enrolled_students.remove(student)

	def __str__(self):
		print(self.identity)
		for course in self.course_offerings:
			print(course.name)

class Student: # Keely
	# The Student class stores the information of a student 
	# (e.g., name, student id, D.O.B, etc), 
	# program code (which program they is currently at), 
	# the academic history, current enrollments, and a study plan. 
	# Assume a student can only have one active program. 
	# The academic history stores a list of courses that a student has attempted before, as well his/her mark and grade of the attempted course. 
	# Current enrollment is a list of existing offerings 
	# (course code, semester, year) that he/she is currently enrolled in, and a study plan is a list of tuples 
	# (course code, semester, year) indicating the future plan for completing the remaining studies towards graduation
	# (i.e.,the study plan excludes the courses that the student has already passed, and courses that he is currently enrolled in.).
	# The Student class should provide constructor, string methods, getter ands etters, as well as methods to amend the academic history and study plan.
	# - Once the official marks of the current enrollments are released, they should be moved to his/her academic history.
	# - You might also want to include a status of the study plan. 
	# For instance:
	# - If a student failed a course, the status of the study plan should indicate that it needs to be adjusted to reflect the updated plan on remaining studies.
	# - Similarly,if a student enrol in or unenroll from a course offering, this status should also be updated to reflect adjustment is needed on the studyplan.
	# - When a new study plan is generated, the status of the study plan should indicate that the study plan is up-to-date.
	def __init__(self):
		self.name = ''
		self.studentID = ''
		self.dob = ''
		self.programCode = '' #relate to program class
		self.academicHist = [] #list [courseCode, mark, grade]
		self.currentEnrol = [] #list of lists of class codes [course code, semester, year] in [subject1, subject2, subject3, subject4] 
		self.studyPlan = [] #aks minyi about this type and if it includes electives. Is the data based on 

	def __str__(self):
		pass

	def get_student_details(self):
		pass

	def input_academicHist(self, answer = 'Y', lst = []):
		if answer == 'N' or 'n':
			return lst
		else:
			tempaca = [input(f"Enter a class in {self.name}'s academic history - eg. course code, mark, grade: ")]
			lst.append(tempaca)
			answer = input("If you would like to add another class print Y, if you are done adding classes print N: ").strip()
			self.input_class(answer, lst)

	def input_currentEnrol(self, answer = 'Y', lst = []):
		if answer == 'N' or 'n':
			return lst
		else:
			tempaca = [input(f"Enter a class in {self.name}'s current enrollments - eg. course code, semester, year: ")]
			lst.append(tempaca)
			answer = input("If you would like to add another class print Y, if you are done adding classes print N: ").strip()
			self.input_class(answer, lst)
	
	def input_studyPlan(self, answer = 'Y', lst = []):
		if answer == 'N' or 'n':
			return lst
		else:
			tempaca = [input(f"Enter a class in {self.name}'s study plan - eg. course code, semester, year: ")]
			lst.append(tempaca)
			answer = input("If you would like to add another class print Y, if you are done adding classes print N: ").strip()
			self.input_class(answer, lst)

	def set_student_details(self):
		self.name = input("Enter student's full name: ")
			#raise error if none if have time
		self.studentID = input(f"Enter {self.name}'s student ID: ")
		self.dob = input(f"Enter {self.name}'s date of birth: ")
		self.programCode = input(f"Enter {self.name}'s program code: ")
		self.academicHist = [self.input_academicHist()]
		self.currentEnrol = [self.input_currentEnrol()]
		self.studyPlan = [self.input_studyPlan()]

	def append_marks(self, courseCode, ):
		pass

	def ammend_history(self, courseCode, semester, year):
		self.academicHist.append([courseCode, semester, year])
		self.append_marks()
		self.currentEnrol.pop([courseCode, semester, year])

	def ammend_plan(self, courseCode, semester, year):
		self.studyPlan.pop([courseCode, semester, year])
		self.currentEnrol.append([courseCode, semester, year])
		pass

	def get_plan_status(self):
		for curClass in self.currentEnrol:
			if curClass[2] == 'NN':
				pass
		pass