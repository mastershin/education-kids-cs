import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Graphical Stars"
STAR_COUNT = 200
MAX_RADIUS = 3


class Star:

    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = random.random() * MAX_RADIUS
        self.color = arcade.color.WHITE

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        # arcade.set_background_color(arcade.color.DARK_BLUE)
        self.star_list = [Star() for _ in range(STAR_COUNT)]

    def on_draw(self):
        arcade.start_render()
        for star in self.star_list:
            star.draw()


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
