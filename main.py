from machine import Pin, Timer
import time

# Initialize the LED and sound sensor pins
led = Pin(25, Pin.OUT)  # On-board LED on Pi Pico W
sound_sensor = Pin(16, Pin.IN)  # GPIO 16 as input for the sound sensor

# Function to blink the LED
def blink_led(timer):
    led.toggle()

# Timer for debouncing the sound detection
debounce_timer = Timer()

# Interrupt handler for sound detection
def on_sound_detected(pin):
    debounce_timer.init(mode=Timer.ONE_SHOT, period=200, callback=blink_led)

# Attach an interrupt to the sound sensor pin
sound_sensor.irq(trigger=Pin.IRQ_RISING, handler=on_sound_detected)

# Main loop
while True:
    time.sleep(1)  # Sleep to reduce CPU usage (optional)
