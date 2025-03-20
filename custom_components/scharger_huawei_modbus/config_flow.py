from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_PORT
from .const import DOMAIN

CONF_DEBUG = "debug_logging"

class HuaweiChargerFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Huawei Charger", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(CONF_PORT, default=502): int,
                vol.Optional(CONF_DEBUG, default=False): bool,
            }),
            errors=errors
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        return HuaweiChargerOptionsFlowHandler(config_entry)

class HuaweiChargerOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(CONF_PORT, default=self.config_entry.data.get(CONF_PORT, 502)): int,
                vol.Optional(CONF_DEBUG, default=self.config_entry.data.get(CONF_DEBUG, False)): bool,
            })
        )
