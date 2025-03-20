DOMAIN = "scharger_huawei_modbus"

REGISTER_MAP = {
    # Documented Collected Signals (Read-only Sensors from PDF documentation)
    0x1000: {"name": "Phase L1 Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1002: {"name": "Phase L2 Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1004: {"name": "Phase L3 Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1006: {"name": "Phase L1 Current", "unit": "A", "scale": 0.01, "type": "sensor"},
    0x1008: {"name": "Phase L2 Current", "unit": "A", "scale": 0.01, "type": "sensor"},
    0x100A: {"name": "Phase L3 Current", "unit": "A", "scale": 0.01, "type": "sensor"},
    0x100C: {"name": "Total Output Power", "unit": "kW", "scale": 0.01, "type": "sensor"},
    0x100E: {"name": "Apparent Power", "unit": "kVA", "scale": 0.01, "type": "sensor"},
    0x1010: {"name": "Power Factor", "unit": "", "scale": 0.01, "type": "sensor"},
    0x1012: {"name": "Charger Temperature", "unit": "°C", "scale": 0.1, "type": "sensor"}
}
