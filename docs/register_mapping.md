# Huawei SCharger REGISTER_MAP (Final Correct Version)

## Setting Signal Registers (Writable)

| Address | Name                   | Unit | Type   | Min | Max |
|---------|------------------------|------|--------|-----|-----|
| 0x3000  | Enable Charging         | -    | number | 0   | 1   |
| 0x3001  | Charging Mode           | -    | number | 0   | 2   |
| 0x3002  | Max Current Setting     | A    | number | 6   | 32  |
| 0x3003  | Charging Power Limit    | W    | number |1000 |7400 |
| 0x3010  | Start Charging Trigger  | -    | number | 0   | 1   |

## Collected Signal Registers (Read-only Sensors)

| Address | Name                     | Unit | Type   |
|---------|--------------------------|------|--------|
| 0x3100  | Charging Status Code     | -    | sensor |
| 0x3101  | Charging Current L1      | A    | sensor |
| 0x3102  | Charging Voltage L1      | V    | sensor |
| 0x3103  | Total Charging Energy    | kWh  | sensor |
| 0x3104  | Session Energy Delivered | kWh  | sensor |
