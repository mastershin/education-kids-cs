"""
Introduction to Classes, creating a Star object, and main class
"""
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Text Stars"
STAR_COUNT = 10
MAX_RADIUS = 3


class Star:

    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = random.random() * MAX_RADIUS
        self.color = "WHITE"

    def draw(self):
        print(self.x, self.y, self.radius, self.color)


class MyStarApp():

    def __init__(self):
        self.star_list = [Star() for _ in range(STAR_COUNT)]

    def on_draw(self):
        for star in self.star_list:
            star.draw()


def main():
    window = MyStarApp()
    window.on_draw()


if __name__ == "__main__":
    main()
