from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms

def adminMenu():
    while True:
		# system login
        print("----------------------------------------")
        print("Admin Menu:")
        print("1 - Add/Remove a student")
        print("2 - Add/Remove a course")
        print("3 - Add/Remove a program")
        print("4 - Add/Remove a semester")
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

        if admin_opt == "1":  # remove/add student
            while True:
                print("----------------------------------------")
                print("1 - Add Student")
                print("2 - Remove Student")
                print("3 - Exit")
                add_or_rem_inpt = input("Press the respective key to navigate:")

                if not checkValidOptionNumb(admin_opt, 3):
                    continue

                if add_or_rem_inpt == "3":
                    break

                if add_or_rem_inpt == "1": # add student option
                   
                   # while True:
                    #    print("-----------------------------------------")
                     #   print("1 - Enter student ID")
                      #  print("2 - Exit")
                       # a_sID_opt = input("Press the respective key to navigate:")

                      #  if not checkValidOptionNumb(a_sID_opt, 2):
                            # if input not valid, reprint menu (continue goes to start of while loop)
                            #continue

                      #  if a_sID_opt == "2": # exit
                       #     break

                        #if a_sID_opt == "1": # add student

                        while True:
                            new_name = input('Enter a name:')
                            if checkNameValid(new_name): # if valid name, break while loop and continue
                                break
                        
                        while True:
                            new_id = input('Enter a student ID:')
                            if checkStudentID(new_id) and not (new_id in dictStudent): # if valid id, break while loop and continue
                                break

                        while True:
                            new_dob = input('Enter a date of birth:')
                            if checkDOBValid(new_dob): # if valid dob, break while loop and continue
                                break
                      
                        dictStudent[new_id] = Student(name = new_name, studentID = new_id, dob = new_dob) # create new instance of student and add to 
                      
                            
                            
                            
                            
                            
                if add_or_rem_inpt == "2": # remove student
                    while True:
                        print("-----------------------------------------")
                        print("1 - Enter student ID")
                        print("2 - Exit")
                        sID_opt = input("Press the respective key to navigate:")
                        if not checkValidOptionNumb(sID_opt, 2):
                            # if input not valid, reprint menu (continue goes to start of while loop)
                            continue

                        if sID_opt == "2":
                            break

                        if sID_opt == "1":
                            stud_to_rem = input("Enter ID of student to remove:")
                            if checkStudentID(stud_to_rem) and (stud_to_rem in dictStudent):
                                pass
                                # remove student from semester.enrolledStudent
                                # remove from dictStudent
                    

        if admin_opt == "2": 
            pass

        if admin_opt == "3": 
            pass

        if admin_opt == "4": 
            pass

        if admin_opt == "5": 
            while True:
                print("-----------------------------------------")
                print("1 - Enter student ID")
                print("2 - Exit")
                sID_opt = input("Press the respective key to navigate:")
                if not checkValidOptionNumb(sID_opt, 2):
                    # if input not valid, reprint menu (continue goes to start of while loop)
                    continue

                if sID_opt == '2':
                    break

                if sID_opt == '1':
                    print("-----------------------------------------")
                    student_id = input('Enter ID of student to query:')
                    if checkStudentID(student_id) and (student_id in dictStudent):
                        student = dictStudent[student_id]
                        print("-----------------------------------------")
                        print("Name:", student.name)
                        print("Student ID:", student.studentID)
                        print("Date of Birth:", student.dob)
                        print("Student Program:", student.programCode)
                        print()
                        print("------------Current Enrolment------------")
                        # loop through currentEnrol list, printing its contents
                        c = 0
                        for i in range(len(student.currentEnrol)//3):
                            print("Course Code:", student.currentEnrol[c]) 
                            print("Semester:", student.currentEnrol[c+1][0:2]) #print first 2 characters, not including year
                            print("Year:", student.currentEnrol[c+2]) 
                            print()
                            c += 3

                        print("------------Academic History------------")
                        # loop through academicHist list, printing its contents
                        c = 0
                        for i in range(len(student.academicHist)//3):
                            print("Course Code:", student.academicHist[c], end = ' | ') 
                            print("Mark: ", student.academicHist[c+1], end = ' | ')
                            print("Grade:", student.academicHist[c+2]) 
                            c += 3
                        print()
                        input('Press enter to go back')

        if admin_opt == "6": 
            pass

        if admin_opt == "7": 
            pass

        if admin_opt == "8": 
            print("-----------------------------------------")
            id = input("Enter student ID:")
            if checkStudentID(id): # returns true if valid
                if id not in dictStudent: # if student not returned
                    print("Student not found.")
                    continue
                
                student = dictStudent[id]
                program = dictPrograms[student.programCode]

            toDo = []

            for item in Program.core_courses:
                if item not in Student.academicHist or item not in Student.currentEnrol:
                    toDo.append(item)

        if admin_opt == "9": 
            pass