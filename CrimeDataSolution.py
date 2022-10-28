# Michael "Mick" Leinbach
# October 28th, 2022
# Lab #9 - CrimeDataSolution

# Import Module
import csv

# Functions

def create_reported_date_dict(user_list):
    '''Gets the list of all the crime data
    and then creates a dictionary where the keys are dates
    value is the number of crimes reported on each date'''
    output_dict = {}
    for row in user_list[1:]:
        if row[1] not in output_dict.keys():
            output_dict[row[1]] = 1
        else:
            output_dict[row[1]] += 1
    return output_dict

def create_offense_by_zip(user_list):
    ''''Gets the list of all the crime data
    and then creates a dictionary where the keys are offenses
    and the values are each a dictionary where the key is a zip-code
    and the value is the number of offenses committed of that offense in that zip-code''''
    output_dict = {}
    for row in user_list[1:]:
        offense = row[7]
        zc = row[13]
        if offense not in output_dict:
            output_dict[offense] = dict({})
        try:
            output_dict[offense][zc] += 1
        except KeyError:
            output_dict[offense][zc] = 1
    return output_dict

def create_offense_dict(user_list):
    '''Creates a dictionary from the crime data
    the keys are the different types of offenses
    and each value is the number of times each offense was committed'''
    output_dict = {}
    for row in user_list[1:]:
        try:
            output_dict[row[7]] += 1
        except KeyError:
            output_dict[row[7]] = 1
    return output_dict

def create_reported_month_dict(user_list):
    '''Creates a dictionary from the crime data
    the keys are the months of the year (integers 1-12)
    and each value is the number of offenses committed on that month'''
    output_dict = {}
    for row in user_list[1:]:
        dates = row[1].split("/")
        month = int(dates[0])
        try:
            output_dict[month] += 1
        except KeyError:
            output_dict[month] = 1
    return output_dict

def month_from_number(user_int):
    '''Takes an integer (1-12) and converts it to a string
    of the corresponding month. Raises a ValueError if the input
    is not acceptable.'''
    if user_int == 1:
        return "January"
    elif user_int == 2:
        return "February"
    elif user_int == 3:
        return "March"
    elif user_int == 4:
        return "April"
    elif user_int == 5:
        return "May"
    elif user_int == 6:
        return "June"
    elif user_int == 7:
        return "July"
    elif user_int == 8:
        return "August"
    elif user_int == 9:
        return "September"
    elif user_int == 10:
        return "October"
    elif user_int == 11:
        return "November"
    elif user_int == 12:
        return "December"
    else:
        raise ValueError("Month must be 1-12")

def read_in_file(filename):
    '''Takes a string, opens it as a csv file, and converts it into a list'''
    with open(filename, "r", encoding = "utf-8") as filename:
        csv_infile = csv.reader(filename)
        return list(csv_infile)
        

# Main program
if __name__ == "__main__":
    user_file = "Null"
    while user_file == "Null": # This loop will make simply sure the user's input is in the directory, closing the file once it is confirmed to exist.
        user_file = input("Enter the name of the crime data file ==> ")
        try:
            my_file = open(user_file, "r")
            print()
            my_file.close()
        except FileNotFoundError:
            print(f"Could not find the file specified. {user_file} not found")
            user_file = "Null"
    data_list = read_in_file(user_file) # Turn the user's input into a list of data
    month_data = create_reported_month_dict(data_list) # Create the month_data dictionary
    worst_month = max(month_data, key=month_data.get) # Get the month with the most offenses
    highest_number = month_data[worst_month] # Get the number of offenses committed on the worst month
    print(f"The month with the highest # of crimes is {month_from_number(worst_month)} with {highest_number} offenses") # Display the month with the highest number of crimes and how many crimes were committed
    crime_data = create_offense_dict(data_list) # Create the crime_data dictionary
    popular_crime = max(crime_data, key=crime_data.get) # Get the crime with the most offenses
    popular_number = crime_data[popular_crime] # Get the amount of times that offense was committed
    print(f"The offense with the highest # of crimes is {popular_crime} with {popular_number} offenses") # Display the most common crime and how many times it was committed
    print()
    user_offense = "null"
    while user_offense == "null": # Repeatedly ask the user for an offense until they enter something valid.
        user_offense = input("Enter an offense")
        if user_offense not in crime_data:
            print("Not a valid offense found, please try again")
            user_offense = "null"
        else: # Display a formatted table of how many times the given crime has been committed in each zip-code.
            zip_list = create_offense_by_zip(data_list) 
            crime_zip_list = zip_list[user_offense]
            print(f"\n{user_offense} offenses by Zip Code")
            print("{:<8}{:>22}".format("Zip Code", "# Offenses"))
            print("=" * 30)
            for key in crime_zip_list:
                print("{:<5}{:>25}".format(key, crime_zip_list[key]))
    
