from Classes import Course, Program, Semester, Student
from error_handling import *
from Inputing_Data import dictStudent, dictCourseOff, dictSubject, dictPrograms, dictSemester

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
        print("7 - Generate a study plan for a student")
        print("8 - Display list of student achievements for course")
        print("9 - Exit")
        admin_opt = input("Press the respective key to navigate:")
        if not checkValidOptionNumb(admin_opt, 9):
            continue

        if admin_opt == '9': #exit
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
                        while True:
                            new_name = input('Enter a name:')
                            if checkNameValid(new_name): # if valid name, break while loop and continue
                                break
                        
                        while True:
                            new_id = input('Enter a student ID:')
                            if (new_id in dictStudent):
                                print("There is already a student with that ID")
                                continue
                            if checkStudentID(new_id): # if valid id, break while loop and continue
                                break

                        while True:
                            new_dob = input('Enter a date of birth:')
                            if checkDOBValid(new_dob): # if valid dob, break while loop and continue
                                break

                        while True:
                            new_program = input('Enter a program code:')  
                            if new_program in dictPrograms: # if valid dob, break while loop and continue
                                break   
                            else:
                                print("Program not found")

                        dictStudent[new_id] = Student(name = new_name, studentID = new_id, dob = new_dob, programCode = new_program) # create new instance of student and add to  
                        print()
                        print("Successfully added", new_id)
                        input("Press enter to return")  
                            
                            
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
                            if checkStudentID(stud_to_rem) and (stud_to_rem in dictStudent): # if valid id and is a student in the system
                                dictStudent.pop(stud_to_rem) # remove from dictStudent dictionary
                                # for every semester, remove student from every course offering
                                for semester in dictSemester.values():
                                    for offering in semester.course_offerings:
                                        if stud_to_rem in offering.enrolled_students:
                                            # only attempts to remove if in list, else an error is generated
                                            offering.enrolled_students.remove(stud_to_rem)
                                print()
                                print("Successfully removed", stud_to_rem)
                                input("Press enter to return")
                        
        if admin_opt == "2": # add/remove course
            while True:
                print("----------------------------------------")
                print("1 - Add Course")
                print("2 - Remove Course")
                print("3 - Exit")
                course_add_rem = input("Press the respective key to navigate:")

                if not checkValidOptionNumb(course_add_rem, 3):
                    continue

                if course_add_rem == "3": # exit
                    break

                if course_add_rem == "1": # add course option
                    new_title = input('Enter the course title:')
                    new_code = input('Enter the course code:')
                    while True:
                        new_credit = input('Enter the credit:')
                        if new_credit.isdigit(): # if credit just numbers, break while loop and continue
                            break
                        print("Credit must be a number")
                    
                    new_preq = input("Enter a prequisite, or enter 'e' to stop:")
                    preq_list = []
                    while new_preq != 'e':
                        preq_list.append(new_preq)
                        new_preq = input("Enter a prequisite, or enter 'e' to stop:")

                    new_semstr = input("Enter a semester (e.g. S12021), or enter 'e' to stop:")
                    semstr_list = []

                    while new_semstr != 'e':
                        if new_semstr in dictSemester:
                            semstr_list.append(new_semstr)
                        else:
                            print("Invalid semester")
                        new_semstr = input("Enter a semester (e.g. S12021), or enter 'e' to stop:")
                    
                    while True:
                        new_cap = input('Enter the student cap:')
                        if new_credit.isdigit(): # if cap just numbers, break while loop and continue
                            break
                        print("Cap must be a number")

                    #for every applicale semester, add to course offerings list
                    for semester in semstr_list:
                        dictSemester[semester].add_course_offering(new_code, new_cap)
                      
                    dictSubject[new_code] = Course(title = new_title, code = new_code, credit = new_credit, prereques = preq_list, sems = semstr_list) # create new instance of student and add to  
                    print()
                    print("Successfully added", new_code)
                    input("Press enter to return")  
                            
                            
                if course_add_rem == "2": # remove course option
                    while True:
                        print("-----------------------------------------")
                        print("1 - Enter course code")
                        print("2 - Exit")
                        cou_opt = input("Press the respective key to navigate:")
                        if not checkValidOptionNumb(cou_opt, 2):
                            # if input not valid, reprint menu (continue goes to start of while loop)
                            continue

                        if cou_opt == "2": # exit
                            break

                        if cou_opt == "1": # remove course
                            cou_to_rem = input("Enter code of course to remove:")
                            if cou_to_rem in dictSubject:
                                # remove course from semester instances
                                for semester in dictSubject[cou_to_rem].semesters: 
                                    cour_obj = dictSemester[semester].getCourseOfferingObj(cou_to_rem)
                                    if not (cour_obj == False):
                                        dictSemester[semester].course_offerings.remove(cour_obj)
                                
                                dictSubject.pop(cou_to_rem)
                                
                                # remove course from student's currently enrolled 
                                for student in dictStudent.values():
                                    if cou_to_rem in student.currentEnrol:
                                       
                                        index = student.currentEnrol.index(cou_to_rem)
                                        
                                        del student.currentEnrol[index]
                                        del student.currentEnrol[index]
                                        del student.currentEnrol[index]
                                print()
                                print("Successfully removed", cou_to_rem)
                                input("Press enter to return")
                    
                            else:
                                print()
                                print('This course could not be found')
                                                               
        if admin_opt == "3": # add/remove program
            while True:
                print("----------------------------------------")
                print("1 - Add Program")
                print("2 - Remove Program")
                print("3 - Exit")
                prog_add_rem = input("Press the respective key to navigate:")

                if not checkValidOptionNumb(prog_add_rem, 3):
                    continue

                if prog_add_rem == "3": # exit
                    break
                
                if prog_add_rem == "1": # add program
                    
                    new_code = input("Enter the program's code:")
                    
                    # check points is an integer
                    while True:
                        new_points = input("Enter the program's points (e.g. 288):")
                        if new_points.isdigit():
                            break
                        print("Points must be an integer")
                        
                    
                    new_core = input("Enter a core course, or enter 'e' to stop:")
                    core_list = []
                    while new_core != 'e':
                        if new_core in dictSubject:
                            core_list.append(new_core)
                        else:
                            print("Course not found")
                        new_core = input("Enter a core course, or enter 'e' to stop:")
                        
                    new_elective = input("Enter an elective, or enter 'e' to stop:")
                    elective_list = []
                    while new_elective != 'e':
                        if new_elective in dictSubject:
                            elective_list.append(new_elective)
                        else:
                            print("Course not found")
                        new_elective = input("Enter an elective, or enter 'e' to stop:")                    
                   
                    dictPrograms[new_code] = Program(new_code, new_points, core = core_list, electives = elective_list)
                    print()
                    print("Successfully added", new_code)
                    input("Press enter to return")
                    

                if prog_add_rem == "2": # remove program
                    code = input("Enter code of program to remove:")
                    if not (code in dictPrograms):
                        print("Program not found")
                        continue
                    else:
                        del dictPrograms[code]
                    # remove program from students
                    for student in dictStudent.values():
                        if student.programCode == code:
                            student.programCode = '' # set students program to nothing
                    print()
                    print("Successfully removed", code)
                    input("Press enter to return")

        if admin_opt == "4": # add/remove semester
            while True:
                print("----------------------------------------")
                print("1 - Add semester")
                print("2 - Remove semester")
                print("3 - Exit")
                sem_add_rem = input("Press the respective key to navigate:")

                if not checkValidOptionNumb(sem_add_rem, 3):
                    continue

                if sem_add_rem == "3": # exit
                    break
                
                if sem_add_rem == "1": # add semester
                    while True:
                        new_identity = input("Enter a semester identity (e.g., S22021):") 
                        if not (new_identity in dictSemester): # if semester doesn't already exist
                            break # progress
                        print("Semester already exists")

                    semester_obj = Semester(new_identity)
                    # ask course id
                    print()
                    new_course = input("Enter a course ID, or enter 'e' to stop:") 
                    while new_course != 'e':
                        # ask student cap
                        while True:
                            new_cap = input("Enter a student cap:")
                            if new_cap.isdigit():
                                break
                            print("Student cap must be an integer")
                        
                        semester_obj.add_course_offering(id = new_course, cap = new_cap)

                        new_stud = input("Enter a student ID, or enter 'e' to stop:") 
                        while new_stud != 'e':
                            if checkStudentID(new_stud):
                                semester_obj.add_student(new_course, new_stud)
                            new_stud = input("Enter a student ID, or enter 'e' to stop:") 
                                   
                        # repeat process, asking for another course
                        print()
                        new_course = input("Enter a course ID, or enter 'e' to stop:")
                    
                    # add to semester dictionary
                    dictSemester[new_identity] = semester_obj
                    print(dictSemester[new_identity].course_offerings)
                    print(new_identity)
                    print()
                    print("Successfully added", new_identity)
                    input("Press enter to return") 
                    print(dictSemester['S12022'])

                    # until stop for every course offering:
                        # ask course id
                        # ask student cap
                        #until stop:
                            # add student
          
                if sem_add_rem == "2": # remove semester
                    # remove from dictSemester
                    # for every course offering in semester to remove
                        # look at enrolled student list
                            # for the student, uneneroll in that 
                    pass
                     
        if admin_opt == "5": # query student
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
            print("-----------------------------------------")
            id = input("Enter student ID:")
            if checkStudentID(id): # returns true if valid
                if id not in dictStudent: # if student not returned
                    print("Student not found.")
                    continue
            student = dictStudent[id]

            if student.studyPlan == '':
                print("------------Study Plan------------")
                program = dictPrograms[student.programCode]
                toDo = []
                doneSub = []

                for item in program.core_courses:
                    if item in student.academicHist or item in student.currentEnrol:
                        doneSub.append(item)
                    else:
                        toDo.append(item)

                for ToDoIndex in range(len(toDo)):
                    subject = dictSubject[toDo[ToDoIndex]]
                    for subjectPrereq in subject.prerequisites:
                        if subjectPrereq in toDo:
                            toDo.pop(ToDoIndex)
                            toDo.insert(ToDoIndex+1, toDo[ToDoIndex])
                    
                student.studyPlan = toDo

            print(f"Student Study Plan: {[it for it in student.studyPlan]}")
            print()

            print("------------Amend Study Plan------------")

            addrem_inputPlan = input('What class would you like to Add/Remove?: ')
            if addrem_inputPlan not in student.studyPlan:
                addrem_inputPlan2 = input('At what point would this be inserted: ')
                student.studyPlan.insert(int(addrem_inputPlan2), addrem_inputPlan)
            else:
                student.studyPlan.remove(addrem_inputPlan)

            print(f"Student Study Plan: {student.studyPlan}")

            print()
            input('Press enter to go back ')

        if admin_opt == "7": 
            print("------------Generate Study Plan------------")
            id = input("Enter student ID:")
            if checkStudentID(id): # returns true if valid
                if id not in dictStudent: # if student not returned
                    print("Student not found.")
                    continue
                
            student = dictStudent[id]
            program = dictPrograms[student.programCode]
            toDo = []
            doneSub = []

            for item in program.core_courses:
                if item in student.academicHist or item in student.currentEnrol:
                    doneSub.append(item)
                else:
                    toDo.append(item)

            for ToDoIndex in range(len(toDo)):
                subject = dictSubject[toDo[ToDoIndex]]
                for subjectPrereq in subject.prerequisites:
                    if subjectPrereq in toDo:
                        toDo.pop(ToDoIndex)
                        toDo.insert(ToDoIndex+1, toDo[ToDoIndex])
            
            student.studyPlan = toDo

            print(f"Student Study Plan: {student.studyPlan}")

            print()
            input('Press enter to go back')

        if admin_opt == "8": 
            print("------------Student Achievements------------")
            id = input("Enter student ID:")
            if checkStudentID(id): # returns true if valid
                if id not in dictStudent: # if student not returned
                    print("Student not found.")
                    continue
            student = dictStudent[id]

            count = 2
            print(f"{student.name} has achieved above 90% (A+) in the following classes: ")
            for grade in range(len(student.academicHist)):
                if count % 3 == 0 and int(student.academicHist[grade]) >= 90:
                    print(f"    {student.academicHist[grade - 1]} with a score of {student.academicHist[grade]}")
                count += 1

            print()
            input('Press enter to go back')

if __name__ == "__main__": # for testing
    adminMenu()