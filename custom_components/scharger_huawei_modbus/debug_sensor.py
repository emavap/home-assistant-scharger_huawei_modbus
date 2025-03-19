from homeassistant.components.sensor import SensorEntity
from datetime import timedelta
import logging

from .modbus_server import ModbusRegisterManager
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data[DOMAIN]["register_manager"]
    async_add_entities([HuaweiChargerDebugSensor(register_manager)])

class HuaweiChargerDebugSensor(SensorEntity):
    def __init__(self, register_manager: ModbusRegisterManager):
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
        # Expose all registers as attributes too
        return {
            f"0x{addr:04X}": self._register_manager.get(addr)
            for addr in range(0x1000, 0x1020)
        }
