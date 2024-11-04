#Author: Joey Thomas
#Date: Sept. 18 - 27, 2024
#Description: This is a little side project with the goal of playing blackjack in python.
import random

#Prevent undefined errors.
Player = 0
Dealer = 0
#Gather and format user input.
print()
Start = str(input("Would you like to play Blackjack? (y/n): ")).lower()
if Start == "y":
    print("Lets begin!")
    print()
    Player = random.randint(2, 11)
    Player += random.randint(2, 11)
    print(f"The dealer hands you 2 cards, their total value being {Player}.")
    Dealer = random.randint(2, 11)
    Dealer += random.randint(2, 11)
    print(f"The dealer reveals their 2 cards, their total value being {Dealer}.")
    print()
    if Dealer >= 17:
        print(f"The dealer stands at {Dealer}.")
        print()
else:
    print("Have a good day.")
    print()

while Start == "y" and Player < 22 and Dealer < 22:
    PlaDes = str(input("Would you like to hit or stand? (h/s)")).lower()
    if PlaDes == "s" and Dealer > Player:
        print(f"You stand on {Player}.")
        print("The dealer wins!")
        break
    if PlaDes == "s" and Dealer < Player and Dealer >= 17:
        print(f"You stand on {Player}.")
        print("The dealer hits!")
        Dealer += random.randint(2,11)
        print()
        print(f"The dealer's new card value is {Dealer}.")
        if Dealer > 22:
            break
        elif Dealer == 21:
            print("The dealer wins with Blackjack!")
        elif Dealer > Player:
            print("The dealer wins!")
        elif Dealer > 21:
            print("The dealer ")