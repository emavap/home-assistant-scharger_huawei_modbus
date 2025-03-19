from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, REGISTER_MAP

async def async_setup_entry(hass, entry, async_add_entities):
    manager = hass.data[DOMAIN]["register_manager"]
    sensors = [HuaweiChargerSensor(register, props, manager) for register, props in REGISTER_MAP.items() if props["type"] == "sensor"]
    async_add_entities(sensors)

class HuaweiChargerSensor(SensorEntity):
    def __init__(self, register, props, manager):
        self._attr_name = props["name"]
        self._attr_native_unit_of_measurement = props.get("unit", "")
        self._register = register
        self._scale = props.get("scale", 1)
        self._manager = manager
        self._attr_unique_id = f"{DOMAIN}_sensor_{register:04X}"

    @property
    def native_value(self):
        return self._manager.get(self._register) * self._scale