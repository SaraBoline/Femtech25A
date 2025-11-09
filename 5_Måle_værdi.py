from machine import ADC, Pin
import time

pulse_pin = ADC(Pin(27))

while True:
    val = pulse_pin.read_u16()
    print(val)
    time.sleep(0.05)
    
