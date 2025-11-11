from machine import Pin, ADC
from neopixel import Neopixel
import time

# --- Hardware setup ---
ADC_PIN = 27
LED_PIN = "LED"

adc = ADC(Pin(ADC_PIN))
led = Pin(LED_PIN, Pin.OUT)

# --- NeoPixel setup ---
num_pixels = 5           # antal LEDs
pixels = Neopixel(num_pixels, 0, 28, "RGB")  # GPIO28 til NeoPixel data
def set_color(color):
    """Sæt alle NeoPixels til en bestemt farve"""
    for i in range(num_pixels):
        pixels.set_pixel(i, color)
    pixels.show()

# --- Farver for forskellige pulsniveauer ---
# (R, G, B)
colors = {
    "low": (0, 0, 255),        # Blå = lav puls
    "normal": (0, 255, 0),     # Grøn = normal
    "elevated": (255, 255, 0), # Gul = let forhøjet
    "high": (255, 165, 0),     # Orange = høj
    "very_high": (255, 0, 0)   # Rød = meget høj
}

# --- Indstillinger til måling ---
threshold = 33200   # Justér efter sensor
hyst = 500          # Hysterese (~1%)
th_hi = threshold + hyst
th_lo = threshold - hyst

# Startopvarmning
for _ in range(10):
    _ = adc.read_u16()
    time.sleep_ms(5)

beats = []            # Tidsstempler for slag
last_state = 0        # LED tilstand
start_time = time.ticks_ms()

# --- Funktion til farveskift baseret på BPM ---
def update_color(bpm):
    """Opdater NeoPixel farve baseret på puls"""
    if bpm < 60:
        set_color(colors["low"])
    elif 60 <= bpm <= 70:
        set_color(colors["normal"])
    elif 71 <= bpm <= 80:
        set_color(colors["elevated"])
    elif 81 <= bpm <= 100:
        set_color(colors["high"])
    else:
        set_color(colors["very_high"])

# --- Main loop ---
while True:
    signal = adc.read_u16()

    # Registrer pulsslag
    if led.value() == 0 and signal > th_hi:
        led.value(1)
    elif led.value() == 1 and signal < th_lo:
        led.value(0)

    state = led.value()

    # Registrer nyt slag (rising edge)
    if state == 1 and last_state == 0:
        now = time.ticks_ms()
        beats.append(now)

        # behold kun de sidste 15 sekunder
        beats = [b for b in beats if time.ticks_diff(now, b) < 15000]

        # Beregn BPM
        if len(beats) > 1:
            intervals = [time.ticks_diff(beats[i], beats[i-1]) for i in range(1, len(beats))]
            avg_interval_ms = sum(intervals) / len(intervals)
            bpm = 60000 / avg_interval_ms
            print("BPM:", int(bpm))

            # Opdater LED-farve efter puls
            update_color(bpm)

    last_state = state
    time.sleep_ms(20)
