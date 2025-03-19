# Huawei SCharger Modbus Integration for Home Assistant

This integration allows Home Assistant to act as a Modbus TCP server for Huawei SCharger EV chargers.
It exposes charger registers as Home Assistant entities, allowing both monitoring and control from the UI.

---

## 📦 Features

- Modbus TCP Server (Home Assistant exposes registers)
- Real-time monitoring (Voltage, Current, Power, Energy)
- Configuration control (Charging power limit, Max current)
- Full bi-directional sync between HA entities and Modbus registers
- Debug logging and developer-friendly architecture

---

## 📂 Installation (via HACS)

### Step 1: Add Custom Repository
1. Go to **HACS > Integrations > Menu (⋮) > Custom repositories**
2. Add repository:  
   ```
   https://github.com/emavap/home-assistant-scharger_huawei_modbus
   ```
   - Category: **Integration**

### Step 2: Install Integration
1. After adding the repository, click **Install**
2. Restart Home Assistant

### Step 3: Configure Integration
1. Go to **Settings > Devices & Services > Add Integration**
2. Search for **Huawei SCharger Modbus**
3. Follow the configuration wizard

---

## ⚙ Configuration Options

| Option | Description |
|--------|-------------|
| `debug` | Enable/disable verbose Modbus data logging |

---

## 🧪 Lovelace Dashboard Example
Check `/examples/lovelace_dashboard.yaml` for a working sample dashboard showing:
- Charging power
- Charger voltage
- Max current setting

---

## 📑 Register Reference
All Modbus registers are documented in [`register_reference.md`](./register_reference.md)

---

## 📸 Screenshots
You can preview example screenshots in the `/docs/` folder.

---

## 💡 Developer Notes
- Follows Home Assistant best practices
- Entities separated in `sensor.py`, `number.py`, and dynamic Modbus server
- Easily extendable with more registers

---

## 🛠 Credits
Developed by [@emavap](https://github.com/emavap)

