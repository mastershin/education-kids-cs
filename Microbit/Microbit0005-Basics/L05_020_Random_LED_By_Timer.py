# Title: Random LEDs using interval function
# Description: Button A clears LEDs, Button B Lights up LEDs randomly continuously using interval function
# Lesson Code: Microbit_05_020
# Lesson Name: Random LEDs By Timer
# Source Code Name: L05_020_Random_LED_By_Timer.py
# Environment: makecode.microbit.org
# Project Link: https://makecode.microbit.org/S74364-52080-62512-62948
#
# Source Code: https://github.com/mastershin/learn-coding-101/tree/main/Microbit
#
# (C) 2024. mastershinAI.com - MIT License.

mode = 0

def on_button_pressed_a():
    global mode
    mode = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mode
    mode = 1
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
                
def on_every_interval():
    global mode
    if mode > 0:
        update_display()

# 1000 == 1000 ms (1 sec), 2000 == 2000 ms (2 seconds)
loops.every_interval(100, on_every_interval)