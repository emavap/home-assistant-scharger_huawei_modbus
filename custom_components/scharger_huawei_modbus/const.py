DOMAIN = "scharger_huawei_modbus"

REGISTER_MAP = {
    0x1000: {"name": "Phase L1 Voltage", "type": "sensor", "unit": "V", "scale": 0.1},
    0x1002: {"name": "Phase L2 Voltage", "type": "sensor", "unit": "V", "scale": 0.1},
    0x1004: {"name": "Phase L3 Voltage", "type": "sensor", "unit": "V", "scale": 0.1},
    0x1006: {"name": "Phase L1 Current", "type": "sensor", "unit": "A", "scale": 0.1},
    0x1008: {"name": "Phase L2 Current", "type": "sensor", "unit": "A", "scale": 0.1},
    0x100A: {"name": "Phase L3 Current", "type": "sensor", "unit": "A", "scale": 0.1},
    0x100C: {"name": "Total Output Power", "type": "sensor", "unit": "kW", "scale": 0.1},
    0x2000: {"name": "Maximum Charging Power", "type": "number", "unit": "kW", "scale": 0.1, "min": 0, "max": 22},
    0x2006: {"name": "Charging Control", "type": "number", "unit": "", "scale": 1, "min": 0, "max": 2},
}