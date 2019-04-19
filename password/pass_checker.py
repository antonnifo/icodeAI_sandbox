import re

def get_password():
    return input("Input your password  ")

def validate_password(p):
    if (len(p)<6 or len(p)>12):
        return("Your Password {} is Invalid it should have a minumum of 6 characters & a maximum of 12 characters".format(p))     
    elif not re.search("[a-z]",p):
        return("Your Password {} is Invalid it should contain at least a lowercase character".format(p))
    elif not re.search("[0-9]",p):
        return("Your Password {} is Invalid it should contain at least a number".format(p))
    elif not re.search("[A-Z]",p):
        return("Your Password {} is Invalid it should contain at least a capital character".format(p))
    elif not re.search("[$#@]",p):
        return("Your Password {} is Invalid it should contain at least a special character".format(p))
    elif re.search("\s",p):
        return("Your Password {} is Invalid it should not contain white spaces".format(p))
    else:
        return("Your password {} is Valid".format(p))
          
if __name__ == '__main__':
    print(validate_password(get_password()))
                