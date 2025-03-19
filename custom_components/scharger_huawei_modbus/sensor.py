from homeassistant.components.sensor import SensorEntity
from .const import REGISTER_MAP
from .modbus_server import ModbusRegisterManager

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data.get("modbus_register_manager")
    sensors = []
    for addr, reg in REGISTER_MAP.items():
        if reg.get("type") != "sensor":
            continue
        sensors.append(HuaweiChargerSensorEntity(addr, reg, register_manager))
    async_add_entities(sensors)

class HuaweiChargerSensorEntity(SensorEntity):
    def __init__(self, addr, reg, register_manager: ModbusRegisterManager):
        self._attr_name = reg.get("name")
        self._attr_unique_id = f"scharger_sensor_{addr:04X}"
        self._attr_native_unit_of_measurement = reg.get("unit")
        self._scale = reg.get("scale", 1.0)
        self._addr = addr
        self._register_manager = register_manager
        self._attr_native_value = 0

    async def async_update(self):
        raw_val = self._register_manager.get(self._addr)
        self._attr_native_value = raw_val * self._scale
