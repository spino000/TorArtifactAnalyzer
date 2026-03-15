from utils import read_file_content

def analyze_network_file(file_path):
    content = read_file_content(file_path)

    results = {
        "tls_detected": False,
        "external_ip_detected": False,
        "persistent_connection_detected": False,
        "tor_like_port_detected": False,
        "evidence": []
    }

    if "tls" in content or "encrypted" in content:
        results["tls_detected"] = True
        results["evidence"].append(f"TLS/encrypted traffic detected in {file_path}")

    if "public ip" in content or "external" in content or "185.220." in content:
        results["external_ip_detected"] = True
        results["evidence"].append(f"External IP communication detected in {file_path}")

    if "persistent" in content or "established" in content:
        results["persistent_connection_detected"] = True
        results["evidence"].append(f"Persistent connection detected in {file_path}")

    if "9001" in content or "9030" in content or "9050" in content:
        results["tor_like_port_detected"] = True
        results["evidence"].append(f"Tor-like port usage detected in {file_path}")

    return results