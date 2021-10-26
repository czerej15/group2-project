def checkStudentID(id):
    """Return True if valid ID, else return False. prints related error messages"""
    try:
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
        # please raise an error if not int, with unique message
        # please raise an error if not in range, with unique message
        option = int(option)
        if 1 <= option <= max:
            return True
        raise ValueError
    except Exception as e:       
        print(e)
        return False

def checkYorN(inpt):
    # check if inpt == 'y' or 'n' and return True
    # else neither, return false print('Not valid option')
    try:
        return True
    except:
        return False
    