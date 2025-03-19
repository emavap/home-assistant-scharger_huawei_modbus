# Huawei SCharger Modbus Integration for Home Assistant

This custom integration allows Home Assistant to act as a **Modbus TCP server** for Huawei SCharger AC chargers.

It exposes all charger registers as real Home Assistant entities (sensors and numbers), allowing you to **monitor and control** your charger from the UI.

---

## 🚀 Features

✅ Modbus TCP Server  
✅ Read/Write to actual charger registers  
✅ Sensor & Number entities auto-generated from `REGISTER_MAP`  
✅ Automatic polling with `SCAN_INTERVAL`  
✅ Entity grouping under a single device  
✅ Toggle debug logging via services

---

## 📂 Installation (via HACS or manually)

### Option A: HACS
1. Add this repo as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories/):
   ```
   https://github.com/yourusername/home-assistant-scharger_huawei_modbus
   ```
   Category: **Integration**
2. Install the integration.
3. Restart Home Assistant.

### Option B: Manual
1. Copy this folder to:  
   `/config/custom_components/scharger_huawei_modbus/`
2. Restart Home Assistant.

---

## ⚙ Configuration

After restart:
1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **Huawei SCharger Modbus**
3. Confirm setup (no parameters needed)

### Configure Port & Logging:
After adding:
- Click **Configure**
- You can set:
  - Modbus TCP Port (default `502`)
  - Debug Logging (on/off)

---

## 🔧 Services

| Service | Description |
|--------|-------------|
| `scharger_huawei_modbus.enable_debug` | Enables full debug logging |
| `scharger_huawei_modbus.disable_debug` | Disables debug logging |

---

## 📡 Auto Polling

- Entities automatically poll values every 10 seconds (`SCAN_INTERVAL`).

---

## 🧪 Testing with Modbus Client

You can use the included `modbus_client_mac.py` script to:
- Read registers
- Write charging values
- Simulate charger interaction

---

## 💡 Credits

Built and maintained by [@yourusername](https://github.com/yourusername)

Inspired by [iobroker.huawei-charger](https://github.com/DNAngelX/ioBroker.huawei-charger)

---

## 🖼 Screenshots

*(Include screenshots of Lovelace dashboard, debug logs, and entities here)*

