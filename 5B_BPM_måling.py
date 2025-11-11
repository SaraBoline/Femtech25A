import time
from machine import Pin, ADC

ADC_PIN = 27
LED_PIN = "LED"

adc = ADC(Pin(ADC_PIN))
led = Pin(LED_PIN, Pin.OUT)

threshold = 33200   # Adjust to your sensor
hyst = 500          # Hysteresis (~1%)
th_hi = threshold + hyst
th_lo = threshold - hyst

# Startup warm-up
for _ in range(10):
    _ = adc.read_u16()
    time.sleep_ms(5)

beats = []            # timestamps of beats
last_state = 0        # LED state
start_time = time.ticks_ms()

while True:
    signal = adc.read_u16()

    # --- pulse detection with hysteresis ---
    if led.value() == 0 and signal > th_hi:
        led.value(1)
    elif led.value() == 1 and signal < th_lo:
        led.value(0)

    state = led.value()

    # detect rising edge = new beat
    if state == 1 and last_state == 0:
        now = time.ticks_ms()
        beats.append(now)

        # keep only last 15 seconds of beats
        beats = [b for b in beats if time.ticks_diff(now, b) < 15000]

        # compute BPM if enough beats
        if len(beats) > 1:
            intervals = [time.ticks_diff(beats[i], beats[i-1]) for i in range(1, len(beats))]
            avg_interval_ms = sum(intervals) / len(intervals)
            bpm = 60000 / avg_interval_ms
            print("BPM:", int(bpm))

    last_state = state
    time.sleep_ms(20)  # same sampling rate as your original code
