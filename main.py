import os
from datetime import datetime

from memory_detector import analyze_memory_file
from disk_detector import analyze_disk_file
from network_detector import analyze_network_file
from application_detector import analyze_application_file
from correlator import correlate_evidence
from report_generator import generate_report
from utils import read_file_content


def merge_results(base, new):
    for key, value in new.items():
        if key == "evidence":
            base["evidence"].extend(value)
        elif isinstance(value, bool):
            if value:
                base[key] = True
    return base


def analyze_folder(
    input_folder="input",
    output_folder="output",
    case_name="Unknown Case",
    investigator_name="Unknown Investigator"
):
    memory_results = {
        "tor_process_detected": False,
        "firefox_detected": False,
        "tor_related_connections": False,
        "evidence": []
    }

    disk_results = {
        "tor_prefetch_found": False,
        "firefox_prefetch_found": False,
        "tor_folder_found": False,
        "suspicious_archive_found": False,
        "evidence": []
    }

    network_results = {
        "tls_detected": False,
        "external_ip_detected": False,
        "persistent_connection_detected": False,
        "tor_like_port_detected": False,
        "evidence": []
    }

    application_results = {
        "tor_profile_found": False,
        "places_sqlite_found": False,
        "cookies_sqlite_found": False,
        "evidence": []
    }

    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder not found: {input_folder}")

    os.makedirs(output_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_case_name = case_name.replace(" ", "_")
    output_path = os.path.join(output_folder, f"{safe_case_name}_{timestamp}_report.txt")

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if not os.path.isfile(file_path):
            continue

        content = read_file_content(file_path)

        if not content:
            continue

        if "tor.exe" in content or "firefox.exe" in content or "pid" in content or "foreignaddr" in content:
            memory_results = merge_results(memory_results, analyze_memory_file(file_path))

        if "tor.exe.pf" in content or "firefox.exe.pf" in content or "prefetch" in content or ".zip" in content:
            disk_results = merge_results(disk_results, analyze_disk_file(file_path))

        if "tls" in content or "encrypted" in content or "9050" in content or "9001" in content or "185.220." in content:
            network_results = merge_results(network_results, analyze_network_file(file_path))

        if "profile.default" in content or "places.sqlite" in content or "cookies.sqlite" in content or "tor browser" in content:
            application_results = merge_results(application_results, analyze_application_file(file_path))

    correlation_results = correlate_evidence(
        memory_results,
        disk_results,
        network_results,
        application_results
    )

    generate_report(
        memory_results,
        disk_results,
        network_results,
        application_results,
        correlation_results,
        output_path,
        case_name,
        investigator_name
    )

    return correlation_results, output_path


def main():
    results, output_path = analyze_folder("input", "output", "Default Case", "Investigator")
    print("Analysis complete.")
    print(f"Report generated: {output_path}")
    print(f"Conclusion: {results['conclusion']}")


if __name__ == "__main__":
    main()