from colorama import Fore

def opening_image():
    print(Fore.GREEN + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣻⢝⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⢷⡦⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢷⢾⣿⣿⡷⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣷⠱⠇⠈⡮⣹⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣞⠦⣻⠀⠀⢛⡴⢳⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣛⣛⣻⣿⣻⣿⣿⣿⣟⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠓⠓⠓⠓⠓⠛⠚⠚⠚⠚⢆⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣻⡭⢻⣟⣿⣏⣉⣿⣿⡟⢩⣍⢆⠀⠀⠀⠀
⠀⠀⡰⣛⡤⢜⣮⠕⠊⠉⠉⠉⠺⢝⡇⢤⣎⢦⠀⠀⠀
⠀⡴⠻⣀⡨⡞⠁⠀⠀⠀⠀⠀⠀⠀⠹⡇⣀⠝⢣⠀⠀
⣼⣔⣊⣑⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣊⣁⣢⣵⡀""")
    
    print(Fore.RESET)


def instructions():
    print("="*70)
    print("*" * 30 + " HOW TO PLAY THE GAME " + "*" * 30)
    print()
    print("""
    1. This is a traditional hangman game
    2. The goal is to guess well-known capital cities with a maximum of 6 tries         
    3. Guess the right capital city to escape the situation
    """)
    print()
    print("*" * 70)
    print("="*70)
    print("\n")
