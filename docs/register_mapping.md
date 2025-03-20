# Huawei SCharger Modbus REGISTER_MAP Reference

This file documents all supported Modbus registers exposed by the Home Assistant Modbus Server
as per Huawei's Northbound Modbus-TCP Interconnection Protocol documentation.

## 📘 Setting Signal Registers

| Address | Name                     | Type   | Unit | Min | Max | Description                          |
|---------|--------------------------|--------|------|-----|-----|--------------------------------------|
| 0x3000 | Enable Charging           | number | -    | 0   | 1   | 1 = Enabled                          |
| 0x3001 | Charging Mode             | number | -    | 0   | 2   | 0=Auto, 1=Manual, 2=Timed            |
| 0x3002 | Max Current Setting       | number | A    | 6   | 32  | Maximum allowed current              |
| 0x3003 | Charging Power Limit      | number | W    |1000 |7400 | Power limit setting                  |
| 0x3004 | Allow Charging            | number | -    | 0   | 1   | Charging allowed flag                |
| 0x3005 | Cable Detection           | number | -    | 0   | 1   | 1 = Cable present                    |
| 0x3006 | Comm Handshake Status     | number | -    | 0   | 1   | Communication handshake ok           |
| 0x3010 | Start Charging Trigger    | number | -    | 0   | 1   | 1 = Trigger charging operation       |

## 📝 Notes
- All values are exposed through Home Assistant `NumberEntity` components.
- Values are readable and writable by the Huawei SCharger Modbus client.
- Units and scale are as per official documentation.

If additional collected or status registers are required (e.g., 0x3100+), this mapping can be expanded accordingly.
