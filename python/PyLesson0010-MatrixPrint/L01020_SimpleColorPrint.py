"""
Print a matrix of random characters with random colors using Colorama library.
"""
import os
import random
import time
from colorama import Fore, Back, Style

# Terminal size for display
# width, height = os.get_terminal_size()

# List of available text colors in Colorama
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN]
# colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

for i in range(100):
    ch = ''
    for k in range(80):
        # Randomly choose between any characters (Be creative)
        # ch += random.choice('*#@+- ')

        color = random.choice(colors)
        ch += color + random.choice('1234567890       ')

        # reset the color
        ch += Style.RESET_ALL

    # Print the current line
    print(ch)

    # Pause a bit (0.1 means 0.1 seconds) before the next iteration
    time.sleep(0.1)
