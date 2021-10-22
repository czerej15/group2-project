from Classes import Student, CourseOffering, Program, Course

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
	ID = Student(l[0], l[1], l[2], l[3], l[4], l[5]) # create student instance
	dictStudent[l[1]] = ID # assign the instance to a dictionary key. Access it by calling dictStudent['s3898340'].name ect 
###################################################################

###################################################################
# Course Offerings
# open and read data from file
f = open('Course_Offerings.csv')
contents = f.read().split('\n') # split each course offering up
f.close()

dictCourseOff = {}

for i in range(len(contents)): # for each course offering
	l = contents[i].split(';') # split the data in a course offering record into the seperate features
	ID = CourseOffering(l[0], l[1], l[2]) # create course offering instance
	dictCourseOff[l[0]] = ID # assign the instance to a dictionary key. Access it by calling dictStudent['COSC2800'].enrolled_students ect 
###################################################################

###################################################################
# Program
# open and read data from file
f = open('programs.csv')
contents = f.read().split('\n') # split each program up
f.close()

dictPrograms = {}

for i in range(len(contents)): # for each program
	l = contents[i].split(';') # split the data in a program record into the seperate features
	ID = Program(l[0], l[1], l[2], l[3]) # create program instance
	dictPrograms[l[1]] = ID # assign the instance to a dictionary key. Access it by calling dictPrograms['BP094'].points ect 
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
	ID = Course(l[0], l[1], l[2], l[3], l[4]) # create course instance
	dictSubject[l[1]] = ID # assign the instance to a dictionary key. Access it by calling dictSubject['ISYS1118'].title ect 
###################################################################
