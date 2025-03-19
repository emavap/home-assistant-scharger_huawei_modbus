REGISTER_MAP = {
    0x3000: {"name": "Enable Charging", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3001: {"name": "Charging Mode", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 3},
    0x3002: {"name": "Max Current Setting", "unit": "A", "scale": 1, "type": "number", "min": 6, "max": 32},
    0x3003: {"name": "Charging Power Limit", "unit": "W", "scale": 1, "type": "number", "min": 1000, "max": 7400},
    0x3004: {"name": "Allow Charging", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3005: {"name": "Cable Detection", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3006: {"name": "Comm Handshake Status", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1},
    0x3010: {"name": "Start Charging Trigger", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 1}
}
