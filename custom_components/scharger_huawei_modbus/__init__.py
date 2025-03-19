"""Init file for Huawei SCharger Modbus."""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry):
    port = config_entry.options.get("port", 502)
    _LOGGER.debug("Setting up Huawei SCharger Modbus integration on port %s", port)

    register_manager = ModbusRegisterManager()
    hass.data["modbus_register_manager"] = register_manager

    start_modbus_server(register_manager, port=port)

    # Ensure entity platforms (sensor, number) are loaded
    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor", "number"])

    # Register debug logging toggle services
    def enable_debug(call):
        register_manager.set_debug(True)
        _LOGGER.setLevel(logging.DEBUG)

    def disable_debug(call):
        register_manager.set_debug(False)
        _LOGGER.setLevel(logging.INFO)

    hass.services.async_register("scharger_huawei_modbus", "enable_debug", enable_debug)
    hass.services.async_register("scharger_huawei_modbus", "disable_debug", disable_debug)

    return True
