from random import randint
import time
from collections import OrderedDict

cast_again = 'r'
statistics = OrderedDict()
casts = 0
menu_options = """
> Options:
>    R - to cast again;
>    S - view stats;
>    E - exit the programme.
> """


def rollDice(dice):
    input('> Press Enter to cast dice!')
    time.sleep(1)
    cast_result = []
    for a_cast in range(0, dice):
        cast_result.append(randint(1, 6))
    return cast_result


def atLeastALetterInput(text_to_display):
    cast_again = 'x'
    try:
        cast_again = input(text_to_display)[0].lower()
        return cast_again
    except IndexError:
        print('> Please make sure input is valid before pressing enter...')

while 1:
    try:
        num_dice = int(input('> Enter the number of dice you would like to cast! (max 10):'))
        if num_dice not in range(0, 11):
            print('> Please enter a value between 1 and 10! ')
            continue
        break
    except ValueError:
        print('> Non-numerical characters detected. Try again!')

while 1:
    if cast_again not in ('r', 's', 'e'):
        print('> Ups! Available options R(new cast), S(statistics) and E(exit).')
        cast_again = atLeastALetterInput(menu_options)
        continue
    if cast_again == 'r':
        next_cast = casts + 1
        print('> Here comes cast number {}'.format(next_cast))
        casts += 1
        cast_results_to_stats = rollDice(num_dice)
        statistics[casts] = cast_results_to_stats
        print('> Here is your result: {}'.format(cast_results_to_stats))
        cast_again = atLeastALetterInput(menu_options)
    elif cast_again == 's':
        for key in statistics:
            print('> *** Cast {} resulted in {}'.format(key, statistics[key]))
        cast_again = atLeastALetterInput(menu_options)
    elif cast_again == 'e':
        print('> The game finished after {} casts.'.format(casts))
        break

print('> Good bye! ')
input()
