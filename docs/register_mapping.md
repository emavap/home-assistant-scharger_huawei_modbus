# Huawei SCharger REGISTER_MAP - Compliant Version

## Collected Signals (from charger to HA):
| Address | Name                     | Unit | Scale | Entity Type |
|---------|--------------------------|------|-------|-------------|
| 0x1000 | Phase L1 Output Voltage   | V    | 0.1   | Sensor      |
| 0x1002 | Phase L2 Output Voltage   | V    | 0.1   | Sensor      |
| 0x1004 | Phase L3 Output Voltage   | V    | 0.1   | Sensor      |
| 0x1006 | Phase L1 Output Current   | A    | 0.1   | Sensor      |
| 0x1008 | Phase L2 Output Current   | A    | 0.1   | Sensor      |
| 0x100A | Phase L3 Output Current   | A    | 0.1   | Sensor      |
| 0x100C | Total Output Power        | kW   | 0.1   | Sensor      |

## Setting Signals (from HA to charger):
| Address | Name                  | Unit | Scale | Min | Max | Entity Type |
|---------|------------------------|------|-------|-----|-----|-------------|
| 0x2000 | Maximum Charge Power   | kW   | 0.1   | 0   | 22  | Number      |
| 0x2006 | Charging Control       | -    | 1     | 0   | 2   | Number      |
