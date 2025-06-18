from homeassistant.core import HomeAssistant

DOMAIN = "rpi5_gpio"

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass, entry):
    return True