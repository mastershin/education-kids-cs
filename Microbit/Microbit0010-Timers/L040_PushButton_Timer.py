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
    for i in range(5):
        for j in range(5):
            if timer > i * 5 + j:
                led.plot(j, i)
            else:
                led.unplot(j, i)

def on_every_interval():
    global timer
    if timer > 0:
        # Update timer every time_value msec
        timer += 0 - 1
        update_display()
        if timer <= 0:
            basic.show_icon(IconNames.HEART)
            music.play_melody("C5 - C5 - C5 - - - ", 120)
    else:
        for k in range(5):
            led.unplot(k, 4)
loops.every_interval(1000, on_every_interval)



