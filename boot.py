#Sets ESP32/8266 into AP mode and sets SSID/Password when booted

import uos, machine
import gc
import webrepl
webrepl.start()
import network
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True) #make access point mode active
ap_if.config(essid="Presentation", authmode=network.AUTH_WPA_WPA2_PSK,password="password")
gc.collect()
