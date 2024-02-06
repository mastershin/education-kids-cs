import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Slowly Blinking Stars"
STAR_COUNT = 500
MAX_RADIUS = 3

MIN_BLINK_INTERVAL = 30  # Minimum number of updates between blinks
MAX_BLINK_INTERVAL = 120  # Maximum number of updates between blinks

MIN_BRIGHTNESS = 50
MAX_BRIGHTNESS = 255


class Star:

    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = random.random() * MAX_RADIUS
        self.color = arcade.color.WHITE
        self.blink_interval = random.randint(MIN_BLINK_INTERVAL,
                                             MAX_BLINK_INTERVAL)
        self.blink_counter = 0
        self.brightness = random.randint(MIN_BRIGHTNESS, MAX_BRIGHTNESS)

    def update(self):

        self.brightness += random.randint(-50, 50)
        if self.brightness > MAX_BRIGHTNESS:
            self.brightness = MAX_BRIGHTNESS
        elif self.brightness < MIN_BRIGHTNESS:
            self.brightness = MIN_BRIGHTNESS

    def draw(self):
        red, green, blue = arcade.color.WHITE
        red *= self.brightness / 255
        green *= self.brightness / 255
        blue *= self.brightness / 255

        color = (red, green, blue)

        arcade.draw_circle_filled(self.x, self.y, self.radius, color)


class MyApp(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.star_list = [Star() for _ in range(STAR_COUNT)]

    def on_draw(self):
        arcade.start_render()
        for star in self.star_list:
            star.draw()

    def on_update(self, delta_time):
        for star in self.star_list:
            star.update()


def main():
    window = MyApp()
    arcade.run()


if __name__ == "__main__":
    main()
