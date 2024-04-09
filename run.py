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


def start_game(secret_city, username): 
    """
    Start the hangman game.
    """
    guessed_correctly = False    
    while True:
        remaining_attempts = 6
        guessed_letters = ""
        unique_secret_letters = secret_city
        print(secret_city)




def main():
    opening_image()
    print(Fore.RESET)

    typewriter("Welcome to capital cities guessing")
    typewriter("We will put your geography knowledge to the test")
    time.sleep(1)

    while True:
        print(Fore.GREEN)
        username = input("Please provide your name \n")

        if username == "":
            typewriter("Looks like you want to play anonymously")
            typewriter("Ok, we will call you Geo, the champ of capital cities knowledge, aka G3C")
            username = "G3C"
            break
        elif not username.isalpha():
            print(Fore.RED)
            typewriter("Please enter a name using only alphabetic characters.")
        else:
            print(Fore.GREEN)
            typewriter(f"Let's get started {username.upper().strip()}")
            time.sleep(0.5)
            instructions()
            time.sleep(0.5)
            break

    while True:
        secret_city = select_word()
        start_game(secret_city, username)


main()
