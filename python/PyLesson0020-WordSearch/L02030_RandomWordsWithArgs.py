import random
import sys

print(sys.argv)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    print('Please provide at least two arguments.')
    sys.exit()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for row in range(height):
    for col in range(width):
        letter = random.choice(alphabet)
        print(letter + " ", end="")

    print()
