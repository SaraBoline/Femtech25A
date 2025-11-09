from neopixel import Neopixel
from machine import Pin
import time

# --- Setup ---
num_pixels = 5                         # Antal pixels i strippen
pixels = Neopixel(num_pixels, 0, 28, "RGB")  # NeoPixel på pin 28

# --- Hjælpefunktion ---
def set_color(color):
    """Sætter alle pixels til samme farve."""
    for i in range(num_pixels):
        pixels.set_pixel(i, color)
    pixels.show()

# --- Funktion til at fade op og ned ---
def fade(color, steps=50, delay=0.05, direction="up"):
    """Fader farven op eller ned over 'steps' trin."""
    for i in range(steps + 1):
        if direction == "up":
            factor = i / steps
        else:
            factor = 1 - (i / steps)
        r = int(color[0] * factor)
        g = int(color[1] * factor)
        b = int(color[2] * factor)
        set_color((r, g, b))
        time.sleep(delay)

# --- Hovedprogram ---
print("Starter Box Breathing øvelse...")

while True:
    # 1️⃣ Træk vejret ind - lys fader op (blå)
    print("Træk vejret ind...")
    fade((0, 0, 255), steps=50, delay=0.08, direction="up")

    # 2️⃣ Hold vejret - lyset forbliver tændt
    print("Hold vejret...")
    set_color((0, 0, 255))
    time.sleep(4)

    # 3️⃣ Pust ud - lys fader langsomt ud
    print("Pust ud...")
    fade((0, 0, 255), steps=50, delay=0.08, direction="down")

    # 4️⃣ Hold igen - lys er slukket
    print("Hold igen...")
    set_color((0, 0, 0))
    time.sleep(4)
