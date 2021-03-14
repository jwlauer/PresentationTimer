"""
Presentation timer using string of 50 WS2811 Leds.

Copyright 2019 Wes Lauer
This code is released under the MIT license

Allows color of a string of WS2811 leds to change
as a function of how close one is to the end of a
presentation. Leds slowly light up until all are lit at
specified presentation time.  Color is green up to one
minute before time, then yellow, the red once time is
up. Leds flash when 30 seconds over time.
"""

import machine, utime, neopixel
np = neopixel.NeoPixel(machine.Pin(4), 50)

def clear_pixels(np):
    for i in range(np.n-1):
        np[i] = (0,0,0)
    np.write()
    
def turn_on(np,pixels,color):
    for i in range(pixels-1):
        np[i] = color
    np.write()

def flash_red(np):
    utime.sleep(0.5)
    for i in range(np.n-1):
        np[i] = (0,0,0)
    np.write()
    utime.sleep(0.5)
    for i in range(np.n-1):
        np[i] = (0,40,0)
    np.write()

def t(minutes):
    import machine, utime, neopixel
    np = neopixel.NeoPixel(machine.Pin(4), 50)
    green = (40,0,0)
    red = (0,40,0)
    yellow = (30,30,0)
    starttime = utime.ticks_ms()

    color = green
    clear_pixels(np)
    np[0] = green
    np.write()
    while True:
        now = utime.ticks_ms()
        elapsed = utime.ticks_diff(now,starttime)
        if elapsed > 60*1000*(minutes-1):
            color = yellow
        if elapsed > 60*1000*(minutes):
            color = red
        pixels = min(50*elapsed//(minutes*60*1000),50)
        if elapsed > 60*1000*minutes+30*1000:
            flash_red(np)
        turn_on(np,pixels,color)