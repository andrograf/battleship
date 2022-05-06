def display_map(map, shot_map, player):
    letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if player=="X":
        other_player="O"
    else:
        other_player="X"
    print("  ", end="")
    for i in range(1, len(map[0])+1):
        print(f"| {i} ", end="")
    print("|")
    print("__", end="")
    for i in range(1, len(map[0])+1):
        print("|___", end="")
    print("|")
    letter=0
    for Y in range(len(map)):
        print("  ", end="")
        for i in range(len(map[Y])):
            print("|   ", end="")
        print("|")
        print(letters[letter], end=" ")
        letter+=1
        for X in range(len(map[Y])):
            print("| ", end="")
            if map[Y][X]==player:
                print(player, end="")
            elif map[Y][X]==other_player and shot_map[Y][X]=="S":
                print(other_player, end="")
            elif shot_map[Y][X]=="S":
                print("S", end="")
            else:
                print(".", end="")
            print(" ", end="")
        print("|")
        print("__", end="")
        for i in range(len(map[Y])):
            print("|___", end="")
        print("|")
#map=[[".", ".", "X", "X", "."], [".", "O", "O", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]
#shot_map=[[".", ".", ".", "S", "."], [".", ".", "S", ".", "."], [".", "S", "S", "S", "."], [".", ".", ".", ".", "."], [".", "S", "S", ".", "."]]
#display_map(map, shot_map, "X")