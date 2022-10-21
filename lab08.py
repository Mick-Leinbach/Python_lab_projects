# Mick Leinbach
# October 21st, 2022
# Lab 08

# Import Math
import math

# Functions
def menu():
    '''Simply print out the options,
       prompt the user for a command,
       and return it to in lowercase form'''
    print(" " * 11, "Grade Menu")
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display Scores")
    print("Q - Quit")
    print()
    command = input("==> ")
    return command.lower()

def advanced_min(my_list):
    '''Returns the minimum value of a list (argument) or 'n\a' if the list is empty.'''
    if len(my_list) > 0:
        return min(my_list)
    else:
        return "n\\a"

def advanced_max(my_list):
    '''Returns the maximum value of a list (argument) or 'n\a' if the list is empty.'''
    if len(my_list) > 0:
        return max(my_list)
    else:
        return "n\\a"

def advanced_average(my_list):
    '''Returns the rounded average of a list (argument) or 'n\a' if the list is empty.'''
    if len(my_list) > 0:
        average = sum(my_list) / len(my_list)
        return round(average, 2)
    else:
        return "n\\a"

def std(my_list):
    '''Returns the standard deviation of a list (argument) or 'n\a' if the list is empty.'''
    if len(my_list) > 0:
        list1 = []
        for num in my_list:
            num -= advanced_average(my_list)
            num = num ** 2
            list1.append(num)
        output = sum(list1) / len(list1)
        output = math.sqrt(output)
        return round(output, 2)
    else:
        return "n\\a"

def get_weighted_score():
    '''Weight the average test score by 60%, weights the average program score by 40%, and adds the two together.
       If one of the score lists is empty, it will simply treat it as a 0.00'''
    global tests
    global programs
    test_score = 0
    program_score = 0

    if len(tests) > 0:
        test_score = advanced_average(tests) * 0.6

    if len(programs) > 0:
        program_score = advanced_average(programs) * 0.4

    return test_score + program_score

def add_test():
    '''Repeatedly asks for a new test score until a valid input is entered
       The program will loop until the value is a positive float value'''
    new_score = "Undefined"

    while new_score == "Undefined":
        try:
            new_score = float(input("\nEnter the new Test score 0-100 ==> "))

            if new_score < 0:
                new_score = "Undefined"
                raise ValueError
        except ValueError:
            print("You must enter a positive number.")
    tests.append(new_score)

def remove_test():
    '''Prompts the user to remove a test score.
       If the user input is not in the list, or if the user input is not a float value,
       the function will tell the user that it has failed to remove anything.'''
    try:
        user_num = int(input("\nEnter the Test to remove 0-100 ==> "))
    except ValueError:
        user_num = "Invalid"
    if user_num in tests:
        tests.remove(user_num)
    else:
        print("Could not find that score to remove")

def clear_tests():
    '''Assigns an empty list to tests, effectively clearing it.'''
    global tests
    tests = []

def add_assignment():
    '''Repeatedly asks for a new assignment score until a valid input is entered
       The program will loop until the value is a positive float value'''
    new_score = "Undefined"

    while new_score == "Undefined":
        try:
            new_score = float(input("\nEnter the new Assignment score 0-100 ==> "))

            if new_score < 0:
                new_score = "Undefined"
                raise ValueError
        except ValueError:
            print("You must enter a positive number.")
    programs.append(new_score)

def remove_assignment():
    '''Prompts the user to remove an assignment score.
       If the user input is not in the list, or if the user input is not a float value,
       the function will tell the user that it has failed to remove anything.'''
    try:
        user_num = int(input("\nEnter the Assignment to remove 0-100 ==> "))
    except ValueError:
        user_num = "Invalid"
    if user_num in programs:
        programs.remove(user_num)
    else:
        print("Could not find that score to remove")

def clear_assignments():
    '''Assigns an empty list to programs, effectively clearing it.'''
    global programs
    programs = []

def display_scores():
    # Print fancy heading
    print("{:<}{:>16}{:>10}{:>10}{:>10}{:>10}".format("Type", "#", "min", "max", "avg", "std"))
    print("=" * 60)
    if len(tests) > 0: # Prints formatted test statistics if there are values in the tests list
        print("{:<}{:>15}{:>10.1f}{:>10.1f}{:>10.2f}{:>10.2f}".format("Tests",len(tests), advanced_min(tests), advanced_max(tests), advanced_average(tests), std(tests)))
    else: # Prints formatted row of "n\a" if the tests list is empty
        print("{:<}{:>15}{:>10}{:>10}{:>10}{:>10}".format("Tests",len(tests), advanced_min(tests), advanced_max(tests), advanced_average(tests), std(tests)))
    if len(programs) > 0: # Prints formatted program statistics if there are values in the programs list
        print("{:<}{:>12}{:>10.1f}{:>10.1f}{:>10.2f}{:>10.2f}".format("Programs",len(programs), advanced_min(programs), advanced_max(programs), advanced_average(programs), std(programs)))
    else: # Prints formatted row of "n\a" if the programs list is empty
        print("{:<}{:>12}{:>10}{:>10}{:>10}{:>10}".format("Programs",len(programs), advanced_min(programs), advanced_max(programs), advanced_average(programs), std(programs)))
    print("\nThe weighted scores is{:>11.2f}".format(get_weighted_score())) # Displays the weighted score, rounded to two decimal places.

# Code Proper
'''create the empty lists tests and programs, and initialize the command variable as 'undefined' '''
tests = []
programs = []
command = "Undecided"

while command != "q": #Until the user chooses to exit the program....
    command = menu() # Bring up the menu

    if command == "d": # Display scores
        display_scores()
        print()
    if command == "1": # Add a test score 
        add_test()
        print()
    if command == "2": # Remove a test score
        remove_test()
        print()
    if command == "3": # Clear test scores
        clear_tests()
        print()
    if command == "4": # Add assignment score
        add_assignment()
        print()
    if command == "5":
        remove_assignment() # Remove assignment score
        print()
    if command == "6":
        clear_assignments() # Clear assignment scores
        print()
