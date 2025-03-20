from homeassistant.components.number import NumberEntity
from .const import DOMAIN, REGISTER_MAP

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data[DOMAIN]["register_manager"]
    numbers = [
        HuaweiChargerNumberEntity(addr, reg, register_manager)
        for addr, reg in REGISTER_MAP.items()
        if reg.get("type") == "number"
    ]
    async_add_entities(numbers)

class HuaweiChargerNumberEntity(NumberEntity):
    def __init__(self, addr, reg, register_manager):
        self._attr_name = reg.get("name")
        self._attr_unique_id = f"scharger_number_{addr:04X}"
        self._attr_native_unit_of_measurement = reg.get("unit")
        self._scale = reg.get("scale", 1)
        self._addr = addr
        self._register_manager = register_manager
        self._attr_native_min_value = reg.get("min")
        self._attr_native_max_value = reg.get("max")
        self._attr_native_step = self._scale
        self._attr_should_poll = True
        self._attr_native_value = self._register_manager.get(self._addr) * self._scale

    async def async_set_native_value(self, value: float):
        raw = int(value / self._scale)
        self._register_manager.set(self._addr, raw)
        self._attr_native_value = value
        self.async_write_ha_state()

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "huawei_scharger")},
            "name": "Huawei SCharger",
            "manufacturer": "Huawei",
            "model": "SCharger"
        }
