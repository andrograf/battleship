from ascii import rules, title
import sys, time, os
import game, game_nine, game_twelve
from credit import credit

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

run = True

while run:
    clearConsole()
    title()
    print()
    print("""
             (1) Rules

             (2) PLayer vs Player

             (3) Player vs AI

             (4) EXIT""")
    print()
    beker = input("Choose your menu: ")

    if beker == "1":
        clearConsole()
        while run:
            rules()
            print()
            back = input("Press 'Y' for return to main menu: ").upper()
            if back == 'Y':
                clearConsole()
                break
            else:
                print("'{}' is not a menu option!".format(back))
                time.sleep(2)
                clearConsole()

    elif beker == "2":
        while run:
            clearConsole()
            print("""
                Please choose from table sizes:
                
                (1) Easy - 5x5
                
                (2) Medium - 9x9
                
                (3) Hard - 12x12
                
                (4) Unique size""")

            print()
            beker = input("                Choose your menu: ")
            if beker == "1":
                clearConsole()
                game_twelve.main_twelve(number)
                clearConsole()
                break
            elif beker == "2":
                clearConsole()
                game_twelve.main_twelve(number)
                clearConsole()
                break
            elif beker == "3":
                number = 12
                clearConsole()
                game_twelve.main_twelve(number)
                clearConsole()
                break
            else:
                print("'{}' is not a menu option!".format(beker))
                time.sleep(2)
    elif beker == "3":
        while run:
            clearConsole()
            print("""
                Please choose from table sizes:
                
                (1) Easy - 5x5
                
                (2) Medium - 12x12""")
            print()
            beker = input("                Choose your menu: ")
            if beker == "1":
                clearConsole()
                print()
                break
            elif beker == "2":
                clearConsole()
                
                print()
                break
            else:
                print("'{}' is not a menu option!".format(beker))
                time.sleep(2)
    elif beker == "4":
        print("Get off our ship, landlubber!")
        time.sleep(1.5)
        clearConsole()
        credit()
        sys.exit()
    else:
        print("'{}' is not a menu option!".format(beker))
        time.sleep(1.5)
        clearConsole()