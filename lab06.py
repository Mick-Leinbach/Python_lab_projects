# Michael "Mick" Leinbach
# October 7th, 2022
# Lab 06

# Import string module
import string

# Menu function prompts the user to enter a selection (1, 2, or Q)
def menu():
    print("MAIN MENU:")
    print("1) Encode a string")
    print("2) Decode a string")
    print("Q) Quit")
    selection = input("Enter your selection ==> ")
    return selection #Returns whatever the user selected

# Encrypt function returns a string (parameter 1) shifted a certain
# number of values (parameter 2)
def encrypt(user_string, shift_value):
    output = "" #Initialize output as an empty string
    for char in user_string: #For every character in the user's string...
        if char.isalpha(): #If it's a letter...
            ch_value = ord(char.lower()) #Get the character's value as a lowercase
            ch_new = ch_value + shift_value #Shift the ord value

            if ch_new > 122: #Loop the value back to "a" if it goes beyond "z"
                ch_new -= 26
            elif ch_new < 97: #Loop the value to "z" if it goes before "a"
                ch_new += 26

            ch_new = chr(ch_new) #Converts the value into a character

            output += ch_new.upper() #Adds the character in uppercase form to the output.
        elif char.isspace(): #If instead it's a blank space...
            output += " " #Add a space to the output if the character is a blank space.
    return output #Return the encrypted/decrypted message

selection = "Undefined" # Initialize selection as "Undefined"

while True: #Until this loop is broken from within...
    while selection != "1" and selection != "2" and selection.upper() != "Q": # While the user input isn't 1, 2, or Q...
        selection = menu() #Run the menu function, return the user's input

    if selection == "1": # If the user chose to encrypt....
        user_string = input("\nEnter (brief) text to encrypt: ") #Prompt the user for the message.
        shift_value = int(input("Enter the number to shift letters by: ")) #Prompt the user for the shift value.
        # Print out the result of the encrypt() function
        # With the arguments that the user just entered.
        print(f"Encrypted: {encrypt(user_string, shift_value)}")
        selection = "Undefined" #Set selection to "Undefined" so the menu will loop again.
        print() # Blank space

    if selection == "2": # If the user chose to decrypt...
        # This block is just like the last one, except for one thing...
        user_string = input("\nEnter (brief) text to decrypt: ")
        # The shift value is the negatory of whatever the user entered,
        # So while it uses the same encrypt() function, it does it "backwards."
        # For example, if you enter a 3 here, it will act as though
        # You entered -3 into the encrypt() function.
        shift_value = -int(input("Enter the number to shift letters by: "))
        print(f"Decrypted: {encrypt(user_string, shift_value)}")
        selection = "Undefined"
        print()

    if selection == "Q": #Break out of the loop if the user's input is "Q" when capitalized
        break
