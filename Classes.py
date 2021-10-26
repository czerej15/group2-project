class Course:
	# The Course class is used to store course related information, this would include: 
	# course code, title, credit points, prerequisites, available semesters 
	# (takes a list of semesters as its value, 
	# e.g., [S1] indicades S1 only, [S2] indicates S2 only, and [S1,S2] means available in both semesters). 
	# For instance, a sample list of courses, their information including 
	# name, course code, pre-requisite and available semesters are available in your enrolment online systems as well as course guides.
	def __init__(self, code, title, credit, prereques = [], sems = []):
		self.code = code
		self.title = title
		self.credit = credit
		self.prerequisites = prereques
		self.semesters = sems #e.g. [S1] or [S1, S2] or [S2]

	def addSemester(self, semester):
		self.semesters.append(semester)

	def removeSemester(self, semester):
		self.semesters.remove(semester)

	def addPreq(self, preq):
		self.prerequisites.append(preq)

	def removePreq(self, preq):
		self.prerequisites.remove(preq)

class Program: 
	# This is the class of an academic program, like the Bachelor of Computer Science (BP094) and Bachelor of Software Engineering (BP096). 
	# Each program consists of program code, credit points 
	# (e.g.,BP094 requires completion of 288 credit points upon graduation),
	# a list of core courses (mandatory requirements) and a list of programe lective courses.
	# In this system prototype, to make it simple, we can ignore the possibilities of a university elective, 
	# i.e., a program can only containcore and elective courses.
	def __init__(self, code, points, core = [], electives = []):
		self.code = code
		self.points = points # e.g. 288
		self.core_courses = core
		self.electives = electives
	
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
	def __init__(self, id, max_students, studentList = []):
		self.id = id
		self.cap = max_students
		self.enrolled_students = studentList

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
	
	def add_course_offering(self, id, cap):
		self.course_offerings.append(CourseOffering(id, cap))

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
	# The Student class should provide constructor, string methods, getter and setters, as well as methods to amend the academic history and study plan.
	# - Once the official marks of the current enrollments are released, they should be moved to his/her academic history.
	# - You might also want to include a status of the study plan. 
	# For instance:
	# - If a student failed a course, the status of the study plan should indicate that it needs to be adjusted to reflect the updated plan on remaining studies.
	# - Similarly,if a student enrol in or unenroll from a course offering, this status should also be updated to reflect adjustment is needed on the studyplan.
	# - When a new study plan is generated, the status of the study plan should indicate that the study plan is up-to-date.
	def __init__(self, name, studentID = '', dob = '', programCode = '', academicHist = [], currentEnrol = []):
		self.name = name
		self.studentID = studentID
		self.dob = dob
		self.programCode = programCode  # had to temporarly comment this out for testing - james  #keely changed it for inputing data
		self.academicHist = academicHist #list [courseCode, mark, grade]
		self.currentEnrol = currentEnrol #list of lists of class codes [course code, semester, year] in [subject1, subject2, subject3, subject4]

	def __str__(self): 
		print(f"Name: {self.name}")
		print(f"Student ID: {self.studentID}")
		print(f"Date of Birth: {self.dob}")
		print(f"Program Code: {self.programCode}")
		print(f"Academic History: {self.academicHist}")
		print(f"Current Enrollments: {self.currentEnrol}")

	def append_marks(self, courseCode, mark, grade):
		self.academicHist.append([courseCode, mark, grade])

	def ammend_history(self, courseCode, semester, year, mark, grade):
		self.append_marks(courseCode, mark, grade)
		self.currentEnrol.pop([courseCode, semester, year])

class StudyPlan:
	def __init__(self, name, code, points, studentID = '', dob = '', programCode = '', academicHist = [], currentEnrol = [], core = [], electives = []):
		Student.__init__(self, name, studentID = '', dob = '', programCode = '', academicHist = [], currentEnrol = [])
		Program.__init__(self, code, points, core = [], electives = [])

		