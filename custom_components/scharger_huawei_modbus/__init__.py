"""Init file for Huawei SCharger Modbus."""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager

_LOGGER = logging.getLogger(__name__)

DOMAIN = "scharger_huawei_modbus"

async def async_setup_entry(hass, config_entry):
    port = config_entry.options.get("port", 502)
    _LOGGER.debug("Setting up Huawei SCharger Modbus integration on port %s", port)

    register_manager = ModbusRegisterManager()
    hass.data[DOMAIN] = {
        "register_manager": register_manager
    }

    server = start_modbus_server(register_manager, port=port)
    hass.data[DOMAIN]["modbus_server"] = server

    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor", "number"])

    def enable_debug(call):
        register_manager.set_debug(True)
        _LOGGER.setLevel(logging.DEBUG)

    def disable_debug(call):
        register_manager.set_debug(False)
        _LOGGER.setLevel(logging.INFO)

    hass.services.async_register(DOMAIN, "enable_debug", enable_debug)
    hass.services.async_register(DOMAIN, "disable_debug", disable_debug)

    return True

async def async_unload_entry(hass, config_entry):
    _LOGGER.debug("Unloading Huawei SCharger Modbus integration")
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, ["sensor", "number"])
    if unload_ok and DOMAIN in hass.data:
        if "modbus_server" in hass.data[DOMAIN]:
            server = hass.data[DOMAIN]["modbus_server"]
            server.shutdown()
            server.server_close()
            _LOGGER.debug("Modbus TCP server shut down on unload")
        hass.data.pop(DOMAIN)
    return unload_ok
