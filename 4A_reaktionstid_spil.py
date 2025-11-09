from neopixel import Neopixel
from machine import Pin
import time, random
#

# Setup
button1 = Pin(20, Pin.IN, Pin.PULL_UP)  # Spiller 1
button2 = Pin(21, Pin.IN, Pin.PULL_UP)  # Spiller 2
pixels = Neopixel(5, 0, 28, "RGB")

def set_color(color):
    for i in range(5):
        pixels.set_pixel(i, color)
    pixels.show()

while True:
    print("\nKlar til duel!")
    set_color((255, 0, 0))  # Rød = vent
    time.sleep(random.uniform(2, 5))  # Tilfældig pause

    set_color((0, 255, 0))  # Grøn = tryk!
    start = time.ticks_ms()

    winner = None

    while not winner:
        if not button1.value():
            winner = "Spiller 1"
        elif not button2.value():
            winner = "Spiller 2"

    reaction = time.ticks_diff(time.ticks_ms(), start)
    print(f"{winner} vandt! Reaktionstid: {reaction} ms")

    # Vinderen får farve
    if winner == "Spiller 1":
        set_color((0, 0, 255))  # Blå
    else:
        set_color((255, 0, 255))  # Magenta

    time.sleep(3)
