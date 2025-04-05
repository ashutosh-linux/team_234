import wmi
import json
import psutil
import platform

def collect_system_info():
    c = wmi.WMI()

    system_info = {
        "OS": platform.system(),
        "Version": platform.version(),
        "Build": platform.release(),
        "Architecture": platform.architecture()[0],
        "CPU": platform.processor(),
        "Installed Software": [s.Name for s in c.Win32_Product()],
        "Running Processes": [p.name() for p in psutil.process_iter()]
    }

    with open("system_scan.json", "w") as file:
        json.dump(system_info, file, indent=4)

    print("✅ System scan completed. Data saved in 'system_scan.json'")

# Run the scanner
if __name__ == "__main__":
    collect_system_info()
