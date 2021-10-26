from Classes import Student, Program
from Inputing_Data import dictStudent, dictPrograms

		toDo = []

		enrolProg = Student.programCode

		for item in Program.core_courses:
			if item not in Student.academicHist or item not in Student.currentEnrol:
				toDo.append(item)