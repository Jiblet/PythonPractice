# Run with Python 3,5
import random

roll_again = "y"


def get_num_dice():
    while True:
        try:
            return int(input('How many dice? '))
        except:
            print('That isn\'t a number, please try again!')

num_dice = get_num_dice()
print('The values are:')
for x in range(num_dice):
    print(random.randint(1, 6))

roll_again = input("Roll the dice again? ")
