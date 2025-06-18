from homeassistant.components.switch import SwitchEntity
from .gpio_controller import GPIOController
import RPi.GPIO as GPIO

controller = GPIOController()

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    switches = []
    for pin in config.get("pins", []):
        controller.setup_pin(pin, GPIO.OUT, initial=GPIO.LOW)
        switches.append(GPIOSwitch(pin))
    async_add_entities(switches)

class GPIOSwitch(SwitchEntity):
    def __init__(self, pin):
        self._pin = pin
        self._attr_name = f"GPIO Switch {pin}"
        self._state = False

    @property
    def is_on(self):
        return controller.read_pin(self._pin) == GPIO.HIGH

    def turn_on(self, **kwargs):
        controller.write_pin(self._pin, GPIO.HIGH)

    def turn_off(self, **kwargs):
        controller.write_pin(self._pin, GPIO.LOW)