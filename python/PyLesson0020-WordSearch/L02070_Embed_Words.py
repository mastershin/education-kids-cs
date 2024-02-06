import sys
import random
from colorama import Fore, Back, Style
import numpy as np

print(sys.argv)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    print('Please provide at least two arguments.')
    sys.exit()

# Define your words (replace with your actual words)
words = [
    "apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry",
    "watermelon"
]

colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.WHITE
]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

array = np.empty((height, width), dtype='str')

for row in range(height):
    for col in range(width):
        array[row][col] = '-'
        # array[row][col] = random.choice(alphabet)

for word in words:
    col = random.randint(0, width - len(word))
    row = random.randint(0, height - 1)

    for i, char in enumerate(word):
        print(row, col + i, i, char)
        array[row, col + i] = char

print('prints numpy array (without comma and brackets)')
for row in array:
    print(' '.join(row))

# Challenge:
# The words overlap each other, how can you fix this?
