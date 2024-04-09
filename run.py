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

def get_unique_letters(word):
    """
    Step 2: Convert the secret word into a set to remove duplicates.
    """
    return "".join(set(word))

def is_guess_in_secret_word(guess, secret_city):
    """
    step 3: Check if the guessed letter is in the secret city.
    """
    guess = guess.upper()
    secret_city = secret_city.upper()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Only single letters are allowed")
        return False
    elif guess.upper() in secret_city:
        return True
    else:
        return False


def start_game(secret_city, username): 
    """
    Start the hangman game.
    """
    guessed_correctly = False    
   
    while True:
        remaining_attempts = 6
        guessed_letters = ""
        unique_secret_letters = get_unique_letters(secret_city)

        while remaining_attempts > 0 and len(guessed_letters) < len(unique_secret_letters):
            guess = input("Guess a letter of the secret city: ").upper()
            guess_in_secret_word = is_guess_in_secret_word(guess, secret_city)
            print(guess_in_secret_word)
           


def main():
    opening_image()
    
    print()
    print()
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
