"""Init file for Huawei SCharger Modbus."""
from .modbus_server import start_modbus_server, ModbusRegisterManager


async def async_setup_entry(hass, config_entry):
    port = config_entry.options.get("port", 502)

    register_manager = ModbusRegisterManager()
    start_modbus_server(register_manager, port=port)
    return True
