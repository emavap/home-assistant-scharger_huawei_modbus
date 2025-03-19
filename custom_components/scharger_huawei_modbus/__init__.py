"""Init file for Huawei SCharger Modbus."""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager

_LOGGER = logging.getLogger(__name__)

DOMAIN = "scharger_huawei_modbus"

async def async_setup_entry(hass, config_entry):
    port = config_entry.options.get("port", 502)
    register_manager = ModbusRegisterManager()
    server = start_modbus_server(register_manager, port=port)

    hass.data[DOMAIN] = {
        "register_manager": register_manager,
        "modbus_server": server
    }

    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor", "number"])

    hass.services.async_register(DOMAIN, "enable_debug", lambda call: register_manager.set_debug(True))
    hass.services.async_register(DOMAIN, "disable_debug", lambda call: register_manager.set_debug(False))
    return True

async def async_unload_entry(hass, config_entry):
    await hass.config_entries.async_unload_platforms(config_entry, ["sensor", "number"])
    if DOMAIN in hass.data:
        server = hass.data[DOMAIN].get("modbus_server")
        if server:
            server.shutdown()
            server.server_close()
        hass.data.pop(DOMAIN)
    return True
