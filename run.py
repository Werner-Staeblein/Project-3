import sys, time, random
import hangman_stages
from opening import opening_image, instructions
from colorama import Fore
import capitalcities
from hangman_stages import get_hangman_stage


def typewriter(textentered):
    """
    Creates typewriter effect for text displayed.
    """
    for letter in textentered:
        if letter == '\n':
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
        time.sleep(0.04)
    print()


def select_word():
    """"
    Step 1: selects a random city from the list in capitalcities
    """
    return random.choice(capitalcities.capital_cities)


def testimpporthangman():
    remaining_attempts = 0
    stage = hangman_stages.get_hangman_stage(remaining_attempts)
    print(stage)

testimpporthangman()