from __future__ import annotations
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([AgriotSensor()])

class AgriotSensor(SensorEntity):
    _attr_name = "Agriot Status"
    _attr_native_value = "ok"
    _attr_icon = "mdi:leaf"

    async def async_update(self):
        return