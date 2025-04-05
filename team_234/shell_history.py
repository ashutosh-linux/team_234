import os
import re

# Common PowerShell history locations
history_paths = [
    os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"),
    os.path.expanduser(r"~\Documents\PowerShell_history.txt")  # Just in case
]

# Regex patterns to match sensitive data
patterns = [
    r'(?i)(password\s*=\s*["\'].*?["\'])',
    r'(?i)(token\s*=\s*["\'].*?["\'])',
    r'(?i)(apikey\s*=\s*["\'].*?["\'])',
    r'(?i)(secret\s*=\s*["\'].*?["\'])',
    r'(?i)(credential.*)',
    r'(?i)(ConvertTo-SecureString.*)'
]

matches = []

for path in history_paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, 1):
                for pattern in patterns:
                    if re.search(pattern, line):
                        matches.append({
                            "line_number": line_num,
                            "content": line.strip(),
                            "pattern": pattern
                        })

# Store results
import json
with open("data/posh_history_scan.json", "w", encoding="utf-8") as f:
    json.dump(matches, f, indent=2)

print(f"✅ Scanned PowerShell history. {len(matches)} suspicious lines found.")
