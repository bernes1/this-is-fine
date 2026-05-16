import network
import socket
import secrets
from machine import Pin
from utime import sleep


pin = Pin(10, Pin.OUT)

def activate():
    pin.off() 
    sleep(1)
    pin.on()
    sleep(0.1)
    pin.off()

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    while not wlan.isconnected():
        sleep(0.5)
    print("IP:", wlan.ifconfig()[0])

def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", 5005))
    while True:
        data, _ = s.recvfrom(64)
        if data == b"activate":
            print("recived")
            activate()

connect_wifi()
serve()