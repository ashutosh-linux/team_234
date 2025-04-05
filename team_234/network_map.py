import subprocess
import re
import networkx as nx
import matplotlib.pyplot as plt
import socket
import os

# 📌 Create output folder if not exists
os.makedirs("output", exist_ok=True)

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def parse_arp_table():
    try:
        output = subprocess.check_output("arp -a", shell=True, text=True)
        arp_entries = []
        pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([\w-]+)\s+([\w]+)"
        for match in re.finditer(pattern, output):
            ip, mac, _ = match.groups()
            arp_entries.append((ip, mac))
        return arp_entries
    except Exception as e:
        print(f"[!] Error parsing ARP: {e}")
        return []

def draw_network_map(arp_entries):
    G = nx.Graph()
    local_ip = get_local_ip()
    G.add_node(local_ip, color="skyblue", label=f"{local_ip}\n(Localhost)")

    for ip, mac in arp_entries:
        label = f"{ip}\n{mac}"
        G.add_node(ip, color="lightgreen", label=label)
        G.add_edge(local_ip, ip)

    colors = [G.nodes[n]['color'] for n in G.nodes]
    labels = {n: G.nodes[n]['label'] for n in G.nodes}

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=False, node_color=colors, node_size=2000, font_size=8, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)

    # 📌 Save and Show
    plt.title("Network Topology Map")
    plt.tight_layout()
    output_path = "output/network_map.png"
    plt.savefig(output_path)
    plt.show()
    print(f"✅ Network map saved at {output_path}")
    return output_path

def main():
    print("[*] Generating Network Map from ARP Table...")
    arp_entries = parse_arp_table()
    if arp_entries:
        image_path = draw_network_map(arp_entries)
        print("✅ Network map displayed and saved.")
    else:
        print("⚠️ No devices found in ARP table.")

if __name__ == "__main__":
    main()
