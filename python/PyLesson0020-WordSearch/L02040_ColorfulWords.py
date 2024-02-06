import sys
import random
from colorama import Fore, Back, Style

print(sys.argv)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    print('Please provide at least two arguments.')
    sys.exit()

colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.WHITE
]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for row in range(height):
    for col in range(width):
        letter = random.choice(alphabet)
        color = random.choice(colors)
        print(color + letter + ' ', end='')

        # reset color
        print(Style.RESET_ALL, end='')

    print()
