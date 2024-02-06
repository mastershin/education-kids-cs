"""
Prints a star moving from left to right and back.
"""
import time

width = 20
position = 0
direction = 1  # 1 for right, -1 for left

while True:
    ch = ' ' * position
    ch += '*'

    print(ch)

    position += direction

    if position == width - 1 or position == 0:
        direction *= -1

    time.sleep(0.05)
