# Huawei SCharger Modbus Integration for Home Assistant

This custom integration allows Home Assistant to act as a Modbus TCP server that exposes setting signal registers for Huawei AC EV Chargers (SCharger), based on Huawei's official Modbus TCP documentation.

## ✅ Features
- Modbus TCP Server (Home Assistant as server, charger as client)
- Fully Huawei-compliant register mapping (based on official docs)
- Configuration flow UI for Modbus port + debug logging
- Real-time control of charging settings via HA entities

## 🔧 Configuration Options
- Modbus TCP Port (default: 502)
- Enable Debug Logging (toggle in setup UI)

## 📦 Exposed Registers
| Register | Entity Name                 | Type     | Description                  |
|---------:|-----------------------------|----------|------------------------------|
| 0x3000   | Enable Charging              | Number   | 0=Disabled, 1=Enabled         |
| 0x3001   | Charging Mode                | Number   | 0=Auto, 1=Manual, 2=Timed     |
| 0x3002   | Max Current Setting (A)      | Number   | Set max charging current     |
| 0x3003   | Charging Power Limit (W)     | Number   | Set max power limit          |
| 0x3004   | Allow Charging               | Number   | 1=Allow charge                |
| 0x3005   | Cable Detection              | Number   | 1=Detected                   |
| 0x3006   | Comm Handshake Status        | Number   | 1=OK                         |
| 0x3010   | Start Charging Trigger       | Number   | 1=Trigger charging            |

## 📥 Installation
1. Extract to `/config/custom_components/scharger_huawei_modbus/`
2. Restart Home Assistant
3. Go to *Settings → Devices & Services → Add Integration → Huawei Charger*
4. Select port and enable logging if needed

## 💡 Lovelace Dashboard Demo

See `lovelace_example.yaml` in this repo for an example dashboard.

---

## 📸 Screenshot

> _(Add a screenshot here after installing)_

---

## 📄 Based on:
- [Huawei Northbound Modbus-TCP Interconnection Protocol for AC Chargers (official documentation)]

---

Enjoy controlling your charger via Home Assistant!
