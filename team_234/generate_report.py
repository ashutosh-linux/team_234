from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
import json
import os

# Set paths for data files
data_files = {
    "System Scan": "data/system_scan.json",
    "PowerShell History Scan": "data/posh_history_scan.json",
    "Network Scan": "data/network_scan.json",
    "Vulnerabilities": "data/vulnerabilities.json"
}

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            return json.load(file)
    return None

def format_dict_data(data):
    if isinstance(data, dict):
        return [f"• {key}: {value}" for key, value in data.items()]
    elif isinstance(data, list):
        lines = []
        for item in data:
            if isinstance(item, dict):
                lines.append("• " + ", ".join(f"{k}: {v}" for k, v in item.items()))
            else:
                lines.append(f"• {item}")
        return lines
    else:
        return [str(data)]

def generate_report(output_file="final_report.pdf"):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    for section, path in data_files.items():
        data = load_json(path)
        flowables.append(Spacer(1, 12))
        flowables.append(Paragraph(f"<b>{section}</b>", styles['Heading2']))

        if data:
            lines = format_dict_data(data)
            for line in lines:
                flowables.append(Paragraph(line, styles['Normal']))
        else:
            flowables.append(Paragraph("• No data available.", styles['Normal']))

        flowables.append(Spacer(1, 12))

    doc.build(flowables)
    print(f"✅ Final report saved as '{output_file}'")

if __name__ == "__main__":
    generate_report()
