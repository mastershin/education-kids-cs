timer_sec = 0
# (C) 2024. mastershin at gmail.com
# https://github.com/mastershin/learn-microbit-101
# Part 1: Basic Timer, 1 second per LEDs. 25 seconds.

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

