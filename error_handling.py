def checkStudentID(id):
    """Return True if valid ID, else return False. prints related error messages"""
    try:
        if len(id) != 8:
            print("Needs to be excatly 8 characters long, including \'s\'")
            return False
        if id[0] != "s":
            raise ValueError("Id doesn't start with 's'")   
        for i in range(1, len(id)):
            if '0' <= id[i] <= '9':
                continue
            raise ValueError("The characters in id are not digits")
        return True
    except Exception as e:       
        print(e)
        return False

def checkValidOptionNumb(option, max):
    """Returns true if option is a number in the range: 1 to max (inclusive). Else returns False. prints related error messages """
    try:
        # please raise an unique error if not int, with unique message
        # please raise an unique error if not in range, with unique message
        option = int(option)
        if 1 <= option <= max:
            return True
        raise ValueError
    except Exception as e:       
        print(e)
        return False

def checkDOBValid(dob):
    """This functions returns true if dob is in this format: DD/MM/YYYY , e.g. 17/03/2012."""
    # check dob has /
    if not ('/' in dob):
        print("Date of birth needs /")
        return False
    dob = dob.split('/')
    # check dob is in DD/MM/YYYY foramt
    if len(dob[0]) != 2 or len(dob[1]) != 2 or len(dob[2]) != 4:
        print("Needs to be format DD/MM/YYYY")
        return False
    # check dob is made up of numbers
    if not (dob[0].isdigit() and dob[1].isdigit() and dob[2].isdigit()):
        print("Only numbers allowed")
        return False

    # returns true if all conditions meet
    return True
    
def checkNameValid(name):
    """ return false is contains any non alphabet characters. raise an error if appropiate with unique message """

    try:
        if not name.isalpha():
            raise NameError("Invalid Name ")
         # use .isalpha()
        return True
       
    except Exception as e: 
        print(e)      
        return False

if __name__ == "__main__":
    print(checkDOBValid('00/00/2002'))
    #print('0343'.isdigit())