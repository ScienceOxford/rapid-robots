from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(channel=6)     # change this to a number between 0-82, and make your receiver match!

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N)
        radio.send('forward')
    elif button_a.is_pressed():
        radio.send('left')
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        radio.send('right')
        display.show(Image.ARROW_E)
    else:
        radio.send('stop')
        display.clear()
    sleep(1)
