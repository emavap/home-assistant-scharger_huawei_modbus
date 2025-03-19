# Huawei SCharger Modbus TCP Integration for Home Assistant

This custom integration exposes a Modbus TCP **Server** that allows direct communication between Home Assistant and Huawei AC Chargers, based on the official Huawei Northbound Modbus TCP Interconnection Protocol.

## Features
✅ Fully compliant with Huawei documentation  
✅ Real Modbus TCP Server implementation  
✅ Bidirectional sync of HA entities and Modbus registers  
✅ Register persistence across restarts  
✅ Configurable debug logging (via UI setup)  
✅ Works on HA OS / Supervised / Container  

## Supported Entities

| Register | Entity                         | Type     | Unit | Scale |
|---------:|-------------------------------|----------|------|-------|
| 0x1000  | Phase L1 Voltage               | Sensor   | V    | 0.1   |
| 0x1002  | Phase L2 Voltage               | Sensor   | V    | 0.1   |
| 0x1004  | Phase L3 Voltage               | Sensor   | V    | 0.1   |
| 0x1006  | Phase L1 Current               | Sensor   | A    | 0.1   |
| 0x100C  | Total Output Power             | Sensor   | kW   | 0.1   |
| 0x2000  | Maximum Charging Power         | Number   | kW   | 0.1   |
| 0x2006  | Charging Control               | Number   | -    | 1     |

## Installation

1. Download and extract this repo to `/config/custom_components/scharger_huawei_modbus/`
2. Restart Home Assistant
3. Go to Settings → Devices & Services → Add Integration → Huawei SCharger Modbus
4. Optionally enable debug logging
5. Enjoy automatic entity creation!

## Lovelace Dashboard Example

See `examples/lovelace_dashboard.yaml` for a ready-to-import UI panel.

## License

MIT