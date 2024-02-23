# Bomb Defuse with PASSWORD
# Press A or B to start the tick
# Once tick starts, guess the correct password (combination of a and b button)

# Title: Bomb Defuse with PASSWORD
# Description: Press A or B to start the tick, guess the password to stop the bomb!
# Lesson Code: L10_050_BombDefuseWithPassword
# Lesson Name: Bomb Defuse with PASSWORD
# Source Code Name: L10_050_BombDefuseWithPassword
# Environment: makecode.microbit.org
# Project Link: https://makecode.microbit.org/S69741-70280-38046-76463
#
# Source Code: https://github.com/mastershin/learn-coding-101/tree/main/Microbit
#
# (C) 2024. mastershinAI.com - MIT License.

state = 0
timer_sec = 0
PASSWORD = "aabbab"
MAX_BOMB_COUNTDOWN = 20

def input_key(key: any):
    global timer_sec, state
    if timer_sec == 0:
        # set timer countdown
        timer_sec = MAX_BOMB_COUNTDOWN + 1
    elif key == PASSWORD[state]:
        # one character matched. move to next state.
        state += 1
        if state == len(PASSWORD):
            # all password matched. bomb defused!
            state = 0
            timer_sec = 0
            basic.show_icon(IconNames.HAPPY)            
    else:
        state = 0

def on_a():
    input_key('a')
def on_b():
    input_key('b')
input.on_button_pressed(Button.A, on_a)
input.on_button_pressed(Button.B, on_b)

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
        timer_sec -= 1
        if timer_sec == 0:
            # exploded!
            basic.show_icon(IconNames.SAD)
            music.play_melody("C G C G C G C G C G C", 500)
        else:
            # tick
            music.play_melody("G ", 200)
            update_display()

loops.every_interval(1000, on_every_interval)
