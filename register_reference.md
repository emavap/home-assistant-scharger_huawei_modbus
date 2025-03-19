# Register Reference - Huawei SCharger

This table lists the supported registers in the current release of the integration.

| Address | Name                        | Type     | Access     | Unit | Scale | Notes                         |
|---------|-----------------------------|----------|------------|------|-------|-------------------------------|
| 0x1000  | Phase L1 Voltage            | Sensor   | Read-only  | V    | 0.1   | From Huawei documentation     |
| 0x100C  | Total Output Power          | Sensor   | Read-only  | kW   | 0.1   |                               |
| 0x2000  | Maximum Charging Power      | Number   | Read/Write | kW   | 0.1   | Set charging power limit      |
| 0x2006  | Charging Control            | Number   | Read/Write | -    | 1     | 0=Standby, 1=Paused, 2=Active |