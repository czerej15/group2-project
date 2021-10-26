from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms

def adminMenu():
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