def analyze_application(app_artifacts_path):
    results = {
        "tor_profile_found": False,
        "places_sqlite_found": False,
        "cookies_sqlite_found": False,
        "evidence": []
    }

    try:
        with open(app_artifacts_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

            for line in lines:
                lower_line = line.lower()

                if "profile.default" in lower_line:
                    results["tor_profile_found"] = True
                    results["evidence"].append(f"Tor browser profile found: {line.strip()}")

                if "places.sqlite" in lower_line:
                    results["places_sqlite_found"] = True
                    results["evidence"].append(f"places.sqlite found: {line.strip()}")

                if "cookies.sqlite" in lower_line:
                    results["cookies_sqlite_found"] = True
                    results["evidence"].append(f"cookies.sqlite found: {line.strip()}")

    except FileNotFoundError:
        results["evidence"].append("application artifacts file not found")

    return results