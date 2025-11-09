from neopixel import Neopixel
from machine import Pin
import time, random

# Setup
button = Pin(20, Pin.IN, Pin.PULL_UP)
pixels = Neopixel(5, 0, 28, "RGB")

def set_color(color):
    for i in range(5):
        pixels.set_pixel(i, color)
    pixels.show()

while True:
    print("\nKlar til næste runde...")
    set_color((255, 0, 0))  # Rød = vent
    time.sleep(random.uniform(2, 5))  # Tilfældigt ventetid

    set_color((0, 255, 0))  # Grøn = tryk nu!
    start = time.ticks_ms()

    # Vent på knaptryk
    while button.value():
        pass
    reaction_time = time.ticks_diff(time.ticks_ms(), start)

    print(f"Reaktionstid: {reaction_time} ms")

    # Vis resultat i farver
    if reaction_time < 250:
        set_color((0, 0, 255))  # Blå = lynhurtig!
    elif reaction_time < 500:
        set_color((255, 255, 0))  # Gul = god
    else:
        set_color((255, 0, 0))  # Rød = langsom

    time.sleep(2)

