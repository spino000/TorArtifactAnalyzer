from utils import read_file_content

def analyze_memory_file(file_path):
    content = read_file_content(file_path)

    results = {
        "tor_process_detected": False,
        "firefox_detected": False,
        "tor_related_connections": False,
        "evidence": []
    }

    if "tor.exe" in content:
        results["tor_process_detected"] = True
        results["evidence"].append(f"tor.exe found in {file_path}")

    if "firefox.exe" in content:
        results["firefox_detected"] = True
        results["evidence"].append(f"firefox.exe found in {file_path}")

    if ":9001" in content or "185.220." in content:
        results["tor_related_connections"] = True
        results["evidence"].append(f"possible Tor-related connection found in {file_path}")

    return results