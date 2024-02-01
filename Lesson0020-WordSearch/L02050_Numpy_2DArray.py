import sys
import random
import numpy as np

print(sys.argv)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    print('Please provide at least two arguments.')
    sys.exit()

array = np.empty((height, width), dtype='int')

for row in range(height):
    for col in range(width):
        array[row][col] = 0
        # array[row][col] = row * width + col
        # array[row][col] = random.randint(0, 9)

# prints numpy array (contains comma and brackets)
print(array)
