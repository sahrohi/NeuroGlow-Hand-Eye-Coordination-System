import RPi.GPIO as GPIO
import time
import random

# LED and Button pin configuration
led_pins = [2,3,4,17,27,22,10,9,11]
button_pins = [5,6,13,19,26,21,20,16,12]

GPIO.setmode(GPIO.BCM)

# Setup LEDs
for led in led_pins:
    GPIO.setup(led, GPIO.OUT)

# Setup Buttons
for button in button_pins:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:

        # Random LED selection
        index = random.randint(0,8)

        led = led_pins[index]
        button = button_pins[index]

        GPIO.output(led, GPIO.HIGH)

        start_time = time.time()

        # Wait for button press
        while GPIO.input(button) == GPIO.HIGH:
            pass

        reaction_time = time.time() - start_time

        GPIO.output(led, GPIO.LOW)

        print("LED", index+1, "Reaction Time:", round(reaction_time,3), "seconds")

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()