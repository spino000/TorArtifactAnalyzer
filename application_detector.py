from utils import read_file_content

def analyze_application_file(file_path):
    content = read_file_content(file_path)

    results = {
        "tor_profile_found": False,
        "places_sqlite_found": False,
        "cookies_sqlite_found": False,
        "evidence": []
    }

    if "profile.default" in content:
        results["tor_profile_found"] = True
        results["evidence"].append(f"Tor profile found in {file_path}")

    if "places.sqlite" in content:
        results["places_sqlite_found"] = True
        results["evidence"].append(f"places.sqlite found in {file_path}")

    if "cookies.sqlite" in content:
        results["cookies_sqlite_found"] = True
        results["evidence"].append(f"cookies.sqlite found in {file_path}")

    return results