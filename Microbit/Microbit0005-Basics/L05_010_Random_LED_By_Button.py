# Title: Random LEDs using Buttons
# Description: Button A clears LEDs, Button B Lights up LEDs randomly
# Lesson Code: Microbit_05_010
# Lesson Name: Random LEDs By Timer
# Source Code Name: L05_010_Random_LED_By_Button.py
# Environment: makecode.microbit.org
# Project Link: https://makecode.microbit.org/S99041-96930-57950-67962
#
# Source Code: https://github.com/mastershin/learn-coding-101/tree/main/Microbit
#
# (C) 2024. mastershin AI. MIT License.

def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    update_display()
input.on_button_pressed(Button.B, on_button_pressed_b)

def update_display():
    for y in range(5):
        for x in range(5):
            # led.plot takes (column, row) or (x, y)
            if Math.random() > 0.5:
                led.plot(x, y)
            else:
                led.unplot(x, y)
