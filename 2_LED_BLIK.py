import machine
from machine import Pin
from time import sleep


button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
led = Pin(1, Pin.OUT)

while True:
    if not button.value():
        led.value(1)
        print('Button pressed!')
        sleep(.2)
        led.value(0)
