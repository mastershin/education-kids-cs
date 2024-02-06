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

print('prints numpy array object (contains comma and brackets)')
print(array)

print('prints each row of numpy array')
for row in array:
    print(row)

print('prints numpy array (without comma and brackets)')
for row in array:
    print(' '.join(row))
