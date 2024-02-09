# Title: LED Timer on Demand
# Description: Button A clears LEDs, Button B Lights up each LED and decreases by 1 every second
# Lesson Code: Microbit_L10_040_On_Demand_Timer
# Lesson Name: LED Timer
# Source Code Name: L10_040_OnDemandTimer
# Environment: makecode.microbit.org
# Project Link: https://makecode.microbit.org/S39561-60527-62381-60006
#
# Source Code: https://github.com/mastershin/learn-coding-101/tree/main/Microbit
#
# (C) 2024. mastershinAI.com - MIT License.

timer = 0

def on_button_pressed_a():
    global timer
    timer = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global timer
    if timer < 25:
        timer += 1
        update_display()
input.on_button_pressed(Button.B, on_button_pressed_b)

def update_display():
    for y in range(5):
        for x in range(5):
            if timer > y * 5 + x:
                led.plot(x, y)
            else:
                led.unplot(x, y)

def on_every_interval():
    global timer
    if timer > 0:
        # Update timer every time_value msec
        timer += 0 - 1
        update_display()
        if timer <= 0:
            basic.show_icon(IconNames.HEART)
            music.play_melody("C5 - C5 - C5 - - - ", 120)

loops.every_interval(1000, on_every_interval)
