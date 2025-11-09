from neopixel import Neopixel
from machine import Pin
import time

# Initialize button with pull-up resistor
button = Pin(20, Pin.IN, Pin.PULL_UP)

# Initialize NeoPixel strip
num_pixels = 5  # Adjust for your setup
pixels = Neopixel(num_pixels, 0, 28, "RGB")  # Ensure correct GRB order

# Define color sequence
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255)   # Magenta
]

color_index = 0  # Start with the first color

def set_color(color):
    """Set all NeoPixels to the given color."""
    for i in range(num_pixels):
        pixels.set_pixel(i, color)
    pixels.show()

# Set initial color
set_color(colors[color_index])

# --- Main loop ---
while True:
    if not button.value():  # Button pressed (LOW)
        print("Button pressed! Skifter farve om 3 sekunder...")
        time.sleep(3)  # ← Her vises forsinkelsen (sleep)
        color_index = (color_index + 1) % len(colors)  # Cycle to the next color
        set_color(colors[color_index])
        time.sleep_ms(500)  # Debounce delay to avoid multiple detections

