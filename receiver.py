from microbit import *
import radio
import neopixel
import random

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(queue=1)
np = neopixel.NeoPixel(pin0, 5)

display.show(Image.ALL_CLOCKS, wait=False, loop=True)

while True:
    message = radio.receive()
    if message is not None:
        print(message)
        for pixel_id in range(0, 5):
            red = random.randint(0, 60)
            green = random.randint(0, 60)
            blue = random.randint(0, 60)
            np[pixel_id] = (red, green, blue)
        np.show()
        sleep(200)
    np.clear()
