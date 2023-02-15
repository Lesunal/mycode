import getpass

# the getpass function from the getpass module is 
# like a "private" version of input()
passcheck = [0,0,0,0]
while passcheck != [1,1,1,1]:
    passwoid= getpass.getpass()

# SUGGESTED FUNCTIONS/METHODS
# len() <-- counts the number of iterables in an object
# str.endswith() <-- checks if a string starts with a character
# str.startswith() <-- checks if a string ends with a character

# is the password a minimum of 8 characters in length?
    if len(passwoid) >= 8:
        passcheck[0]=1
    else:
        print("The password must be a minimum of 8 characters.")
# does the password start with a capital "P"?
    if  passwoid.startswith('P'):
        passcheck[1]=1
    else:
        print("The password must begin with P")
# does the password end with 3?
    if passwoid.endswith('3'):
        passcheck[2]=1
    else:
        print("The password must end with 3")
# does the password NOT have the word "butts" in it?
    if "butts" not in passwoid:
        passcheck[3]=1
    else:
        print("The password must not contain the word butts")
