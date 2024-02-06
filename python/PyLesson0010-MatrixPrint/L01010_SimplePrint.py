"""
Prints a simple matrix of characters to the console.
"""
import random
import time

# Loop 100 times to create 200 lines
for i in range(100):
    ch = ""
    # Add additional random characters to the line
    for k in range(80):
        # Randomly choose between any characters (Be creative)
        # ch += random.choice('*#@+- ')
        ch += random.choice('1234567890')

    # Print the current line
    print(ch)

    # Pause a bit (0.1 means 0.1 seconds) before the next iteration
    time.sleep(0.1)
