import csv

def analyze_disk(disk_csv_path):
    results = {
        "tor_prefetch_found": False,
        "firefox_prefetch_found": False,
        "tor_folder_found": False,
        "suspicious_archive_found": False,
        "evidence": []
    }

    try:
        with open(disk_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                artifact_name = row["artifact_name"].lower()
                path = row["path"].lower()

                if artifact_name == "tor.exe.pf":
                    results["tor_prefetch_found"] = True
                    results["evidence"].append(f"Tor prefetch found: {row['path']}")

                if artifact_name == "firefox.exe.pf":
                    results["firefox_prefetch_found"] = True
                    results["evidence"].append(f"Firefox prefetch found: {row['path']}")

                if "tor browser" in artifact_name or "tor browser" in path:
                    results["tor_folder_found"] = True
                    results["evidence"].append(f"Tor Browser folder found: {row['path']}")

                if artifact_name.endswith(".zip") or artifact_name.endswith(".rar") or artifact_name.endswith(".7z"):
                    results["suspicious_archive_found"] = True
                    results["evidence"].append(f"Suspicious archive found: {row['path']}")

    except FileNotFoundError:
        results["evidence"].append("disk artifacts CSV file not found")

    return results