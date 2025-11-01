<h1>Exp 9: Solve Wumpus World Problem using Python demonstrating Inferences from Propositional Logic</h1> 
<h3>Name: HARI PRIYA M                     </h3>
<h3>Register Number: 212224240047             </h3>

<H2>Aim:</H2>
<p>
    To solve  Wumpus World Problem using Python demonstrating Inferences from Propositional Logic
</p>
<h2>Problem Description</h2>
<hr>
<h2>Wumpus World</h2>
<hr>
The Wumpus world is a simple world example to illustrate the worth of a knowledge-based agent and to represent knowledge representation.

The figure below shows a Wumpus world containing one pit and one Wumpus. There is an agent in room [1,1]. The goal of the agent is to exit the Wumpus world alive. The agent can exit the Wumpus world by reaching room [4,4]. The wumpus world contains exactly one Wumpus and one pit. There will be a breeze in the rooms adjacent to the pit, and there will be a stench in the rooms adjacent to Wumpus.

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/cd6b68dc-c79f-4dcb-8126-04da90d65912)

<center>Wumpus World Representation</center>
<p>
This is a python program that uses propositional logic sentences to check which rooms are safe. 

It is assumed that there will always be a safe path that the agent can take to exit the Wumpus world. The logical agent can take four actions: Up, Down, Left and Right. These actions help the agent move from one room to an adjacent room. The agent can perceive two things: Breeze and Stench.
</p>

<hr>

<h2>Algorithm:</h2>

### STEP 1: Start with all variables and domains
Initialize each variable with its possible domain values.

### STEP 2: Select a variable and constraint
Pick a variable and check the constraints involving that variable.

### STEP 3: Apply constraints to reduce domains
Remove any domain values that violate the constraints.

### STEP 4: Propagate the changes
If a variable’s domain is reduced, propagate this change to other related variables.

### STEP 5: Repeat until no more changes
Continue steps 2–4 until all domains are consistent or no further reduction is possible.
<hr>
<h2>Program:</h2>

```python
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
```

<h2>Sample Input and Output:</h2>
<hr>

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/8696111a-a4a7-47cb-ba4b-43a4ef88573f)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/4be5bf06-79fa-4fa0-9334-38a33f06060b)

<h2>Result:</h2>
Thus, the Wumpus World game was successfully implemented in Python. The player was able to navigate through the cave, sense dangers, shoot the Wumpus, and collect gold based on the game logic, demonstrating basic agent-based decision-making.
