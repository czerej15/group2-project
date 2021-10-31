from Classes import Student, Program, Course, Semester

###################################################################
# Student
# open and read data from file
f = open('student_data.csv')
contents = f.read().split('\n') # split each student up
f.close()

dictStudent = {}

for i in range(len(contents)): # for each student
	l = contents[i].split(';') # split the data in a student record into the seperate features
	l[4] = l[4].split(',')
	l[5] = l[5].split(',')
	ID = Student(l[0], l[1], l[2], l[3], l[4], l[5], l[6]) # create student instance
	dictStudent[l[1]] = ID # assign the instance to a dictionary key. Access it by calling dictStudent['s3898340'].name ect 
###################################################################

# Program
# open and read data from file
f = open('programs.csv')
contents = f.read().split('\n') # split each program up
f.close()

dictPrograms = {}

for i in range(len(contents)): # for each program
	l = contents[i].split(';')
	l[2] = l[2].split(',') # split the data in a program record into the seperate features
	ID = Program(l[0], l[1], l[2], l[3]) # create program instance
	dictPrograms[l[0]] = ID # assign the instance to a dictionary key. Access it by calling dictPrograms['BP094'].points ect 
###################################################################

###################################################################
# Course
# open and read data from file
f = open('Subjects.csv')
contents = f.read().split('\n') # split each course up
f.close()

dictSubject = {}

for i in range(len(contents)): # for each course
	l = contents[i].split(';') # split the data in a course record into the seperate features
	#print(l[0], l[1], l[2], l[3], l[4])
#	print(l[4].split(','))
	ID = Course(l[0], l[1], l[2], l[3].split(','), l[4].split(',')) # create course instance
	dictSubject[l[0]] = ID # assign the instance to a dictionary key. Access it by calling dictSubject['ISYS1118'].title ect
###################################################################



f = open('semester_data.csv')
contents = f.read() 
contents = contents.split('\n')
f.close()

dictSemester = {}

for line in contents:
	line = line.split(';')
	# line example
	# ['S12021', 'COSC2801,5,s3900781,s3900123,s3900321', 'IBY2041,3,s3900111,s3900222,s3900555']
	new_semester = Semester(line[0])
	for course in line[1:]: # ignore semester identiy
		course = course.split(',')
		#print(course)
		new_semester.add_course_offering(course[0], course[1])
		if len(course) > 2: # if there are students entered in csv for course e.g. s3900781,s3900123,s3900321
			for student in course[2:]:
				new_semester.add_student(course[0], student)
	dictSemester[new_semester.identity] = new_semester


