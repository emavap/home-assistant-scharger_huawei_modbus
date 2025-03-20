DOMAIN = "scharger_huawei_modbus"

REGISTER_MAP = {
    # --- Collected Signals (provided by charger → sensor entities in HA) ---
    0x1000: {"name": "Phase L1 Output Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1002: {"name": "Phase L2 Output Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1004: {"name": "Phase L3 Output Voltage", "unit": "V", "scale": 0.1, "type": "sensor"},
    0x1006: {"name": "Phase L1 Output Current", "unit": "A", "scale": 0.1, "type": "sensor"},
    0x1008: {"name": "Phase L2 Output Current", "unit": "A", "scale": 0.1, "type": "sensor"},
    0x100A: {"name": "Phase L3 Output Current", "unit": "A", "scale": 0.1, "type": "sensor"},
    0x100C: {"name": "Total Output Power", "unit": "kW", "scale": 0.1, "type": "sensor"},

    # --- Setting Signals (provided by HA → number/select entities in HA) ---
    0x2000: {"name": "Maximum Charge Power", "unit": "kW", "scale": 0.1, "type": "number", "min": 0, "max": 22},
    0x2006: {"name": "Charging Control", "unit": None, "scale": 1, "type": "number", "min": 0, "max": 2}
}
