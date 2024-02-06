"""
Prints a Matrix-like text on the console.
"""
import random
import time

# Define the characters used, similar to The Matrix's style
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'

# Adjust width, height, and density as per your preference
width = 80
height = 100
density = 0.1

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

    print(output)
    time.sleep(0.1)
