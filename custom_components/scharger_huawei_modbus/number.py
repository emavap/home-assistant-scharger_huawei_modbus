from homeassistant.components.number import NumberEntity
from .const import REGISTER_MAP
from .modbus_server import ModbusRegisterManager

async def async_setup_entry(hass, config_entry, async_add_entities):
    register_manager = hass.data.get("modbus_register_manager")
    numbers = []
    for addr, reg in REGISTER_MAP.items():
        if reg.get("type") != "number":
            continue
        numbers.append(HuaweiChargerNumberEntity(addr, reg, register_manager))
    async_add_entities(numbers)

class HuaweiChargerNumberEntity(NumberEntity):
    def __init__(self, addr, reg, register_manager: ModbusRegisterManager):
        self._attr_name = reg.get("name")
        self._attr_unique_id = f"scharger_number_{addr:04X}"
        self._attr_native_unit_of_measurement = reg.get("unit")
        self._scale = reg.get("scale", 1.0)
        self._addr = addr
        self._register_manager = register_manager
        self._attr_native_min_value = reg.get("min", 0)
        self._attr_native_max_value = reg.get("max", 100)
        self._attr_native_step = self._scale
        self._attr_native_value = self._register_manager.get(self._addr) * self._scale

    async def async_set_native_value(self, value: float):
        self._attr_native_value = value
        raw_value = int(value / self._scale)
        self._register_manager.set(self._addr, raw_value)
