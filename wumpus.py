#Program developed by
# NAME : HARI PRIYA M
# REG NO : 212224240047

wumpus = [["Save", "Breeze", "PIT", "Breeze"],
          ["Smell", "Save", "Breeze", "Save"],
          ["WUMPUS", "GOLD", "PIT", "Breeze"],
          ["Smell", "Save", "Breeze", "PIT"]]

# Initial Variables
row = 0              # player's current row position
column = 0           # player's current column position
arrow = True         # player has one arrow initially
player = True        # controls the game loop
score = 0            # initial score

while player:
    choice = input("press u to move up\npress d to move down\npress l to move left\npress r to move right\n")
    
    if choice == "u":
        if row != 0:
            row -= 1
        else:
            print("move denied")
        print("current location: ", wumpus[row][column], "\n")

    elif choice == "d":
        if row != 3:
            row += 1
        else:
            print("move denied")
        print("current location: ", wumpus[row][column], "\n")

    elif choice == "l":
        if column != 0:
            column -= 1
        else:
            print("move denied")
        print("current location: ", wumpus[row][column], "\n")

    elif choice == "r":
        if column != 3:
            column += 1
        else:
            print("move denied")
        print("current location: ", wumpus[row][column], "\n")

    else:
        print("move denied")

    # When player senses a smell (Wumpus nearby)
    if wumpus[row][column] == "Smell" and arrow != False:
        arrow_choice = input("do you want to throw an arrow? (y/n): ")
        if arrow_choice == "y":
            arrow_throw = input("press u to throw up\npress d to throw down\npress l to throw left\npress r to throw right\n")

            if arrow_throw == "u":
                if row > 0 and wumpus[row - 1][column] == "WUMPUS":
                    print("Wumpus killed!")
                    score += 1000
                    print("score: ", score)
                    wumpus[row - 1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted...")
                    score -= 10
                    print("score: ", score)

            elif arrow_throw == "d":
                if row < 3 and wumpus[row + 1][column] == "WUMPUS":
                    print("Wumpus killed!")
                    score += 1000
                    print("score: ", score)
                    wumpus[row + 1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted...")
                    score -= 10
                    print("score: ", score)

            elif arrow_throw == "l":
                if column > 0 and wumpus[row][column - 1] == "WUMPUS":
                    print("Wumpus killed!")
                    score += 1000
                    print("score: ", score)
                    wumpus[row][column - 1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted...")
                    score -= 10
                    print("score: ", score)

            elif arrow_throw == "r":
                if column < 3 and wumpus[row][column + 1] == "WUMPUS":
                    print("Wumpus killed!")
                    score += 1000
                    print("score: ", score)
                    wumpus[row][column + 1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted...")
                    score -= 10
                    print("score: ", score)

            arrow = False

    # If the player encounters the Wumpus directly
    if wumpus[row][column] == "WUMPUS":
        score -= 1000
        print("\nWumpus here!!\nYou Die\nYour score is:", score, "\n")
        break

    # If the player finds GOLD
    if wumpus[row][column] == "GOLD":
        score += 1000
        print("\nCongratulations!! You found the GOLD!")
        print("You Win! Your final score is:", score, "\n")
        break

    # If the player falls into a PIT
    if wumpus[row][column] == "PIT":
        score -= 1000
        print("Ahhhhh!!!!\nYou fell into a pit.\nYour score is:", score, "\n")
        break
