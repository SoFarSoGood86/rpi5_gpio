import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pins = {}

    def setup_pin(self, pin, mode, initial=None):
        if pin not in self.pins:
            GPIO.setup(pin, mode, initial=initial)
            self.pins[pin] = mode

    def write_pin(self, pin, value):
        GPIO.output(pin, value)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def cleanup(self):
        GPIO.cleanup()