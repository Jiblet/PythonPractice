# Run with Python 3,5
import random

roll_again = "yes"


def get_num_dice():
    while True:
        try:
            return int(input('How many dice? '))
        except:
            print('That isn\'t a number, please try again!')


def get_num_sides():
    while True:
        try:
            return int(input('How many sides per die? '))
        except:
            print('That isn\'t a number, please try again!')


while roll_again == "yes" or roll_again == "y":
    num_dice = get_num_dice()
    num_sides = get_num_sides()
    print('Rolling the dice...')
    print('The values are:')
    for x in range(num_dice):
        print(random.randint(1, num_sides))

    roll_again = input("Roll the dice again? ")
