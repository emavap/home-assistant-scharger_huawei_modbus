from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN


class HuaweiChargerFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Huawei Charger", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional("debug", default=False): bool
            })
        )

    async def async_get_options_flow(self, config_entry):
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
                vol.Optional("debug", default=self.config_entry.options.get("debug", False)): bool
            })
        )
