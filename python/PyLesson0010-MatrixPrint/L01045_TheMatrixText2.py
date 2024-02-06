"""
One column of random characters is printed.
"""
import random
import time

# Define the characters used, similar to The Matrix's style
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'

height = 100

drop_length = 10

# Create an output for each column
for row in range(height):
    output = ''
    if drop_length > 0:
        output += random.choice(chars)
        drop_length -= 1
    else:
        output += ' '
        drop_length = random.randint(0, 20)  # Randomize new drop length

    print(output)
    time.sleep(0.1)
