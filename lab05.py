########################################################################
##
## CS 101 Lab
## Program # 4
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

#import modules needed

import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    # Asks the user if they want to play again
    playing = input("Do you want to play again ==> ")

    # Repeatedly ask for an input until an acceptable one is entered. Always checks the lowercase version so that the program doesn't have to be case sensitive.
    while playing.lower() != "yes" and playing.lower() != "y" and playing.lower() != "n" and playing.lower() != "no":
        print("\nYou must enter Y/YES/N/NO to continue. Please try again")
        playing = input("Do you want to play again ==> ")

    # Returns true if the player enters "Y" or "YES," returns false if they entered "N" or "NO"
    if playing.lower() == "yes" or playing.lower() == "y":
        return True
    else:
        return False
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    # Get the player's wager
    wager = int(input("How many chips do you want to wager? ==> "))

    # Loops if the wager is outside the acceptable range
    while wager <= 0 or wager > bank:
        if wager <= 0: # Response if the wager isn't greater than zero
            print("The wager amount must be greater than 0. Please enter again.")
            wager = int(input("How many chips do you want to wager? ==> "))
        else: # Reponse if the wager is above the bank amount
            print(f"The wager cannot be greater than how much you have. {bank}")
            wager = int(input("How many chips do you want to wager? ==> "))

    # Returns the wager once the user has entered something acceptable
    return wager            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    # The three variables are all assigned a random number from 1 (inclusive) to eleven (exclusive)
    reel1 = random.choice(range(1,11))
    reel2 = random.choice(range(1,11))
    reel3 = random.choice(range(1,11))
    # Returns the three variables as a tuple
    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    # Checks if all three values are equal. (This method works because of the transient property: if a = b, and b = c, then a = c).
    if reela == reelb and reelb == reelc:
        # Return 3 if all numbers match
        return 3
    # If there isn't a triple match, is there at least one pair of matching numbers?
    elif reela == reelb or reelb == reelc or reela == reelc:
        # Return 2 if there is one pair of matching numbers
        return 2
    else:
        # There are no matching numbers, so return 0
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    # Get user input
    bank = int(input("How many chips do you want to start with? ==> "))

    # Loop if the user's initial bank is outside the acceptable range.
    while bank <= 0 or bank > 100:
        # Alert the user and ask again if the input isn't greater than zero.
        if bank <= 0:
            print("Too low a value, you can only choose 1 - 100 chips")
            bank = int(input("How many chips do you want to start with? ==> "))
        # Alert the user and ask again if the input isn't less than 100.
        if bank > 100:
            print("Too high a value, you can only choose 1 - 100 chips")
            bank = int(input("How many chips do you want to start with? ==> "))

    # Return the user's inputted bank once they have entered something acceptable.
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    # If all three numbers matched, the payout is ten times the wager minus the wager.
    if matches == 3:
        payout = (10 * wager) - wager
    # If only two numbers matched, the payout is three times the wager minus the wager.
    elif matches == 2:
        payout = (3 * wager) - wager
    # If no numbers matched, the payout is a loss of money equal to the wager.
    else:
        payout = wager * -1

    # Return the user's payout
    return payout   


if __name__ == "__main__":

    # Start the program by setting the playing variable to True
    playing = True

    # Repeat until the player is no longer playing
    while playing:

        # Initialize variables. Store the bank's initial value in bankStart for later.
        bank = get_bank()
        bankStart = bank
        spins = 0
        record = bank

        # Repeat until the user runs out of money
        while bank > 0:

            # Get an acceptable wager
            wager = get_wager(bank)

            # Gets three results from the slot machine, increments the number of spins.
            reel1, reel2, reel3 = get_slot_results()
            spins += 1

            # See how many matches there are, get the payout, and add the payout to the amount in the bank.
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            # If the current amount in the bank breaks the record, update the record.
            if bank > record:
                record = bank

            # Tell the user what their spin was, how many reels they matched, how much money they won or lost, and how much money they have left
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        # Once the user runs out of money...
        # Remind the user of how much money they started with and tell them how many spins it took to lose it all.
        print("You lost all", bankStart, "in", spins, "spins")
        # Tell the user the most chips they had throughout the game
        print("The most chips you had was", record)
        # Ask the user if they would like to play again
        playing = play_again()
