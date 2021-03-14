# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:51:47 2021

@author: ILYAS MUTLU
"""

import random
import time
print("Welcome to the number guessing game!  Guess a number between 1-100")
number = random.randint(1,100)
guessing = 5
while True:
    guess = int(input("Your guess: "))
    
    if guess == number:
        print("Questioning number... ")
        time.sleep(1)
        print("Congratulations! you got it right")
        break
    elif guess > number:
        print("Questioning number... ")
        time.sleep(1)
        guessing-=1
        print("Please enter a smaller number")
        print("Remaining forecast right: ",guessing)
    else:
        print("Questioning number... ")
        time.sleep(1)
        guessing -= 1
        print("Please enter a larger number")
        print("Remaining forecast right: ", guessing)
    if guessing == 0:
        print("Your right to guess is over")
        print("Computer prediction: ",number)
        break