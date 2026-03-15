from utils import read_file_content

def analyze_disk_file(file_path):
    content = read_file_content(file_path)

    results = {
        "tor_prefetch_found": False,
        "firefox_prefetch_found": False,
        "tor_folder_found": False,
        "suspicious_archive_found": False,
        "evidence": []
    }

    if "tor.exe.pf" in content:
        results["tor_prefetch_found"] = True
        results["evidence"].append(f"Tor prefetch found in {file_path}")

    if "firefox.exe.pf" in content:
        results["firefox_prefetch_found"] = True
        results["evidence"].append(f"Firefox prefetch found in {file_path}")

    if "tor browser" in content or "profile.default" in content:
        results["tor_folder_found"] = True
        results["evidence"].append(f"Tor Browser artifacts found in {file_path}")

    if ".zip" in content or ".rar" in content or ".7z" in content:
        results["suspicious_archive_found"] = True
        results["evidence"].append(f"Suspicious archive reference found in {file_path}")

    return results