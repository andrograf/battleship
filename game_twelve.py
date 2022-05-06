import sys, os, ascii, string
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def P1map_generator(number):
    P1map = []
    rows = []
    for i in range(number):
        for s in range(number):
            rows.append("  .  ")
        P1map.append(rows)
        rows = []
    return P1map

def P1display_generator(number):
    P1display = []
    rows = []
    for i in range(number):
        for s in range(number):
            rows.append("  .  ")
        P1display.append(rows)
        rows = []
    return P1display

def P1board_generator(number):
    P1board = []
    rows = []
    letters = list(string.ascii_letters)
    for i in range(number):
        for s in range(number):
            rows.append(f"{letters[26+i]}{s+1}")
        P1board.append(rows)
        rows = []
    return P1board

def P2map_generator(number):
    P2map = []
    rows = []
    for i in range(number):
        for s in range(number):
            rows.append("  .  ")
        P2map.append(rows)
        rows = []
    return P2map

def P2display_generator(number):
    P2display = []
    rows = []
    for i in range(number):
        for s in range(number):
            rows.append("  .  ")
        P2display.append(rows)
        rows = []
    return P2display

def P2board_generator(number):
    P2board = []
    rows = []
    letters = list(string.ascii_letters)
    for i in range(number):
        for s in range(number):
            rows.append(f"{letters[26+i]}{s+1}")
        P2board.append(rows)
        rows = []
    return P2board
#placing phase
def mapP1(board):  #EMPTY BOARD
    letters = list(string.ascii_letters)                
    print('   ',end=(''))
    for i in range(len(board)):
        if len(str(i+1)) == 1:
            print(f'  {i+1}  ', end=" ")
        elif len(str(i+1)) == 2:
            print(f'  {i+1} ', end=" ")
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


def playerOne(player1board, P1map, number): #one block ship
    beker = input("Place your ship: ").upper()
    while True:
        if beker != '' and len(beker)== 2 or len(beker)==3 and int(beker[1:])<=number:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        if beker == player1board[i][j]: 
                            P1map[i][j] = '  S  '
                            return True
                    else:
                        pass
            raise
        elif beker == "QUIT":
            return False
            
        else:
            raise

def playerOne_two(player1board, P1map, number): #two block ship
    beker = input("Place your two-long ship: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        position = input("Give a direction for your ship(left,right,up,down) ").lower()
                        if beker == player1board[i][j] and position == 'left': 
                            if P1map[i][j-1] == '  .  ' and P1map[i][j-1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j-1] = '  S  '
                                return True
                            else:
                                raise
                            
                        elif beker == player1board[i][j] and position == 'right':
                            if P1map[i][j+1] == '  .  ' and P1map[i][j+1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j+1] = '  S  '
                                return True
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'up':
                            if P1map[i-1][j] == '  S  ' and P1map[i-1][j] != '  S  ':
                                P1map[i-1][j] = '  S  '
                                P1map[i][j] = '  S  '
                                return True
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'down':
                            if P1map[i+1][j] == '  .  ' and P1map[i+1][j] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i+1][j] = '  S  '
                                return True
                            else:
                                raise
                    else:
                        pass
            raise
        elif beker == "QUIT":
            return False
        else:
            raise

#three block ship
def playerOne_three(player1board, P1map, number): #three block ship
    beker = input("Place your three-long ship: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        position = input("Give a direction for your ship(left,right,up,down) ").lower()
                        if beker == player1board[i][j] and position == 'left': 
                            if P1map[i][j-1] == '  .  ' and P1map[i][j-1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j-1] = '  S  '
                                P1map[i][j-2] = '  S  '
                                return
                            else:
                                raise
                            
                        elif beker == player1board[i][j] and position == 'right':
                            if P1map[i][j+1] == '  .  ' and P1map[i][j+1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j+1] = '  S  '
                                P1map[i][j+2] = '  S  '
                                return
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'up':
                            if P1map[i-1][j] == '  S  ' and P1map[i-1][j] != '  S  ':
                                P1map[i-1][j] = '  S  '
                                P1map[i-2][j] = '  S  '
                                P1map[i][j] = '  S  '
                                return
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'down':
                            if P1map[i+1][j] == '  .  ' and P1map[i+1][j] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i+1][j] = '  S  '
                                P1map[i+2][j] = '  S  '
                                return
                            else:
                                raise
                    else:
                        pass
            raise
        elif beker == "QUIT":
            sys.exit()
        else:
            raise

def mapP2(board):                    #EMPTY BOARD
    letters = list(string.ascii_letters)                #EMPTY BOARD
    print('   ',end=(''))
    for i in range(len(board)):
        if len(str(i+1)) == 1:
            print(f'  {i+1}  ', end=" ")
        elif len(str(i+1)) == 2:
            print(f'  {i+1} ', end=" ")
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


def playerTwo(player2board, P2map,number): #one-block ship

    beker = input("Place your ship: ").upper()
    while True:
        if beker != '' and len(beker) == 2 or len(beker)==3 and int(beker[1:])<=number:
            for i in range(len(player2board)):
                for j in range(len(player2board[i])):
                    if beker == player2board[i][j] and P2map[i][j] == "  .  ": 
                        if beker == player2board[i][j]: 
                            P2map[i][j] = '  S  '
                            return True
                    else:
                        pass
            raise
        elif beker == "QUIT":
            return False
        else:
            raise

def playerTwo_two(player1board, P1map,number): #two block ship
    beker = input("Place your two-long ship: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        position = input("Give a direction for your ship(left,right,up,down) ").lower()
                        if beker == player1board[i][j] and position == 'left': 
                            if P1map[i][j-1] == '  .  ' and P1map[i][j-1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j-1] = '  S  '
                                return True
                            else:
                                raise
                            
                        elif beker == player1board[i][j] and position == 'right':
                            if P1map[i][j+1] == '  .  ' and P1map[i][j+1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j+1] = '  S  '
                                return True
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'up':
                            if P1map[i-1][j] == '  S  ' and P1map[i-1][j] != '  S  ':
                                P1map[i-1][j] = '  S  '
                                P1map[i][j] = '  S  '
                                return True
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'down':
                            if P1map[i+1][j] == '  .  ' and P1map[i+1][j] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i+1][j] = '  S  '
                                return True
                            else:
                                raise
                    else:
                        pass
            raise
        elif beker == "QUIT":
            return False
        else:
            raise       
            
#three block ship
def playerTwo_three(player1board, P1map,number): #three block ship
    beker = input("Place your three-long ship: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
            for i in range(len(player1board)):
                for j in range(len(player1board[i])):
                    if beker == player1board[i][j] and P1map[i][j] == "  .  ": 
                        position = input("Give a direction for your ship(left,right,up,down) ").lower()
                        if beker == player1board[i][j] and position == 'left': 
                            if P1map[i][j-1] == '  .  ' and P1map[i][j-1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j-1] = '  S  '
                                P1map[i][j-2] = '  S  '
                                return
                            else:
                                raise
                            
                        elif beker == player1board[i][j] and position == 'right':
                            if P1map[i][j+1] == '  .  ' and P1map[i][j+1] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i][j+1] = '  S  '
                                P1map[i][j+2] = '  S  '
                                return
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'up':
                            if P1map[i-1][j] == '  S  ' and P1map[i-1][j] != '  S  ':
                                P1map[i-1][j] = '  S  '
                                P1map[i-2][j] = '  S  '
                                P1map[i][j] = '  S  '
                                return
                            else:
                                raise
                        elif beker == player1board[i][j] and position == 'down':
                            if P1map[i+1][j] == '  .  ' and P1map[i+1][j] != '  S  ':
                                P1map[i][j] = '  S  '
                                P1map[i+1][j] = '  S  '
                                P1map[i+2][j] = '  S  '
                                return
                            else:
                                raise
                    else:
                        pass
            raise
        elif beker == "QUIT":
            sys.exit()
        else:
            raise       
            

#shooting phase
def shootingP1(P1display, P2map, P1board,number):
    beker = input("Place your guess: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
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
        elif beker == "QUIT":
            sys.exit()
        else:
            raise                                             

def shootingP2(P2display, P1map, P2board,number):
    beker = input("Place your guess: ").upper()
    while True:
        if beker != '' and (len(beker)== 2 or len(beker)==3) and int(beker[1:])<=number:
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
        elif beker == "QUIT":
            sys.exit()
        else:
            raise

def P1placing_one(P1board, P1map,number):
    for i in range(3):
        run = True
        while run:
            try:
                print("PLAYER1 - placing phase")
                print()
                #print board - empty
                mapP1(P1map)
                #input player one - reprint board with ships
                if playerOne(P1board,P1map,number) != True:
                    return
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
    clearConsole()

def P1placing_two(P1board, P1map,number):
    for i in range(2):
            run = True
            while run:
                try:
                    print("PLAYER1 - placing phase")
                    print()
                    #print board - empty
                    mapP1(P1map)
                    #input player one - reprint board with ships
                    if playerOne_two(P1board,P1map,number) != True:
                        return                       
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
    clearConsole()
    
def P1placing_three(P1board, P1map,number):
    for i in range(2):
            run = True
            while run:
                try:
                    print("PLAYER1 - placing phase")
                    print()
                    #print board - empty
                    mapP1(P1map)
                    #input player one - reprint board with ships
                    playerOne_three(P1board,P1map,number)                       
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
    
def P2placing_one(P2board, P2map,number):
    for i in range(3):
            run = True
            while run:
                try:
                    print("PLAYER2 - placing phase")
                    print()
                    #print board - empty
                    mapP2(P2map)
                    #input player one - reprint board with ships
                    if playerTwo(P2board,P2map,number) != True:
                        return
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
    clearConsole()

def P2placing_two(P2board, P2map,number):
    for i in range(2):
            run = True
            while run:
                try:
                    print("PLAYER2 - placing phase")
                    print()
                    #print board - empty
                    mapP2(P2map)
                    #input player one - reprint board with ships
                    if playerTwo_two(P2board,P2map,number) != True:
                        return                       
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
    clearConsole()

def P2placing_three(P2board, P2map,number):
    for i in range(2):
            run = True
            while run:
                try:
                    print("PLAYER2 - placing phase")
                    print()
                    #print board - empty
                    mapP2(P2map)
                    #input player one - reprint board with ships
                    if playerTwo_three(P2board,P2map,number):
                        return                       
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

def P1shooting_phase(P1display,P2map,P1board,number):
    while True:
        try:
            print("PLAYER1 - shooting phase")
            print()
            mapP1(P1display)
            shoot1 = shootingP1(P1display,P2map, P1board,number)
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

def P2shooting_phase(P2display,P1map,P2board,number):
    while True:
        try:
            print("PLAYER2 - shooting phase")
            print()
            mapP2(P2display)
            shoot2 = shootingP1(P2display,P1map, P2board,number)
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

#number = board size
def main_twelve(number):
    run = True
    while run:

        P1board = P1board_generator(number)
        P1map = P1map_generator(number)
        P1display = P1display_generator(number)

        P2board = P2board_generator(number)
        P2map = P2map_generator(number)
        P2display = P2display_generator(number)

        clearConsole()
        ascii.placing_phase()
        P1placing_one(P1board, P1map,number) #P1 placing phase
        P1placing_two(P1board, P1map,number)
        P1placing_three(P1board,P1map,number)
        sleep(1)
        clearConsole()
        ascii.player2_switch()
        P2placing_one(P2board,P2map,number) #P2 placing phase
        P2placing_two(P2board,P2map,number)
        P2placing_three(P2board,P2map,number)
        sleep(2)
        
        clearConsole()
        ascii.shooting_phase()
        for i in range(number*number):
            P1shooting_phase(P1display,P2map,P1board,number) #P1 shooting phase
            ascii.player2_switch()
            P2shooting_phase(P2display,P1map,P2board,number) #P2 shooting phase
            ascii.player1_switch()
        break
    ascii.tie_game()
    print("You, admirals, are too strong, could't win this battle.")
    sleep(3)

main_twelve(15)

def test(num):
    P1board = []
    rows = []
    letters = list(string.ascii_letters)
    for i in range(num):
        for s in range(num):
            rows.append(f"{letters[26+i]}{s+1}")
        P1board.append(rows)
        rows = []
    return P1board
#print(test(10))

min = 5 #hajók számának dinamikus növekedésének számolása
num = 5 # nincs ötlet :(
limit = 10
for i in range(num):
    if min <= min:
