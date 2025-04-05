import json
import os

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# System Info
system_info = {
    "OS": "Windows 11 Pro",
    "Architecture": "64-bit",
    "Processor": "Intel(R) Core(TM) i7-1185G7",
    "RAM": "16 GB",
    "Hostname": "TEAM-SECURE-PC",
    "Username": "admin_user"
}

# PowerShell History
powershell_history = [
    {
        "command": "Get-ChildItem -Path C:\\Windows\\System32",
        "timestamp": "2025-04-04T13:01:45Z"
    },
    {
        "command": "Invoke-WebRequest http://malicious-url.com",
        "timestamp": "2025-04-04T13:05:12Z"
    }
]

# Network Scan
network_scan = [
    {"IP": "192.168.0.101", "Hostname": "OfficePrinter", "MAC": "00:1A:2B:3C:4D:5E"},
    {"IP": "192.168.0.102", "Hostname": "LabRouter", "MAC": "AA:BB:CC:DD:EE:FF"}
]

# Vulnerabilities
vulnerabilities = [
    {"CVE_ID": "CVE-2023-45678", "Description": "SMB Remote Code Execution", "Severity": "Critical"},
    {"CVE_ID": "CVE-2024-11223", "Description": "Windows Kernel Elevation of Privilege", "Severity": "High"}
]

# Write to files
with open(f"{output_folder}/system_scan.json", "w") as f:
    json.dump(system_info, f, indent=4)

with open(f"{output_folder}/powershell_history.json", "w") as f:
    json.dump(powershell_history, f, indent=4)

with open(f"{output_folder}/network_scan.json", "w") as f:
    json.dump(network_scan, f, indent=4)

with open(f"{output_folder}/vulnerabilities.json", "w") as f:
    json.dump(vulnerabilities, f, indent=4)

print("✅ Dummy data created successfully!")
