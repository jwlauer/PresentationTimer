"""
Web interface for a presentation timer.

Copyright 2019 Wes Lauer
This code is released under the MIT license

Requires timer.py

Creates a simple website that allows user to enter the time
required for a presentation over a web page served by an
ESP32 or ESP8266. The program calls a separate script that
controls uses this time to control a presentation timer.
Can be used over a typical cell phone if the user joins the
ESP32/8266 network (using SSID/Password set up in boot.py),
then navigates using a browser app to 192.168.4.1.

"""

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>WS2812 LED Presentation Timer</title> </head>
<h2>LEDs Turn Yellow One Minute Before Time, Red at Time</h2></center>
<h3>(ESP32)</h3></center>
    <form action="/test" method="get">
        Enter Minutes: <input type="text" name="minutes"><br />
        <input type="submit" value="Submit">
    </form>
</html>
"""

#Setup PINS
import machine
import socket
import re
import utime
import timer

LED_BLUE = machine.Pin(2, machine.Pin.OUT)

#Setup Socket WebServer
#addr = socket.getaddrinfo('192.168.4.1', 80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
#s.bind(addr)
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    output = re.search("minutes=(.+?) HTTP", request)
    if output:
        out_min = output.group(1)
        print(out_min)
        LED_BLUE.value(0)
        utime.sleep(float(out_min))
        LED_BLUE.value(1)
        timer.t(float(out_min))
    response = html
    conn.send(response)
    conn.close()
