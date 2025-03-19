from homeassistant.components.number import NumberEntity
from homeassistant.helpers.restore_state import RestoreNumber
from .const import DOMAIN, REGISTER_MAP

async def async_setup_entry(hass, entry, async_add_entities):
    manager = hass.data[DOMAIN]["register_manager"]
    numbers = [HuaweiChargerNumber(register, props, manager) for register, props in REGISTER_MAP.items() if props["type"] == "number"]
    async_add_entities(numbers)

class HuaweiChargerNumber(RestoreNumber):
    def __init__(self, register, props, manager):
        self._attr_name = props["name"]
        self._attr_native_unit_of_measurement = props.get("unit", "")
        self._attr_native_min_value = props.get("min", 0)
        self._attr_native_max_value = props.get("max", 100)
        self._register = register
        self._scale = props.get("scale", 1)
        self._manager = manager
        self._attr_unique_id = f"{DOMAIN}_number_{register:04X}"
        self._value = 0

    @property
    def native_value(self):
        return self._manager.get(self._register) * self._scale

    async def async_set_native_value(self, value):
        self._value = value
        self._manager.set(self._register, int(value / self._scale))
        self.async_write_ha_state()