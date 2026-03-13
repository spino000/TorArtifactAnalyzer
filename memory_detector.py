def analyze_memory(pslist_path, netscan_path):
    results = {
        "tor_process_detected": False,
        "firefox_detected": False,
        "tor_related_connections": False,
        "evidence": []
    }

    # Check process list
    try:
        with open(pslist_path, "r", encoding="utf-8") as f:
            content = f.read().lower()

            if "tor.exe" in content:
                results["tor_process_detected"] = True
                results["evidence"].append("tor.exe found in memory process list")

            if "firefox.exe" in content:
                results["firefox_detected"] = True
                results["evidence"].append("firefox.exe found in memory process list")

    except FileNotFoundError:
        results["evidence"].append("pslist file not found")

    # Check network scan
    try:
        with open(netscan_path, "r", encoding="utf-8") as f:
            content = f.read().lower()

            if ":9001" in content or "185.220." in content:
                results["tor_related_connections"] = True
                results["evidence"].append("possible Tor-related connection found in netscan")

    except FileNotFoundError:
        results["evidence"].append("netscan file not found")

    return results