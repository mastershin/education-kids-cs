"""
Prints a matrix of random characters, similar to The Matrix's style.
"""
import random
import time

# Define the characters used, similar to The Matrix's style
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'

# Adjust width, height, and density as per your preference
width = 80
height = 100
density = 0.05

# Create an output for each column
for row in range(height):
    output = ''
    for i in range(width):
        output += random.choice(chars)

    print(output)
    time.sleep(0.1)
