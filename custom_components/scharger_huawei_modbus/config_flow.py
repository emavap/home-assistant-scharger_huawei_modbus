from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class HuaweiChargerFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Huawei Charger", data={}, options=user_input)
        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Optional("debug", default=False): bool
        }))

    async def async_get_options_flow(self, config_entry):
        return self

    async def async_step_init(self, user_input=None):
        return await self.async_step_user(user_input)

    async def async_step_options(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data={}, options=user_input)
        return self.async_show_form(step_id="options", data_schema=vol.Schema({
            vol.Optional("debug", default=self.options.get("debug", False)): bool
        }))