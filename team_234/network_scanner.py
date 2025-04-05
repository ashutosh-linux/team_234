import os
import json
import subprocess
import socket
import psutil

def get_arp_table():
    try:
        output = subprocess.check_output("arp -a", shell=True, text=True)
        return output.strip()
    except Exception as e:
        return str(e)

def get_dns_cache():
    try:
        output = subprocess.check_output("ipconfig /displaydns", shell=True, text=True, errors="ignore")
        return output.strip()
    except Exception as e:
        return str(e)

def get_open_connections():
    connections = []
    try:
        for conn in psutil.net_connections():
            try:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
                connections.append({
                    "type": str(conn.type),
                    "status": conn.status,
                    "local_address": laddr,
                    "remote_address": raddr,
                    "pid": conn.pid
                })
            except:
                continue
        return connections
    except Exception as e:
        return str(e)

def get_network_shares():
    try:
        output = subprocess.check_output("net share", shell=True, text=True)
        return output.strip()
    except Exception as e:
        return str(e)

def get_adapter_info():
    info = []
    try:
        addrs = psutil.net_if_addrs()
        for iface, addr_list in addrs.items():
            for addr in addr_list:
                if addr.family == socket.AF_INET:
                    info.append({
                        "interface": iface,
                        "ip_address": addr.address,
                        "netmask": addr.netmask,
                        "broadcast": addr.broadcast
                    })
        return info
    except Exception as e:
        return str(e)

def main():
    print("[*] Scanning network info...")

    results = {
        "arp_table": get_arp_table(),
        "dns_cache": get_dns_cache(),
        "open_connections": get_open_connections(),
        "network_shares": get_network_shares(),
        "adapter_info": get_adapter_info()
    }

    os.makedirs("data", exist_ok=True)
    with open("data/network_scan.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("✅ Network scan completed and saved to 'data/network_scan.json'.")

if __name__ == "__main__":
    main()
