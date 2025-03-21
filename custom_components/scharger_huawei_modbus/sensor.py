from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, REGISTER_MAP

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data[DOMAIN]["register_manager"]
    sensors = [
        HuaweiChargerSensorEntity(addr, reg, register_manager)
        for addr, reg in REGISTER_MAP.items()
        if reg.get("type") == "sensor"
    ]
    async_add_entities(sensors, update_before_add=True)

class HuaweiChargerSensorEntity(SensorEntity):
    def __init__(self, addr, reg, register_manager):
        self._attr_name = reg.get("name")
        self._attr_unique_id = f"scharger_sensor_{addr:04X}"
        self._attr_native_unit_of_measurement = reg.get("unit")
        self._scale = reg.get("scale", 1)
        self._addr = addr
        self._register_manager = register_manager
        self._attr_should_poll = True
        self._attr_native_value = self._register_manager.get(self._addr) * self._scale

    async def async_update(self):
        raw = self._register_manager.get(self._addr)
        self._attr_native_value = raw * self._scale

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "huawei_scharger")},
            "name": "Huawei SCharger",
            "manufacturer": "Huawei",
            "model": "SCharger"
        }
