"""Huawei SCharger Modbus Integration Init"""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager, PRESET_REGISTER_VALUES
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry):
    port = config_entry.data.get("port", 502)
    debug = config_entry.data.get("debug_logging", False)

    register_manager = ModbusRegisterManager()
    server = start_modbus_server(register_manager, port=port)

    for addr, val in PRESET_REGISTER_VALUES.items():
        register_manager.set(addr, val)
        _LOGGER.debug("[MODBUS] Preset register 0x%04X = %d", addr, val)

    if debug:
        _LOGGER.setLevel(logging.DEBUG)
        register_manager.set_debug(True)

    hass.data[DOMAIN] = {
        "register_manager": register_manager,
        "modbus_server": server
    }

    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor"])
    return True

async def async_unload_entry(hass, config_entry):
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, ["sensor"])
    server = hass.data[DOMAIN].get("modbus_server")
    if server:
        try:
            _LOGGER.info("[MODBUS] Gracefully shutting down Modbus TCP server...")
            server.shutdown()
            server.server_close()
            _LOGGER.info("[MODBUS] Server closed and socket released")
        except Exception as e:
            _LOGGER.warning("[MODBUS] Failed to release server socket: %s", e)
    hass.data.pop(DOMAIN, None)
    return unload_ok
