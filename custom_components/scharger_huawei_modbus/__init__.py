"""Init file for Huawei SCharger Modbus."""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager, PRESET_REGISTER_VALUES

_LOGGER = logging.getLogger(__name__)
DOMAIN = "scharger_huawei_modbus"

async def async_setup_entry(hass, config_entry):
    port = config_entry.options.get("port", 502)
    _LOGGER.debug("Starting Huawei SCharger Modbus integration")

    register_manager = ModbusRegisterManager()
    server = start_modbus_server(register_manager, port=port)

    # Preload preset setting signal registers
    for addr, val in PRESET_REGISTER_VALUES.items():
        register_manager.set(addr, val)
        _LOGGER.debug("[MODBUS] Preset register 0x%04X = %d", addr, val)

    hass.data[DOMAIN] = {
        "register_manager": register_manager,
        "modbus_server": server
    }

    await hass.config_entries.async_forward_entry_setups(config_entry, ["number"])

    hass.services.async_register(DOMAIN, "enable_debug", lambda call: register_manager.set_debug(True))
    hass.services.async_register(DOMAIN, "disable_debug", lambda call: register_manager.set_debug(False))

    return True

async def async_unload_entry(hass, config_entry):
    await hass.config_entries.async_unload_platforms(config_entry, ["number"])
    if DOMAIN in hass.data:
        server = hass.data[DOMAIN].get("modbus_server")
        if server:
            server.shutdown()
            server.server_close()
        hass.data.pop(DOMAIN)
    return True
