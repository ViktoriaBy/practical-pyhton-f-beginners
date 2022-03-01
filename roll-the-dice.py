# ROLL THE DICE GAME

import random

# roll = random.randint(1, 6)
# guess = int(input('Guess the dice roll:\n'))
#
# if guess == roll:
#     print("Correct! They rolled a " + str(roll))
# else:
#     print("Wrong! They rolled a " + str(roll))

#ROLL THE DICE WITH FUNCTIONS
def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('You tie!')

main()