DOMAIN = "scharger_huawei_modbus"

REGISTER_MAP = {
    0x3000: {"name": "Enable Charging", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3001: {"name": "Charging Mode", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 2},
    0x3002: {"name": "Max Current Setting", "unit": "A", "scale": 1, "type": "number", "min": 6, "max": 32},
    0x3003: {"name": "Charging Power Limit", "unit": "W", "scale": 1, "type": "number", "min": 1000, "max": 7400},
    0x3004: {"name": "Allow Charging", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3005: {"name": "Cable Detection", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3006: {"name": "Comm Handshake Status", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3010: {"name": "Start Charging Trigger", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3100: {"name": "Charging Status Code", "unit": None, "scale": 1, "type": "sensor"},
    0x3101: {"name": "Charging Current L1", "unit": "A", "scale": 1, "type": "sensor"},
    0x3102: {"name": "Charging Voltage L1", "unit": "V", "scale": 1, "type": "sensor"},
    0x3103: {"name": "Total Charging Energy", "unit": "kWh", "scale": 0.01, "type": "sensor"},
    0x3104: {"name": "Session Energy Delivered", "unit": "kWh", "scale": 0.01, "type": "sensor"}
}
