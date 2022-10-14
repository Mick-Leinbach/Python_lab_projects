# Michael "Mick" Leinbach
# October 14th, 2022 (Friday)
# Lab 7 -- Car mpg program

print()
minimum_mpg = "Undecided" # Initialize minimum_mpg

while minimum_mpg == "Undecided": # Until a valid value is given for minimum_mpg...
    try:
        minimum_mpg = float(input("Enter the minimum mpg ==> ")) # Program tries to convert user input into a float

        if minimum_mpg <= 0:
            minimum_mpg = "Undecided" # Reset minimum_mpg so the code block will loop
            raise Exception("Fuel economy given must be greater than 0") # Raise exception if the user's input isn't greater than 0

        if minimum_mpg >= 100:
            minimum_mpg = "Undecided" # Reset minimum_mpg so the code block will loop
            raise Exception("Fuel economy must be less than 100") # Raise exception if the user's input isn't less than 100
            
    except ValueError: # If the user input could not be converted into a float...
        print("You must enter a number for the fuel economy")
    except Exception as excpt: # If the user input wasn't greater than 0 and less than 100...
        print(excpt)

print()

user_file = "Undecided" # Initialize user_file

while user_file == "Undecided": # Until a valid input is given for user_file...
    try:
        user_file = input("Enter the name of the input vehicle file ==> ")
        f = open(user_file,"r") # Attempt to read the file entered by the user
    except IOError or FileNotFoundError: # If the file entered by the user does not exist or cannot exist, tell that to the user and reset user_file so the code block will loop
        print(f"Could not open file {user_file}")
        user_file = "Undecided"

print()

user_output = "Undecided" # Initialize user_output

while user_output == "Undecided": # Until a valid input is given for user_output...
    try:
        user_output = input("Enter the name of the file to output to ==> ")
        file_out = open(user_output, "w") # Attempt to write the file entered by the user
    except IOError: # If the file entered by the user cannot be used as the name for a file, tell that to the user and reset user_output so the code block will loop
        print(f"There is an IO Error {user_output}")
        user_output = "Undecided"

print()

with f as file_in: # Open the input file...
    with open(user_output, "w") as file_out: # Open the output file...
        contents_in = file_in.readlines() # Assign a list of file_in's lines to contents_in
        for line in contents_in[1:]: # For each line in the input file except for the first one...
            # Assign the mpg, year, make, and model values to variables
            mpg = (line.split("\t")[7])
            year = (line.split("\t")[0])
            make = (line.split("\t")[1])
            model = (line.split("\t")[2])
            try:
                float(mpg)# If the mpg value can be "floated"...
                if float(mpg) >= float(minimum_mpg): # If the mpg for this car is greater than the minimum_mpg threshold...
                    file_out.write("{:<20}{:<40}{:>10.3f}".format(year + " " + make, model, float(mpg))) # Write to the output file the year, make, model, and mpg of the car with specific formatting.
                    file_out.write("\n") # Make a new line each time a car's stats are written to the output file.
            except ValueError: # If the mpg value cannot be "floated", tell the user so and move on.
                print(f"Could not convert value {mpg} for vehicle {year} {make} {model}")

        print()
