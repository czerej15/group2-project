from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms

def sudentMenu():
    while True:
                    print("-----------------------------------------")
                    print("1 - Enter student ID")
                    print("2 - Exit")
                    sID_opt = input("Press the respective key to navigate:")
                    if not checkValidOptionNumb(sID_opt, 2):
                        continue
                    
                    if sID_opt == '2': #exit
                        break
                    
                    if sID_opt == "1":
                        print("-----------------------------------------")
                        id = input("Enter student ID:")
                        if checkStudentID(id): # returns true if valid
                            if id not in dictStudent: # if student not returned
                                print("Student not found.")
                                continue
                            
                            student = dictStudent[id]
                            
                            while True:
                                print("-----------------------------------------")
                                # print student info
                                print("Name:", student.name)
                                print("Student ID:", student.studentID)
                                print("Date of Birth:", student.dob)
                                print("Student Program:", student.programCode)
                                print("Student Menu:")
                                # student menu options
                                print()
                                print("1 - Display academic history and current enrolment")
                                print("2 - Querying course or program information")
                                print("3 - Enrol/UnEnrol in a current offering")
                                print("4 - View current GPA") # in progress for extra functionalities
                                print("5 - Exit")
                                stud_opt = input("Press the respective key to navigate:")
                                print(stud_opt)
                                if not checkValidOptionNumb(stud_opt, 5):
                                    continue

                                if stud_opt == "5": #exit
                                    break

                                if stud_opt == "1": 
                                    
                                    print("------------Current Enrolment------------")
                                    # loop through currentEnrol list, printing its contents
                                    c = 0
                                    for i in range(len(student.currentEnrol)//3):
                                        print("Course Code:", student.currentEnrol[c]) 
                                        print("Semester:", student.currentEnrol[c+1][0:2]) 
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
                                    
                                    
                                if stud_opt == "2": 
                                    while True:
                                        print("1 - Query Course")
                                        print("2 - Query Program")
                                        cou_or_prog_inpt = input("Press the respective key to navigate:")
                                        
                                        if not checkValidOptionNumb(sID_opt, 2):
                                            continue
                                        if cou_or_prog_inpt == '1':
                                            course = input("Enter course code:")
                                            print(dictSubject[course])
                                            input()
                                            

                                        if cou_or_prog_inpt == '2':
                                            program = input("Enter program code:")
                                            print(dictPrograms[program])

                                        

                                if stud_opt == "3": 
                                    pass

                                if stud_opt == "4": # in progress, doesn't work - keely
                                        gradePoints = 0
                                        creditPoints = 0
                                        for acaRecord in student.academicHist:
                                            if acaRecord in dictSubject:
                                                creditPoints += int(dictSubject[acaRecord].credit)
                                                tempCredit = int(dictSubject[acaRecord].credit)
                                            if acaRecord == 'HD':
                                                gradePoints += 4 * tempCredit
                                            elif acaRecord == 'DI': 
                                                gradePoints += 3 * tempCredit
                                            elif acaRecord == 'CR': 
                                                gradePoints += 2 * tempCredit
                                            elif acaRecord == 'PA':
                                                gradePoints += 1 * tempCredit
                                            else:
                                                gradePoints += 0
                                        
                                        GPA = gradePoints/creditPoints
                                        print(f"{student.name}'s GPA is {GPA:.2f}")