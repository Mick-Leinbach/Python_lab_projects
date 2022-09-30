########################################################################
##
## CS 101 Lab
## Program # 5
## Mick Leinbach
## mtl9pn@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
# import statements
# functions

# Returns one of three schools depending on the sixth character of the code. If the fifth character isn't 1, 2, or 3, return "Invalid School"
def get_school(user_string):
    if user_string[5] == "1":
        return "School of Computing and Engineering SCE"
    elif user_string[5] == "2":
        return "School of Law"
    elif user_string[5] == "3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

# Returns one of four grades depending on the seventh character of the code. If the seventh character isn't 1, 2, 3, or 4, return "Invalid Grade"
def get_grade(user_string):
    if user_string[6] == "1":
        return "Freshman"
    elif user_string[6] == "2":
        return "Sophomore"
    elif user_string[6] == "3":
        return "Junior"
    elif user_string[6] == "4":
        return "Senior"
    else:
        return "Invalid Grade"

# Convert a character into its character value and then subtract it by 65 so that A = 0, B = 1, C = 2, etc. Return that number of 0-25.
def character_value(char):
    output = ord(char) - 65
    return output

# Perform the complicated formula, multiplying the numbers in the first five characters with their position in the string plus one, and return the final digit of the result.
def get_check_digit(user_string):
    total = 0
    i = 0
    
    while i <= 4:
        total += (i + 1) * character_value(user_string[i])
        i += 1
        
        
    while i <= 8:
        total += (i + 1) * int(user_string[i])
        i += 1
        
    output = total % 10
    return output

# Makes sure that the first five characters of the string are letters. If they aren't, return false and specify the position of the offending character, and what that character is.
def verify_alpha_start(user_string):
    i = 0
    while i <= 4:
        if user_string[i].isalpha() == False:
            return False, i, user_string[i]
        i += 1
    return True, 0, 0

# Makes sure that the last three characters of the string are numbers. If they aren't, return False and specify the position of the offending character, and what that character is.
def verify_number_end(user_string):
    i = 7
    while i <= 9:
        if user_string[i].isdigit() == False:
            return False, i, user_string[i]
        i += 1
    return True, 0, 0

# Returns false if the code isn't ten characters long.
def verify_check_digit(user_string):
    if len(user_string) != 10:
        return False, "The length of the number given must be 10"

    # Unpack the values of the verify_alpha_start and verify_number_end functions.
    alphaPresent, alphaOffenderIndex, alphaOffenderChr = verify_alpha_start(user_string)
    numberPresent, numberOffenderIndex, numberOffenderChr = verify_number_end(user_string)

    # Get the school and grade in the form of a string
    school = get_school(user_string)
    grade = get_grade(user_string)

    
    if alphaPresent == False: # Error if the code isn't 10 digits long
        return False, f"The first 5 characters must be A-Z, the invalid character is at {alphaOffenderIndex} is {alphaOffenderChr}"
    elif numberPresent == False: # Error if the last three characters aren't numbers
        return False, f"The last 3 characters must be 0-9, the invalid character is at {numberOffenderIndex} is {numberOffenderChr}"
    elif school == "Invalid School": # Error if the sixth digit doesn't correspond to one of the three schools.
        return False, "The sixth character must be 1 2 or 3"
    elif grade == "Invalid Grade": # Error if the seventh digit doesn't correspond to one of the four grades.
        return False, "The seventh character must be 1 2 3 or 4"
    elif user_string[9].isdigit() == False or get_check_digit(user_string) != int(user_string[9]): # Error if the check digit doesn't match the last digit of the code.
        return False, f"Check Digit {user_string[9]} does not match calculated value {get_check_digit(user_string)}."
    else:
        return True, "" # Return True if the code passes every test.

if __name__ == "__main__":
    # main program
    validity, reason = "Undecided", "Undecided" # Initialize validity and reason
    code = "Undecided" # Initialize code

    # Print a fancy header
    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("=" * 60)

    # Repeat the loop until the user simply hits Enter
    while code != "":
        code = input("\nEnter Library Card.  Hit Enter to Exit ==> ") # Get a code from the user.
        if code == "": # Breaks the loop if the user just hit Enter
            break
        validity, reason = verify_check_digit(code) # Unpacks results of verify_check_digit into validity and reason
        if validity == False: # If the code is invalid, inform the user of that and specify why it's invalid.
            print("Library card is invalid.")
            print(reason)
        if validity == True: # If the code is valid, inform the user of that and inform them of the student's school and grade.
            print("Labrary card is valid.")
            print(f"The cards belong to a student in {get_school(code)}")
            print(f"The card belongs to a {get_grade(code)}")
