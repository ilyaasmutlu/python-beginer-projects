import random 
option=["rock","paper","scissors"]
rock=option[0]
paper=option[1]
scissors=option[2]
print("Wolcome to the game press q to end the game")
while True:
    selection = input("Is it rock or paper or scissors?: ")
    selection2 = random.choice(option)
    if selection==rock:
        if selection2==rock:
            print("Computer`s choice: stone result: Draw")
        elif selection2==paper:
            print("Computer choice paper: you lost")
        else:
            print("Computer choice scissors: you won")
    if selection==paper:
        if selection2==rock:
            print("Computer selection stone: you won")

        elif selection2==paper:
            print("Computer selection paper: draw")
        else:
            print("Computer choice scissors: you lost")
    if selection==scissors:
        if selection2==rock:
            print("Computer choice scissors: you lost")
        elif selection2==paper:
            print("Computer selection paper: you won")
        else:
            print("Computer choice scissors: draw")

    if selection=='q':
        print("Exiting ...")
        break