from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN
from .modbus_server import start_modbus_server, ModbusRegisterManager
from .config_flow import HuaweiChargerFlow

register_manager = ModbusRegisterManager()

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["register_manager"] = register_manager
    register_manager.set_debug(entry.options.get("debug", False))
    start_modbus_server(register_manager)
    hass.async_create_task(hass.config_entries.async_forward_entry_setups(entry, ["sensor", "number"]))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True

def async_get_options_flow(config_entry: ConfigEntry):
    return HuaweiChargerFlow()