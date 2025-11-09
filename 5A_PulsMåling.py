import time
from machine import Pin, ADC

ADC_PIN = 27
LED_PIN = "LED"

adc = ADC(Pin(ADC_PIN))
led = Pin(LED_PIN, Pin.OUT)


threshold = 33200   # ~50% af den fulde opløsning
hyst = 500  		# tilpas efter smag (~1% af den fulde opløsning)
th_hi = threshold + hyst
th_lo = threshold - hyst

# lad lige sensoren starte op
for _ in range(10):
    _ = adc.read_u16()
    time.sleep_ms(5)

while True:
    signal = adc.read_u16()
    print(signal)

    # filtrer "chatter" bort
    if led.value() == 0 and signal > th_hi:
        led.value(1)
    elif led.value() == 1 and signal < th_lo:
        led.value(0)

    time.sleep_ms(20)
