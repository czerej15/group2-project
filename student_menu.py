from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms, dictSemester

def studentMenu():
    while True:
        print("-----------------------------------------")
        print("1 - Enter student ID")
        print("2 - Exit")
        sID_opt = input("Press the respective key to navigate:")
        if not checkValidOptionNumb(sID_opt, 2):
            # if input not valid, reprint menu (continue goes to start of while loop)
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
                    print()
                    # student menu options
                    print("Student Menu:")
                    print("1 - Display academic history and current enrolment")
                    print("2 - Querying course or program information")
                    print("3 - Enrol/UnEnrol in a current offering")
                    print("4 - View current GPA") # in progress for extra functionalities
                    print("5 - Exit")
                    stud_opt = input("Press the respective key to navigate:")
                    
                    if not checkValidOptionNumb(stud_opt, 5):
                        # if input not valid, reprint menu (continue goes to start of while loop)
                        continue

                    if stud_opt == "5": #exit
                        break

                    if stud_opt == "1":                         
                        print("------------Current Enrolment------------")
                        print(student.currentEnrol)
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
                        
                        
                    if stud_opt == "2":        
                        while True:
                            print("-----------------------------------------")
                            print("1 - Query Course")
                            print("2 - Query Program")
                            print("3 - Exit")
                            cou_or_prog_inpt = input("Press the respective key to navigate:")
                            
                            if not checkValidOptionNumb(sID_opt, 3): 
                                # if input not valid, reprint menu (continue goes to start of while loop)
                                continue

                            if cou_or_prog_inpt == '3': #exit while loop aka go to previous menu
                                break

                            if cou_or_prog_inpt == '1': # query course
                                course = input("Enter course code:")
                                if not (course in dictSubject):
                                    print('Course not found')
                                    continue
                                print("-----------------------------------------")
                                print(dictSubject[course])
                                input("Press enter to go back")
                                
                            if cou_or_prog_inpt == '2': # query program
                                program = input("Enter program code:")
                                if not (program in dictPrograms):
                                    print('Program not found')
                                    continue
                               
                                print("-----------------------------------------")
                                print(dictPrograms[program])
                                input("Press enter to go back")                

                    if stud_opt == "3": 
                        while True:
                            print("-----------------------------------------")
                            print("1 - Enrol")
                            print("2 - Unenroll")
                            print("3 - Exit")
                            enroll_inpt = input("Press the respective key to navigate:")

                            if not checkValidOptionNumb(enroll_inpt, 3): 
                                # if input not valid, reprint menu (continue goes to start of while loop)
                                continue

                            if enroll_inpt == '3': #exit while loop aka go to previous menu
                                break
                            
                            if enroll_inpt == '1': # enrol
                                unav_courses = []
                                avail_courses = []
                                for offering in dictSemester['S22021'].course_offerings:
                                    # if course was attempted (in acedmic history)
                                    if (offering.id in student.academicHist):
                                        # if attempted course resulted in failure, can do again
                                        index =  student.academicHist.index(offering.id)
                                        if int(student.academicHist[index+1]) > 59:
                                            unav_courses.append(offering.id)
                                        else:
                                            avail_courses.append(offering.id)
                                    elif (offering.id in student.currentEnrol):
                                        # if student currently doing course or did it in the pass
                                        unav_courses.append(offering.id)
                                    else:
                                        avail_courses.append(offering.id)
                                print("Available Courses:")
                                for avai in avail_courses:
                                   print(avai)
                                print()
                                print("Unavailable Course:")
                                for unav in unav_courses:
                                   print(unav)

                                enrol_cour = input("Enter course code you wish to enrol in:")
                                # check student has completed prerequistes for course wanting to enrol in
                                if enrol_cour in avail_courses:
                                    flag = True
                                    for preq in dictSubject[enrol_cour].prerequisites:
                                        if preq in student.academicHist:
                                            continue
                                        else:
                                            flag = False
                                    if flag == True:
                                        dictSemester["S22021"].add_student(enrol_cour, student.studentID)
                                        student.currentEnrol.append(enrol_cour)
                                        student.currentEnrol.append('S22021')
                                        student.currentEnrol.append('2021')
                                    
                                else:
                                    print('Not available course')
                                
                                

                                # edit semester:
                                #  add_student(self, course, student):
                                #  remove_student(self, course, student):

                                # edit student:
                                # - current_enrolement
                            if enroll_inpt == '2': # unenroll
                                pass
                                # edit semester:
                                # def add_student(self, course, student):
                                # def remove_student(self, course, student):

                                # edit student:
                                # - current_enrolement

                    if stud_opt == "4": # in progress, doesn't work - keely
                        print("------------Student GPA------------")
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

                        print()
                        input('Press enter to go back')