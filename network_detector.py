def analyze_network(network_summary_path):
    results = {
        "tls_detected": False,
        "external_ip_detected": False,
        "persistent_connection_detected": False,
        "tor_like_port_detected": False,
        "evidence": []
    }

    try:
        with open(network_summary_path, "r", encoding="utf-8") as f:
            content = f.read().lower()

            if "tls" in content or "encrypted" in content:
                results["tls_detected"] = True
                results["evidence"].append("TLS/encrypted traffic detected")

            if "public ip" in content or "external" in content:
                results["external_ip_detected"] = True
                results["evidence"].append("external IP communication detected")

            if "persistent" in content:
                results["persistent_connection_detected"] = True
                results["evidence"].append("persistent network connection detected")

            if "9001" in content or "9030" in content:
                results["tor_like_port_detected"] = True
                results["evidence"].append("Tor-like port usage detected")

    except FileNotFoundError:
        results["evidence"].append("network summary file not found")

    return results