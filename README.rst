Presentation Timer
==================

This repository includes MicroPython code for a presentation timer based on a 50-light string of WS2811 LEDs controlled by an ESP32 or ESP8266. I wrote this to help students in my classes avoid going beyond the alotted time when giving presentations. 

timer.py controls the behavior of the leds, which light up at a rate that depends on a user-specified presentation time. Lights slowly light up until the 
entire string is lighted when the presentation is supposed to end.  Lights are initially green but turn yellow when one minute is left and red when time is up.  They begin to flash 30 seconds past the presentation time.

serverLEDtime.py serves a simple web page that asks a user for the presentation time and then calls the timer.py script with this time.

boot.py sets the ESP into AP mode with SSID "Presentation" and password "password". A user who has logged into the AP can access the web interface by navigating to the ESP's IP address (192.168.4.1 worked for me--but try 192.168.1.1 as well) using a browser. This should be possible from most cell phones, allowing the user to control the light strip remotely.

Wiring
------
The data pin for the WS2811 should be wired to Pin 4. Because 50 neopixels may overload the output from the EPS, power should be provided directly to the neopixels and should not be provided from ESP32/8266.
