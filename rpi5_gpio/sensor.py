from homeassistant.components.sensor import SensorEntity
from .gpio_controller import GPIOController
import RPi.GPIO as GPIO

controller = GPIOController()

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    sensors = []
    for pin in config.get("pins", []):
        controller.setup_pin(pin, GPIO.IN)
        sensors.append(GPIOInputSensor(pin))
    async_add_entities(sensors)

class GPIOInputSensor(SensorEntity):
    def __init__(self, pin):
        self._pin = pin
        self._attr_name = f"GPIO Sensor {pin}"

    @property
    def state(self):
        return controller.read_pin(self._pin)