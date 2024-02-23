"""
Shows how to use command line arguments in Python.
"""
import sys

print(sys.argv)
if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    print('Please provide at least two arguments.')
    sys.exit()

print(f'Thank you.  Width: {width} and height: {height}.')
