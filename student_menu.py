from error_handling import *
from Inputing_Data import dictStudent, dictSubject, dictPrograms, dictSemester
import matplotlib.pyplot as plt

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
                    print("5 - View graph of acedimic results")
                    print("6 - View acedimic results sorted")
                    print("7 - Exit")
                    stud_opt = input("Press the respective key to navigate:")
                    
                    if not checkValidOptionNumb(stud_opt, 7):
                        # if input not valid, reprint menu (continue goes to start of while loop)
                        continue

                    if stud_opt == "7": #exit
                        break

                    if stud_opt == "1":  # Display academic history and current enrolment                       
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
                        
                    if stud_opt == "2":  # Querying course or program information 
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
                                    input("Press enter to go back")
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

                    if stud_opt == "3": # Enrol/UnEnrol in a current offering
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
                                if 'S12022' not in dictSemester: # can only enroll in current semester. current semester should therefore exist
                                    print("Create a S12022 first")
                                    input("Press enter to return")
                                    continue

                                unav_courses = []
                                avail_courses = []
                                # go through course offerings in the current semester, putting courses into avaliable or unavaliable 
                                for offering in dictSemester['S12022'].course_offerings:
                                    # check not currently enrolled
                                    if offering.id in student.currentEnrol:
                                        unav_courses.append(offering.id)
                                        continue
                                        
                                    # check student meets preerquisies
                                    flag = True
                                    for preq in dictSubject[offering.id].prerequisites:
                                        if preq == "None":
                                            continue # if preq == None, it means has no prerequisites
                                        if preq in student.academicHist:
                                            continue # this preq is fine, check next preq
                                        else:
                                            flag = False
                                            unav_courses.append(offering.id)
                                            break
                                    if flag == True: # if prerequistes met
                                        # if course was attempted (in acedmic history)
                                        if (offering.id in student.academicHist):
                                            # if attempted course resulted in failure, can do again
                                            index =  student.academicHist.index(offering.id)
                                            if int(student.academicHist[index+1]) > 59:
                                                unav_courses.append(offering.id)
                                            else:
                                                # passed course, cant do it again
                                                avail_courses.append(offering.id)
                                        elif (offering.id in student.currentEnrol):
                                            # if student currently doing course, cant enrol in it
                                            unav_courses.append(offering.id)
                                        else:
                                            avail_courses.append(offering.id)
                                print("-----------------------------------------")
                                print("Please note, you can only enroll in courses for next semester (S1, 2022)")
                                # print all Available Courses
                                print("Available Courses:")
                                for avai in avail_courses:
                                   print(avai)

                                # print all Unavailable Courses
                                print()
                                print("Unavailable Course:")
                                for unav in unav_courses:
                                   print(unav)

                                enrol_cour = input("Enter course code you wish to enrol in:")
                                
                                if enrol_cour in avail_courses: # if avaliable course
                                        # check the cap limit has not been exceeded
                                        # checkInCap returns false if cap exceeded, else returns true and also adds student to course offering
                                        checkInCap = dictSemester["S12022"].add_student(enrol_cour, student.studentID)
                                        if checkInCap: # if doesnt exceed cap
                                            # add to students current enrolement
                                            student.currentEnrol.append(enrol_cour)
                                            student.currentEnrol.append('S12022')
                                            student.currentEnrol.append('2022')
                                            print("Successfully enrolled in ", enrol_cour)
                                            input('Press enter to go back')
                                        else:
                                            print("Student cap for that course in that semester has been exceeded")
                                            print("Could not enrol")
                                            input('Press enter to go back')

                                else:
                                    print('Not available course')
                                    input('Press enter to go back')
                                
                         
                            if enroll_inpt == '2': # unenroll
                                print("-----------------------------------------")
                                print("Currently Enrolled Courses:")
                                # just prints course codes from .currentEnrol list
                                c=0
                                for i in range(len(student.currentEnrol)//3):
                                    print(student.currentEnrol[c]) 
                                    c += 3

                                unenrol_cour = input("Enter course code you wish to unenroll from:")
                                if unenrol_cour in student.currentEnrol:
                                    # removes current semester i.e S22021
                                    dictSemester["S22021"].remove_student(unenrol_cour, student.studentID)
                                    # remove unerolled course from student's current enrollment
                                    index =  student.currentEnrol.index(unenrol_cour)
                                    del student.currentEnrol[index]
                                    del student.currentEnrol[index]
                                    del student.currentEnrol[index]
                                   
                                    print("Successfully unenrolled from ", unenrol_cour)
                                    input('Press enter to go back')
                                else:
                                    print("Not a valid course to unenroll from")

                    if stud_opt == "4": # View current GPA
                        print("------------Student GPA------------")
                        gradePoints = 0
                        creditPoints = 0 #initialise grade and credit points
                        for acaRecord in student.academicHist:
                            if acaRecord in dictSubject: #for every class in a student's academic history, add up the number of credit points
                                creditPoints += int(dictSubject[acaRecord].credit)
                                tempCredit = int(dictSubject[acaRecord].credit)
                            if acaRecord == 'HD': # calculate gpa
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
                        print(f"{student.name}'s GPA is {GPA:.2f}") #print gpa

                        print()
                        input('Press enter to go back')
                    
                    if stud_opt == "5": # Graph results
                        history = student.academicHist # just so dont have to type student.academicHist everytime

                        x = []
                        y = []
                        count = 0
                        for i in range(len(history)//3):
                            x.append(history[count]) # add course names to x
                            y.append(int(history[count+1])) # add course mark to y
                            count += 3
                        # using matplotlib to create a scatter plot
                        plt.scatter(x,y)
                        plt.title("Results for " + str(student.studentID))
                        plt.xlabel("Course")
                        plt.ylabel("Mark")
                        plt.ylim([0, 100]) # so y axis is alwayd 0 to 100, not min to max e.g. 45 to 87
                        plt.show()
                    
                    if stud_opt == "6": # print acedimic history sorted
                        sorted_hist = [] 
                        c=0 # count variable
                        hist = student.academicHist.copy() # copy of student.academicHist 
                        for i in range(len(hist)//3):
                            # find highest for each iteration 
                            c2 = 0
                            max = -1
                            for i in range(len(hist)//3):
                                if int(hist[c2+1]) > max:
                                    max = int(hist[c2+1]) # e.g. max = 82
                                c2+=3
                            sorted_hist.append(hist[hist.index(str(max))-1]) # the course code of max
                            sorted_hist.append(hist[hist.index(str(max))]) # the mark of max
                            sorted_hist.append(hist[hist.index(str(max))+1]) # the grade of max
                            hist[hist.index(str(max))] = 0 # set max to 0 so when checking again it doesnt notice it
                        # print out sorted acedmic history                     
                        c3=0 # another counter
                        for i in range(len(sorted_hist)//3):
                            print(f"{i+1}) {sorted_hist[c3]} {sorted_hist[c3+1]} {sorted_hist[c3+2]}")
                            c3+=3
                        input("Press enter to return")