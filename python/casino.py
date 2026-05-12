#import libraries or packages
import os
from random import randint
#declare and initialize variables and/or constants
lives = 3
dice1 = 0
dice2 = 0  
roll_count = 0
equal_count = 0
dices_add = 0
status = True


#functions
def rollDices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2




#main
while status:
    os.system("cls")
    dices = rollDices()
    roll_count += 1
    dices_add = 0
    print("#" * 20)
    print(f"roll dices N°: {roll_count}")
    print("#" * 20)
    print(f"player lives:  {player_lives}")
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]
    
    if dices_add%2 != 0:
        player_lives -= 1
        print(f"you lose a life, you have {player_lives} lives left")
    
    if roll_count == 5:
        break
    else:
        press_key = input("\npress any key to roll the dices again")