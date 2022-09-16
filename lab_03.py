# Greet the user
print("Welcome to the Flarsheim Guesser!\n")

wants_to_play = "Y"

while wants_to_play == "Y" or wants_to_play == "y":

    print("Please think of a number between and including 1 and 100.\n")

    # Initialize Variables at -1
    divided_by_3 = -1
    divided_by_5 = -1
    divided_by_7 = -1
    magic_number = -1

    # Refuse to accept any input until it is between 0 and 2 (inclusive)
    # If the input is not acceptable, state why it isn't and ask again
    while divided_by_3 == -1:
        divided_by_3 = int(input("What is the remainder when your number is divided by 3 ?"))
        if divided_by_3 < 0:
            print("The value entered must be 0 or greater.")
            divided_by_3 = -1
        if divided_by_3 >= 3:
            print("The value entered must be less than 3.")
            divided_by_3 = -1
    else:
        print() #Once an input is acceptable, put a space between this prompt and the "5 prompt"
        
    # Refuse to accept any input until it is between 0 and 4 (inclusive)
    # If the input is not acceptable, state why it isn't and ask again
    while divided_by_5 == -1:
        divided_by_5 = int(input("What is the remainder when your number is divided by 5 ?"))
        if divided_by_5 < 0:
            print("The value entered must be 0 or greater.")
            divided_by_5 = -1
        if divided_by_5 >= 5:
            print("The value entered must be less than 5.")
            divided_by_5 = -1
    else:
        print() #Once an input is acceptable, put a space between this prompt and the "7 prompt"

    # Refuse to accept any input until it is between 0 and 6 (inclusive)
    # If the input is not acceptable, state why it isn't and ask again
    while divided_by_7 == -1:
        divided_by_7 = int(input("What is the remainder when your number is divided by 7 ?"))
        if divided_by_7 < 0:
            print("The value entered must be 0 or greater.")
            divided_by_7 = -1
        if divided_by_7 >= 7:
            print("The value entered must be less than 7.")
            divided_by_7 = -1
    else:
        print() #Once an input is acceptable, create a new line

    # User the user's three inputs to "divine" their number
    for i in range(1, 101):
        if ((i % 3) == divided_by_3) and ((i % 5) == divided_by_5) and ((i % 7) == divided_by_7):
            magic_number = i
            break

    # Print answer and brag about it, or tell the user that their number wasn't in the range
    if magic_number == -1:
        print("Your number is not in the range.\n")
    else:
        print(f"Your number was  {magic_number}")
        print("How amazing is that?\n")

    # Ask the user if they want to play again. Keep asking until they respond with "Y" or "N"
    wants_to_play = "Undecided"
    while wants_to_play != "Y" and wants_to_play != "N" and wants_to_play != "y" and wants_to_play != "n":
        wants_to_play = input("Do you want to play again? Y to continue, N to quit ==> ")
