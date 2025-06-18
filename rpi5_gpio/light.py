from homeassistant.components.light import LightEntity, ATTR_BRIGHTNESS
from .gpio_controller import GPIOController
import RPi.GPIO as GPIO

controller = GPIOController()

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    lights = []
    for pin in config.get("pins", []):
        controller.setup_pin(pin, GPIO.OUT)
        lights.append(GPIOLight(pin))
    async_add_entities(lights)

class GPIOLight(LightEntity):
    def __init__(self, pin):
        self._pin = pin
        self._attr_name = f"GPIO Light {pin}"
        self._is_on = False

    @property
    def is_on(self):
        return controller.read_pin(self._pin) == GPIO.HIGH

    def turn_on(self, **kwargs):
        controller.write_pin(self._pin, GPIO.HIGH)
        self._is_on = True

    def turn_off(self, **kwargs):
        controller.write_pin(self._pin, GPIO.LOW)
        self._is_on = False