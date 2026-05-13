from machine import Pin
from utime import sleep


pin = Pin(10, Pin.OUT)

def activate():
    pin.off() 
    sleep(1)
    pin.on()
    sleep(0.1)
    pin.off()


activate()





