from microbit import *
import time

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

distance = 0.5      # distance in meters between sensors
sensor_start = pin0.read_analog()
sensor_end = pin2.read_analog()

# start sequence
display.show("3 2 1")
display.clear()
sleep(400)
display.show(Image.SQUARE)

# wait for first sensor to activate, then note time
while sensor_start > 100:
    sensor_start = pin0.read_analog()
start = time.ticks_ms()
display.clear()

# wait for second sensor to activate, then note time
while sensor_end > 100:
    sensor_end = pin2.read_analog()
end = time.ticks_ms()

# calculate time taken in seconds & speed over given distance
time_taken = (end - start) / 1000
speed = distance / time_taken

# reset button presses to zero
button_a.was_pressed()
button_b.was_pressed()

# until any button pressed, display the time taken or the speed
while button_a.was_pressed() is False and button_b.was_pressed() is False:
    display.scroll('time = ' + str(time_taken) + '   ')
    # display.scroll('speed = ' + str(speed) + '   ')

reset()
