#This is the menu where the user can choose between A (add), R(remove), L(show list) and X(exit the program)
def main():
    #selection variable is where the user inputs the option they would like to select, the '.upper()' command would convert all lowercase letters to uppercase and Str( converts the input into string type
    selection = str(input("Please Choose A, R, L, or G (‘X’ for exit): ")).upper()
    #if the user inputs 'a' or 'A' the program would go to the studName() function which asks the user to enter the name of a new student
    if selection == "A":
        studName()
    #if the user enters 'r' or 'R' the program would direct to the studNameR() function which removes names from the database
    elif selection == "R":
        studNameR()
    #if the user enters 'l' or 'L' thid would direct to the showList() function which shows the database list
    elif selection == "L":
        showList()
    #if the user enters x or X it will direct to the exitData() function which bracefully exits the program
    elif selection == "X":
        exitData()
    #if the user enters g or G then it would direct the user to input the students grade and credit hours
    elif selection == "G":
        studNameGrade()
    #if the user inputs anything other than a,r,l,g or x then the program with print "invalid option!" and re run the main function again
    else:
        print("invalid option!")
        main()


 #this function checks the first name to see if the user has accidentally inputted an integer instead of a string   
def checkFirstNameINT(firstNameINT):
    #the purpose of the 'try' and 'except' statement is to ensure that if the user enters valid character only 
    try:
        #the program uses a new variable to try converting the parameter variable into an integer
        checkFirsINT = int(firstNameINT)
        #boolean expression checks to see if the new variable is an integer
        while checkFirsINT == int(firstNameINT):
            #if the boolean runs true then an error message would be printed and the main function would be called again
            print(checkFirsINT, "is not a valid first name")
            main()
 
     #this line of code makes sure that program does not crash if the first variable assignment is not an integer       
    except ValueError:
        None

# This function does the same thing as the function on top but it does the validation to see if the first name is a float
def checkFirstNameFLO(firstNameFloat):
    try:
        checkFloat = float(firstNameFloat)
        
        while checkFloat == float(firstNameFloat):
            print(checkFloat, "is not a valid first name")
            main()

    except ValueError:
        None
# This function is similar to the integer validation for the first name however this function checks it for the surname
def checkSurNameINT(surnameINT):
     try:
        checkSurINT = int(surnameINT)
        
        while checkSurINT == int(surnameINT):
            print(checkSurINT, "is not a valid surname")
            main()
            
     except ValueError:
         None

#this function is also does the same thing as the function as for the float validation for the first name but for the surname instead
def checkSurNameFLO(surnameFloat):
    try:
        checkSurFloat = float(surnameFloat)       
        while checkSurFloat == float(surnameFloat):
            print(checkSurFloat, "is not a valid surname")
            main()
            
    except ValueError:
        None
    
    

#this function takes input from the user on the name they want to be added
def studName():
    #'firs' is the variable where the user enters the first name of the new student
    firs = input("New student's name: ")
    #the first name validation functions are called by the program
    checkFirstNameINT(firs)
    checkFirstNameFLO(firs)
    #the while loop below is the validation check to see if the user only pressed the enter key as their input. Loop will continue till they do not press the enter key as input
    while firs == "":
        print("please enter a valid first name")
        firs=str(input("re-enter New students first name: "))
    #the next while loop below is the validation check to see if the user has pressed only a space as their input. The loop will continue till they do not input a space as their input
    while firs == ' ':
        print("please enter a valid first name")
        firs =str(input("re-enter New students first name: "))

    #user is asked to input their surname next and their input is stored on the new variable 'sur'    
    sur = input("New student's surname: ")
    #the validation functions for the surname are now called by the program
    checkSurNameINT(sur)
    checkSurNameFLO(sur)

    #like for the first name, the same new validation check is performed by the program to see if the user had inputted enter or space only.
    while sur == "":
        print("please enter a valid surname")
        sur =str(input("re-enter New students surname: "))
    while sur == ' ':
        print("please enter a valid surname")
        sur =str(input("re-enter New students surname: "))

    # a new variable is created to store the surname and first name as one in that order    
    name = (sur + ',' + ' ' + firs)
    #the add name function now called by the program while holding the first name, surname and full name as perimeters
    addStud(firs,sur,name)
    #the different variables are returned from the function
    return(name,firs,sur)

def addStud(firs,sur,name):
    #this function takes the result of studName() and computes it into the database
    #before computing the result, the function checks to see if the name is in the database first
    if name in alist:
        #if the name is already in the list then an error message is printed and the main function is called
        print("This student is already on the Database.")
        main()
        
    else:
        #if the name isnt in the database then the 'name' is appended in the main list and zeros are appended into the other 3 lists as placeholders for the time being
        alist.append(name)
        gradeList.append(0)
        creditList.append(0)
        gpaList.append(0)
        #the program will print a success message after doing so and then call the main function once again
        print("Student", firs, sur, "has been added to the data base.")
        main()
    return

#the grade function is defined here. The function allows the user to enter the name they want to add the grade and credit hours to
def studNameGrade():
    #the next few lines are the same thing as the name input for the add name function
    firsG = str(input("Student's Name "))
    checkFirstNameINT(firsG)
    checkFirstNameFLO(firsG)
    while firsG == "":
        print("please enter a valid name")
        firsG = str(input("re-enter the students name: "))
    while firsG == ' ':
        print("please enter a valid name")
        firsG =str(input("re-enter the students name: "))
        
    surG = str(input("Student's Surname"))
    checkSurNameINT(surG)
    checkSurNameFLO(surG)
    while surG == "":
        print("please enter a valid surname")
        surG =str(input("re-enter the students surname: "))
    while surG == ' ':
        print("please enter a valid surname")
        surG =str(input("re-enter the students surname: "))

    #nameG stores the whole name as one like the previous variable (name)
    nameG = surG + ',' + ' ' + firsG
    #the actual function that calculates the grade, credit hours and gpa is called with the name variables as its perimeters
    addGrade(nameG,surG,firsG)
    #the name variables are also returned outside of the function
    return(nameG,surG,firsG)

#this function is created to check if the credit hour has been inputted as a float
def checkCreditHour(number):
    #like before, try runs the following code without breaking the entire program
    try:
        #this insures that the user had inputted a float
        value = float(input(number))
        return(value)
    #if they didnt then valueerror would show up. However, try lets us override the error and call addgrade and the main function once again
    except ValueError:
        print("invalid")
        main()
        addGrade(value)
        
#this function calculates the gpa, asks the user for the credit hours and also their grades. Grade name variables are used in this as perimeters
def addGrade(nameG,surG,firsG):
    #new variable is made to store the total value number for the main list with the fullname present (name list)
    countListG = alist.count(nameG)
    #if the name list have the name only one time then an error message and call the main function again
    while countListG != 1:
        print("This Student Is not in the Database!")
        main()
    #this variable stores the index value for the main list with the full name as its perimeter
    insert_at = alist.index(nameG)
    #qpchange uses the insert_at variable for the grade list
    qpChange = gradeList[insert_at]
    #same thing happens here but for the credit hour list
    creditChange = creditList[insert_at]    
    
    #The user is asked to enter the users grade here
    studentsGrade = input("enter Grade A/B/C/D: ")
    
    #the next few lines will run if the user inputs A as their grade
    if studentsGrade == "A":
        #gradepoint is assigned to 4 by default as its Grade A
        gradePoint = 4.0
        #credit hours is stored in this variable with the credit hour check function being called
        creditHours = checkCreditHour("Please enter credit hours: ")
        #if statement validates that credit hours are above 0
        if creditHours > 0 or creditHours == "":
            #new variable (QP) stores the total Quality Points based on credit hours multiplied by gradepoint
            QP = creditHours * gradePoint
            #the next two lines amends the credit hours and Q points if the name already has previous values
            creditList[insert_at] = creditHours + creditChange
            gradeList[insert_at] = qpChange + QP
            #GPA formula is added into the program in the variable gpaForm and the insert at variable is linked with the variable
            gpaForm = round(gradeList[insert_at]/creditList[insert_at],2)
            gpaList[insert_at] = gpaForm
            #A success message is added for the user to know and the main function is called
            print(QP, "QPs added to",nameG)
            main()

        #however if the users input is not valid then an error message would output and the main function will be called again
        else:
            print("invalid Credit Hours")
            main()


    #the next several lines of codes do the same exact thing as the block above but for the input B and the grade point 3.0
    if studentsGrade == "B":        
        gradePoint = 3.0
        creditHours = checkCreditHour("Please enter credit hours: ")
        if creditHours > 0 or creditHours == "":
            QP = creditHours * gradePoint
            
            creditList[insert_at] = creditHours + creditChange
            gradeList[insert_at] = qpChange + QP
            gpaForm = round(gradeList[insert_at]/creditList[insert_at],2)
            gpaList[insert_at] = gpaForm
            print(QP, "QPs added to",nameG)
            main()

        else:
            print("invalid Credit Hours")
            main()


    #the next several lines of codes do the same exact thing as the block above but for the input C and the grade point 2.0
    if studentsGrade == "C":        
        gradePoint = 2.0
        creditHours = checkCreditHour("Please enter credit hours: (>0) ")
        if creditHours > 0 or creditHours == "":
            QP = creditHours * gradePoint
            
            creditList[insert_at] = creditHours + creditChange
            gradeList[insert_at] = qpChange + QP
            gpaForm = round(gradeList[insert_at]/creditList[insert_at],2)
            gpaList[insert_at] = gpaForm
            print(QP, "QPs added to",nameG)
            main()

        else:
            print("invalid Credit Hours")
            main()


    #the next several lines of codes do the same exact thing as the block above but for the input D and the grade point 1.0
    if studentsGrade == "D":        
        gradePoint = 1.0
        creditHours = checkCreditHour("Please enter credit hours: (>0)")
        if creditHours > 0 or creditHours == "":
            QP = creditHours * gradePoint
            
            creditList[insert_at] = creditHours + creditChange
            gradeList[insert_at] = qpChange + QP
            gpaForm = round(gradeList[insert_at]/creditList[insert_at],2)
            gpaList[insert_at] = gpaForm
            print(QP, "QPs added to",nameG)
            main()

        else:
            print("invalid Credit Hours")
            main()



#if the user had inputted a letter other than A/B/C/D then this error message would pop up             
    else:
        print("Invalid Grade")
        main()
        return(QP,creditHours)

 # a function was created to handle the gpa sorting needed for the list sorting. The method we used were bubble sort.       
def gpaSort():
    for pNum in range(len(gpaList)-1,0,-1):
        for ind in range(pNum):
            #the sort would check if the first index value is bigger than the second one
            if gpaList[ind] < gpaList[ind+1]:
                #if it is then two variables are made to store the first values from the gpa and name list
                tempHold = gpaList[ind]
                tempHold2 = alist[ind]
                #the second values is switched with the first values
                gpaList[ind] = gpaList[ind+1]
                alist[ind] = alist[ind+1]
                gpaList[ind+1] = tempHold
                alist[ind+1] = tempHold2


def showList():
    #this functions shows the Database
    #if the length of the full name list equals 0 then the error message is printed and the main function is called back
    if len(alist) == 0:
        print("Database is empty.")
        main()
    #if there is something within name list then the gpaSort function is called
    else:
        gpaSort()
        #for loop is developed for the main list to individualise each element in the list
        for element in alist:
            #new variable is created to hold each index value of the main list
            nOrder = alist.index(element)
            #the for loop will check each element of the credit and grade list to see if any values hold 0 as their value
            if gradeList[nOrder] == 0 or creditList[nOrder] == 0:
                #if they do then they will this message would output
                print(element, "- GPA: None")
            else:
                #gpa new variable will hold the index value of the gpa list 
                gpa = gpaList[nOrder]
                #the students name and gpa will be printed out
                print(element, "- GPA", gpa)

             
        #\n prints out each of the lines in a new line
        strList = '\n'.join(alist)
        
        
        main()
    return

def studNameR():
    #this function takes the input from user on the name they want to be removed
    #validation check is performed just like the previous functions
    firsR = str(input("Name of student to be removed: "))
    checkFirstNameINT(firsR)
    checkFirstNameFLO(firsR)
    while firsR == "":
        print("please enter a valid name")
        firsR = str(input("re-enter the students name: "))
    while firsR == ' ':
        print("please enter a valid name")
        firsR =str(input("re-enter the students name: "))

    surR = str(input("Surname of student to be removed: "))
    checkSurNameINT(surR)
    checkSurNameFLO(surR)
    while surR == "":
        print("please enter a valid surname")
        surR =str(input("re-enter the students surname: "))
    while surR == ' ':
        print("please enter a valid surname")
        surR =str(input("re-enter the students surname: "))
        
    #the surname and first name are stored into a new variable in that order
    nameR = surR + ',' + ' ' + firsR
    #remove function is now called with the name variables as its perimeters
    remStud(nameR,surR,firsR)
    #the name variables are returned
    return(nameR,surR,firsR)

def remStud(nameR,surR,firsR):
    #this function removes the name input by the user in studNameR()
    #the list is counted to see if the name is present
    countList = alist.count(nameR)
    #if statement checks to see if the count of that name is one.
    if countList == 1:
        #if it is then a new variable is made to get the index point of the name in the main list
        remove = alist.index(nameR)
        #del function deletes the name from the list and a success message is printed
        del alist[remove]
        print("Student", firsR, surR, "has been removed from the data base.")
    else:
        #however if the user isnt found within the list then an error message is produced
        print("This student is not found in the Database.")
    #main function is called right after either situation
    main()
    return

#this function is created to allow the user to end the program
def exitData():
    #a success message will print and then the end function will run
    print("Thank You - Goodbye.")
    quit()

#the four lists used by the program are created just before the program is ran and is left empty
alist = []
creditList = []
gradeList = []
gpaList = []
#main menu function is called here at the start of the program when ran
main()





