# Project:1
# Snake , Water and Gun Game     or
# Rock, Paper and Scissor Game

import random


# Game Function (definition)
def gameWin(comp, you):
    # if two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose 's'
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # Check for all possibilities when computer chose 'w'
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # Check for all possibilities when computer chose 'g'
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


# Computer's Turn To choose
comp = print("Computer's Turn : Snake (s), Water (w), Gun (g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'  #Snake

elif randNo == 2:
    comp = 'w'  #Water

elif randNo == 3:
    comp = 'g'  #Gun

# Your Turn to Choose
you = input("Your Turn       : Snake (s), Water (w), Gun (g)?  : ")

print(end='\n'"Output:\n")

# What both Player's Chose
print(f"Computer's Chose : {comp} ")
print(f"You Chose        : {you} ")

print(end='\n'"Output:\n")

#main()

a = gameWin(comp, you)   #call the function

if a == None:
    print("Game Tie!")

elif a:
    print("You Won!")

else:
    print("You Lose!")
