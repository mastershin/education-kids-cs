# Title: LED Timer
# Description: Button A clears LEDs, Button B Lights up all LEDs and decreases by 1 every second
# Lesson Code: Microbit_L10_010_LED_Timer
# Lesson Name: LED Timer
# Source Code Name: L10_010_LED_Timer.py
# Environment: makecode.microbit.org
# Project Link: https://makecode.microbit.org/S30409-52244-96520-14238
#
# Source Code: https://github.com/mastershin/learn-coding-101/tree/main/Microbit
#
# (C) 2024. mastershinAI.com - MIT License.

timer_sec = 0

def on_button_pressed_a():
    global timer_sec
    timer_sec = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global timer_sec
    timer_sec = 25
    update_display()
input.on_button_pressed(Button.B, on_button_pressed_b)

def update_display():
    for i in range(5):
        for j in range(5):
            if timer_sec > i * 5 + j:
                led.plot(j, i)
            else:
                led.unplot(j, i)

def on_every_interval():
    global timer_sec
    if timer_sec > 0:
        timer_sec += 0 - 1
        update_display()
        if timer_sec <= 0:
            music.play_melody("E B C5 A B G A F", 200)

# 1000 == 1000 ms (1 sec), 2000 == 2000 ms (2 seconds)
loops.every_interval(1000, on_every_interval)

