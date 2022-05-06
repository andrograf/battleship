import sys, os, ascii, string
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def mapP1(board):                    #EMPTY BOARD
    letters = list(string.ascii_letters)                #EMPTY BOARD
    print('   ',end=(''))
    for i in range(len(board)):
        print(f'  {i+1}  ', end=" ")
    for i in range(1):
        print('\n  +',end=(''))
        print('-----+'*len(board))
        for y in range(len(board)):
            print(letters[26+y]+' ', end="|")
            for s in board[y]:
                print(s + '|', end='')
            print()
            for i in range(1):
                print('  +',end=(''))
                print('-----+'*len(board))
            


def playerOne(player1board, P1map):
    beker = input("Place your ship: ").upper()
    while True:
        if beker != '' and len(beker)== 2:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        if beker == player1board[i][j]: 
                            P1map[i][j] = '  S  '
                            return
                    else:
                        pass
            raise
        else:
            raise
        
        
        

def mapP2(board):                    #EMPTY BOARD
    letters = list(string.ascii_letters)                #EMPTY BOARD
    print('   ',end=(''))
    for i in range(len(board)):
        print(f'  {i+1}  ', end=" ")
    for i in range(1):
        print('\n  +',end=(''))
        print('-----+'*len(board))
        for y in range(len(board)):
            print(letters[26+y]+' ', end="|")
            for s in board[y]:
                print(s + '|', end='')
            print()
            for i in range(1):
                print('  +',end=(''))
                print('-----+'*len(board))


def playerTwo(player2board, P2map):
    beker = input("Place your ship: ").upper()
    while True:
        if beker != '' and len(beker) == 2:
            for i in range(len(player2board)):
                for j in range(len(player2board[i])):
                    if beker == player2board[i][j] and P2map[i][j] == "  .  ": 
                        if beker == player2board[i][j]: 
                            P2map[i][j] = '  S  '
                            return
                    else:
                        pass
            raise
        else:
            raise
        

def shootingP1(P1display, P2map, P1board):
    beker = input("Place your guess: ").upper()
    while True:
        if beker != '' and len(beker) == 2:
            for i in range(len(P2map)):
                for j in range(len(P2map[i])):
                    if beker == P1board[i][j]:
                        if P2map[i][j] != '  .  ':
                            P1display[i][j] = "  X  "
                            return True
                        elif P2map[i][j] == '  .  ':
                            P1display[i][j] = "  O  "
                            return False
                        else:
                            pass
            raise
        else:
            raise


def shootingP2(P2display, P1map, P2board):
    beker = input("Place your guess: ").upper()
    while True:
        if beker != '' and len(beker) == 2:
            for i in range(len(P1map)):
                for j in range(len(P1map[i])):
                    if beker == P2board[i][j]:
                        if P1map[i][j] != '  .  ':
                            P2display[i][j] = "  X  "
                            return True
                        elif P1map[i][j] == '  .  ':
                            P2display[i][j] = "  O  "
                            return False
                        else:
                            pass
            raise
        else:
            raise



def main():
    while True:
        P1board=[["A1", "A2", "A3", "A4", "A5"], ["B1", "B2", "B3", "B4", "B5"], ["C1", "C2", "C3", "C4", "C5"], ["D1", "D2", "D3", "D4", "D5"], ["E1", "E2", "E3", "E4", "E5"]]
        P1map=[["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "]]
        P1display=[["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "]]

        P2board=[["A1", "A2", "A3", "A4", "A5"], ["B1", "B2", "B3", "B4", "B5"], ["C1", "C2", "C3", "C4", "C5"], ["D1", "D2", "D3", "D4", "D5"], ["E1", "E2", "E3", "E4", "E5"]]
        P2map=[["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "]]
        P2display=[["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  ", "  .  ", "  .  "]]

        clearConsole()
        
        for i in range(3):
            run = True
            while run:
                try:
                    print("PLAYER1 - placing phase")
                    print()
                    #print board - empty
                    mapP1(P1map)
                    #input player one - reprint board with ships
                    playerOne(P1board,P1map)
                except:
                    print("Invalid coordinates!")
                    sleep(2)
                    clearConsole()
                    continue
                clearConsole()
                break
        print("PLAYER1 - placing phase")
        print()
        mapP1(P1map)
        sleep(2)
        clearConsole()

        
        for i in range(3):
            run = True
            while run:
                try:
                    print("PLAYER2 - placing phase")
                    print()
                    #print board - empty
                    mapP2(P2map)
                    #input player one - reprint board with ships
                    playerTwo(P2board,P2map)
                except:
                    print("Invalid coordinates!")
                    sleep(2)
                    clearConsole()
                    continue
                clearConsole()
                break
        print("PLAYER2 - placing phase")
        print()
        mapP2(P2map)
        sleep(2)
        clearConsole()

        for i in range(3):
            while True:
                try:
                    print("PLAYER1 - shooting phase")
                    print()
                    mapP1(P1display)
                    shoot1 = shootingP1(P1display,P2map, P1board)
                    break
                except:
                    print("Invalid coordinates!")
                    sleep(2)
                    clearConsole()
                    continue
            if  shoot1 == True:
                counter = 0
                for i in range(len(P1display)):
                    for j in range(len(P1display[i])):
                        if P1display[i][j] == '  X  ': 
                            counter += 1
                counter2 = 0
                for i in range(len(P2map)):
                    for j in range(len(P2map[i])):
                        if P2map[i][j] == '  S  ': 
                            counter2 += 1
                
                if counter == counter2:
                    clearConsole()
                    print("PLAYER1 - shooting phase")
                    print()
                    mapP1(P1display)
                    print("All ships are shooted. You won!")
                    sleep(2)
                    sys.exit()
                else:
                    clearConsole()
                    print("PLAYER1 - shooting phase")
                    print()
                    mapP1(P1display)
                    print("Nice shot!")
                    sleep(3)
            elif shoot1 != True:
                clearConsole()
                print("PLAYER1 - shooting phase")
                print()
                mapP1(P1display)
                print("Not lucky, huh?")
                sleep(3)
            clearConsole()
            
            
            #input player two - reprint board with ships
            while True:
                try:
                    print("PLAYER2 - shooting phase")
                    print()
                    mapP2(P2display)
                    shoot2 = shootingP1(P2display,P1map, P2board)
                    break
                except:
                    print("Invalid coordinates!")
                    sleep(2)
                    clearConsole()
                    continue
            if  shoot2 == True:
                if  shoot2 == True:
                    counter = 0
                    for i in range(len(P2display)):
                        for j in range(len(P2display[i])):
                            if P2display[i][j] == '  X  ': 
                                counter += 1
                    counter2 = 0
                    for i in range(len(P1map)):
                        for j in range(len(P1map[i])):
                            if P1map[i][j] == '  S  ': 
                                counter2 += 1
                    
                    if counter == counter2:
                        clearConsole()
                        print("PLAYER1 - shooting phase")
                        print()
                        mapP1(P2display)
                        print("All ships are shooted. You won!")
                        sleep(2)
                        sys.exit()
                    else:
                        clearConsole()
                        print("PLAYER2 - shooting phase")
                        print()
                        mapP2(P2display)
                        print("Nice shot!")
                        sleep(3)
            elif shoot2 != True:
                clearConsole()
                print("PLAYER2 - shooting phase")
                print()
                mapP2(P2display)
                print("Not lucky, huh?")
                sleep(3) 
            clearConsole()
            #shooting phase
            #turns - player1, player2
        break
    ascii.tie_game()
    print("You, admirals, are too strong, could't win this battle.")
    sleep(3)

#main()

