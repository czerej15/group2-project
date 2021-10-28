def checkStudentID(id):
    """Return True if valid ID, else return False. prints related error messages"""
    try:
        # also check if length of id is correct (needs to be 8 characters exactly, including s) 
        # print unique message if not as well
        # like what u did with: raise ValueError("Id doesn't start with 's'")   
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
    """This functions returns true if dob is in this format: DD/MM/YYYY , e.g. 17/03/2012"""
    try:
         return True
       
    except:       
        return False

def checkNameValid(name):
    """ return false is contains any non alphabet characters """
    try:
         # use .isalpha()
         return True
       
    except:       
        return False

    