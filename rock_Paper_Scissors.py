# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:08:17 2021

@author: ILYAS MUTLU
"""

import random
option=["rock","paper","scissors"]
rock=option[0]
paper=option[1]
scissors=option[2]
print("Welcome to the game Press q to end the game")
while True:
    selection = input("Is it rock or paper or scissors?: ")
    selection2 = random.choice(option)
    if selection==rock:
        if selection2==rock:
            print("Computer's choice: Stone Result: Draw")
        elif selection2==paper:
            print("Computer choice Paper: You lost")
        else:
            print("Computer choice scissors: You won")
    if selection==paper:
        if selection2==rock:
            print("Computer selection Stone: You won")
        elif selection2==paper:
            print("Computer selection Paper: Draw")
        else:
            print("Computer choice scissors: You lost")
    if selection==scissors:
        if selection2==rock:
            print("Computer choice Stone: You lost")
        elif selection2==paper:
            print("Computer selection Paper: You won")
        else:
            print("Computer choice of scissors: Draw")
    if selection=='q':
        print("Exiting...")
        break