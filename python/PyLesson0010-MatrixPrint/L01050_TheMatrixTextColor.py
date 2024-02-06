import random
import time
from colorama import Fore, Back, Style

# Define the characters used, similar to The Matrix's style
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'

colors = [Fore.GREEN, Fore.LIGHTGREEN_EX]

# Adjust width, height, and density as per your preference
width = 80
height = 100
density = 0.02

columns = [0] * width

# Create an output for each column
for row in range(height):
    output = ''
    for i in range(width):
        if columns[i] > 0:
            output += random.choice(chars)
            columns[i] -= 1
        else:
            output += ' '
            if random.random() < density:
                columns[i] = random.randint(5, 20)  # Randomize new drop length

    color = random.choice(colors)
    print(color + output + Style.RESET_ALL)
    time.sleep(0.1)
