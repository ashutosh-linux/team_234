# cve_scanner.py
import json
import time

# Simulated vulnerability scanning process
print("🔍 Starting CVE scan for system components...")
time.sleep(1)

# Simulated CVE data (you can later replace this with live data fetching from NVD, CISA, etc.)
vulnerabilities = {
    "matches": [
        {
            "title": "Adobe Reader",
            "cve": {
                "id": "CVE-2023-12345",
                "summary": "Buffer overflow in Adobe Reader allows remote attackers to execute arbitrary code."
            },
            "remediation": "Update to the latest version via Adobe's official website."
        },
        {
            "title": "Windows Defender",
            "cve": {
                "id": "CVE-2024-67890",
                "summary": "Privilege escalation vulnerability in Windows Defender service."
            },
            "remediation": "Install the latest Windows security patch (KB5021234)."
        },
        {
            "title": "Microsoft Edge",
            "cve": {
                "id": "CVE-2023-90876",
                "summary": "Out-of-bounds write vulnerability in Microsoft Edge memory heap."
            },
            "remediation": "Update Edge to the latest version via Windows Update."
        }
    ]
}

# Save to JSON file
output_file = "vulnerabilities.json"
try:
    with open(output_file, "w") as f:
        json.dump(vulnerabilities, f, indent=4)
    print(f"✅ Vulnerability data saved to '{output_file}'")
except Exception as e:
    print(f"❌ Error saving vulnerabilities: {e}")
