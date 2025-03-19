"""Init file for Huawei SCharger Modbus."""
from .modbus_server import start_modbus_server, RegisterManager


async def async_setup_entry(hass, config_entry):
    port = config_entry.data.get("port", 8502)
    if config_entry.options:
        port = config_entry.options.get("port", port)

    register_manager = RegisterManager(hass)
    start_modbus_server(register_manager, port=port)
    return True
