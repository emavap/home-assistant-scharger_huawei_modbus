"""Huawei SCharger Modbus Integration Init"""
import logging
from .modbus_server import start_modbus_server, ModbusRegisterManager, PRESET_REGISTER_VALUES
from .const import DOMAIN, REGISTER_MAP

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry):
    port = config_entry.data.get("port", 502)
    debug = config_entry.data.get("debug_logging", False)

    register_manager = ModbusRegisterManager()
    server = start_modbus_server(register_manager, port=port)

    # Clear collected sensor registers (0x1000–0x100C range)
    for addr in REGISTER_MAP:
        if addr >= 0x1000 and addr <= 0x100C and REGISTER_MAP[addr]["type"] == "sensor":
            register_manager.set(addr, 0)
            _LOGGER.debug("[MODBUS] Cleared sensor register 0x%04X", addr)

    # Only preset HA-owned setting signals
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

    _LOGGER.info("[MODBUS] Integration setup complete.")
    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor", "number"])
    return True

async def async_unload_entry(hass, config_entry):
    _LOGGER.info("[MODBUS] Starting integration unload process...")
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, ["sensor", "number"])

    server = hass.data[DOMAIN].get("modbus_server")
    if server:
        try:
            _LOGGER.info("[MODBUS] Attempting to gracefully shutdown Modbus TCP server...")
            server.shutdown()
            server.server_close()
            _LOGGER.info("[MODBUS] Server shutdown and socket released successfully.")
        except Exception as e:
            _LOGGER.warning("[MODBUS] Server shutdown failed: %s", e)

    hass.data.pop(DOMAIN, None)
    _LOGGER.info("[MODBUS] Integration unload completed.")
    return unload_ok
