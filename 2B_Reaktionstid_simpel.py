import machine
import utime
import urandom

led = machine.Pin(1, machine.Pin.OUT)
button1 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)


def button_handler(pin):
    button1.irq(handler=None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    
    
    print("Your reaction time was " + str(timer_reaction)+ " milliseconds!" )

led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)
timer_start = utime.ticks_ms()
button1.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
