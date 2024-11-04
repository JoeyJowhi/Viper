#Author: Joey Thomas
#Date: Oct. 23, 2024 - ?
#Description: Some prototype for a horror fantasy RPG.

#Required libraries.
import time

#Constants.

#Functions.
def mainmenu():
    print("----------------------------------------")
    print("\n        The All-Encompasssing\n")
    print("             ------------")
    print("             | New Game |")
    print("             | Load Game|")
    print("             | Settings |")
    print("             | Extras   |")
    print("             | Quit     |")
    print("             ------------")
    while True:
        PlaCho = input("\n     Make Your Choice (N/L/S/E/Q).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "N" and PlaCho != "L" and PlaCho != "S" and PlaCho != "E" and PlaCho != "Q":
            print("\n   Input Error: Your choice must be N, L, S, E or Q.\n\n")
        else:
            break

    if PlaCho == "N":
        newgameoptions()
    elif PlaCho == "L":
        pass
    elif PlaCho == "S":
        settingsmenu()
    elif PlaCho == "E":
        extrasmenu()
    elif PlaCho == "Q":
        return "Q"


###New Game##
def newgameoptions():
    print("\n               New Game")
    print("      --------------------------")
    print("      | Save Slot 1: Empty     |")
    print("      | Save Slot 2: Empty     |")
    print("      | Save Slot 3: Empty     |")
    print("      | Save Slot 4: Empty     |")
    print("      | Back                   |")
    print("      --------------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (1/2/3/4/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #PlaCho != "1" and PlaCho != "2" and PlaCho != "3" and PlaCho != "4":
            print("\n   Input Error: Your choice must be 1, 2, 3, 4 or B.\n\n")
        else:
            break
    
    if PlaCho == "B":
        mainmenu()
    elif PlaCho == "1" or PlaCho == "2" or PlaCho == "3" or PlaCho == "4":
        return PlaCho
###^New Game^###


###Settings###
def settingsmenu():
    print("\n               Settings")
    print("             ------------")
    print("             | Graphics |")
    print("             | Controls |")
    print("             | Audio    |")
    print("             | Gameplay |")
    print("             | Back     |")
    print("             ------------")
    while True:
        PlaCho = input("\n     Make Your Choice (G/C/A/P/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "G" and PlaCho != "C" and PlaCho != "A" and PlaCho != "P" and PlaCho != "B":
            print("\n   Input Error: Your choice must be G, C, A, P or B.\n\n")
        else:
            break

    if PlaCho == "B":
        mainmenu()
    elif PlaCho == "G":
        settingsgraphics()
    elif PlaCho == "C":
        settingscontrol()
    elif PlaCho == "A":
        settingsaudio()
    elif PlaCho == "P":
        settingsgameplay()


def settingsgraphics():
    print("\n               Graphics")
    print("      --------------------------")
    print("      | Resolution: 1920x1080  |")
    print("      | Texture Quality: Ultra |")
    print("      | FPS Cap: ON            |")
    print("      | FPS Limit: 144fps      |")
    print("      | Back                   |")
    print("      --------------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (R/T/F/L/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #PlaCho != "R" and PlaCho != "T" and PlaCho != "F" and PlaCho != "L":
            print("\n   Input Error: Your choice must be R, T, F, L or B.\n\n")
        else:
            break
    
    if PlaCho == "B":
        settingsmenu()


def settingsaudio():
    print("\n                 Audio")
    print("           ------------------")
    print("           | Master:   100% |")
    print("           | Music:    100% |")
    print("           | Sound FX: 100% |")
    print("           | Voice:    100% |")
    print("           | Back           |")
    print("           ------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (M/T/S/V/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #and PlaCho != "M" and PlaCho != "T" and PlaCho != "S" and PlaCho != "V":
            print("\n   Input Error: Your choice must be M, T, S, V or B.\n\n")
        else:
            break
    if PlaCho == "B":
        settingsmenu()


def settingscontrol():
    print("\n              Controls")
    print("         ------------------")
    print("         | Keybinds       |")
    print("         | Sensitivity: 8 |")
    print("         | Raw Input: YES |")
    print("         | Controller: NO |")
    print("         | Back           |")
    print("         ------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (K/S/R/C/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #and PlaCho != "K" and PlaCho != "S" and PlaCho != "R" and PlaCho != "C":
            print("\n   Input Error: Your choice must be K, S, R, C or B.\n\n")
        else:
            break
    if PlaCho == "B":
        settingsmenu()


def settingsgameplay():
    print("\n              Gameplay")
    print("         ------------------")
    print("         | NPC Count: HIGH|")
    print("         | Autosave: NO   |")
    print("         | Difficulty: Dy |")
    print("         | Cheats: OFF    |")
    print("         | Back           |")
    print("         ------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (N/A/D/C/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #and PlaCho != "N" and PlaCho != "A" and PlaCho != "D" and PlaCho != "C":
            print("\n   Input Error: Your choice must be N, A, D, C or B.\n\n")
        else:
            break
    if PlaCho == "B":
        settingsmenu()
###^Settings^###


###Extras###
def extrasmenu():
    print("\n            Extras")
    print("         ------------------")
    print("         | Lore           |")
    print("         | Secrets        |")
    print("         | Completion     |")
    print("         | Art            |")
    print("         | Back           |")
    print("         ------------------")
    while True:
        PlaCho = input("\n     Make Your Choice (L/S/C/A/B).\n\n                  ").upper()
        if PlaCho == "":
            print("\n   Input Error: Your choice cannot be empty.\n\n")
        elif PlaCho != "B": #and PlaCho != "L" and PlaCho != "S" and PlaCho != "C" and PlaCho != "A":
            print("\n   Input Error: Your choice must be L, S, C, A or B.\n\n")
        else:
            break
    if PlaCho == "B":
        mainmenu()
###^Extras^###


#Main program.
while True:
    #Input.
    while True:
        Begin = "Y" #input("\nDelve into the depths? (Y/N):   ").upper()
        if Begin == "":
            print("\n   Input Error: You must choose.")
        elif Begin != "Y" and Begin != "N":
            print("\n   Input Error: Choose Y or N. There is no other option.")
        else:
            break

    #Processing.
    if Begin == "Y":
        PlaCho = mainmenu()
    else:
        break

    if PlaCho == "Q":
        break
    elif PlaCho == "1" or PlaCho == "2" or PlaCho == "3" or PlaCho == "4":
        

        #Game Start.
        print(time.sleep(1))







        

#Housekeeping
print("\nThank you for playing!\n")