# 🔐 Agent-less Windows System Vulnerability and Network Scanner

This is a Blue Team security tool designed to **scan, analyze, and report potential vulnerabilities** in Windows 10/11 systems **without installing any agents**. It combines system scanning, PowerShell history analysis, network enumeration, CVE lookup, and automated PDF report generation.

---

## 🚀 Features

- ✅ **Agent-less Design** – No installation needed on the target machine
- ✅ **System Info Scanner** – Gathers hardware, OS, patch, and service info
- ✅ **PowerShell History Scan** – Identifies suspicious or malicious commands
- ✅ **Network Scanner** – Lists all active devices in the subnet
- ✅ **CVE Scanner** – Detects known vulnerabilities from system data
- ✅ **Network Mapper** – Visualizes the local network topology
- ✅ **Auto PDF Report Generator** – Summarizes findings in a clean report

---

## 🧰 Modules Overview

| Script                        | Description |
|------------------------------|-------------|
| `scanner.py`                 | Collects OS, hardware, and system configuration data |
| `scan_powershell_history.py` | Analyzes PowerShell command history for suspicious lines |
| `network_scanner.py`         | Scans the local network and logs connected devices |
| `cve_scanner.py`             | Performs CVE lookup using system data |
| `network_map.py`             | Creates a network map image from scanned data |
| `generate_report.py`         | Combines all JSON outputs into a final PDF report |

---

## 🛠 How to Run (in PowerShell)

```powershell
python scanner.py
python scan_powershell_history.py
python network_scanner.py
python cve_scanner.py
python network_map.py
python generate_report.py
