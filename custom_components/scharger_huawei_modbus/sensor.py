from homeassistant.components.sensor import SensorEntity
from datetime import timedelta
import logging
from .const import DOMAIN, REGISTER_MAP

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data[DOMAIN]["register_manager"]
    sensors = [
        HuaweiChargerSensorEntity(addr, reg, register_manager)
        for addr, reg in REGISTER_MAP.items()
        if reg.get("type") == "sensor"
    ]
    sensors.append(HuaweiChargerDebugSensor(register_manager))
    async_add_entities(sensors)

class HuaweiChargerSensorEntity(SensorEntity):
    def __init__(self, addr, reg, register_manager):
        self._attr_name = reg.get("name")
        self._attr_unique_id = f"scharger_sensor_{addr:04X}"
        self._attr_native_unit_of_measurement = reg.get("unit")
        self._scale = reg.get("scale", 1.0)
        self._addr = addr
        self._register_manager = register_manager
        self._attr_should_poll = True

    async def async_update(self):
        raw_val = self._register_manager.get(self._addr)
        self._attr_native_value = raw_val * self._scale

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "huawei_scharger")},
            "name": "Huawei SCharger",
            "manufacturer": "Huawei",
            "model": "SCharger",
        }

class HuaweiChargerDebugSensor(SensorEntity):
    def __init__(self, register_manager):
        self._attr_name = "Huawei SCharger Debug Registers"
        self._attr_unique_id = "scharger_debug_raw"
        self._register_manager = register_manager
        self._attr_should_poll = True

    async def async_update(self):
        result = {}
        for addr in range(0x1000, 0x1020):
            result[f"0x{addr:04X}"] = self._register_manager.get(addr)
        self._attr_native_value = str(result)

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "huawei_scharger")},
            "name": "Huawei SCharger",
            "manufacturer": "Huawei",
            "model": "SCharger",
        }

    @property
    def extra_state_attributes(self):
        return {
            f"0x{addr:04X}": self._register_manager.get(addr)
            for addr in range(0x1000, 0x1020)
        }
