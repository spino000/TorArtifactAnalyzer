from memory_detector import analyze_memory
from disk_detector import analyze_disk
from network_detector import analyze_network
from application_detector import analyze_application
from correlator import correlate_evidence
from report_generator import generate_report

def main():
    # Input files
    pslist_path = "input/pslist.txt"
    netscan_path = "input/netscan.txt"
    disk_csv_path = "input/disk_artifacts.csv"
    network_summary_path = "input/network_summary.txt"
    app_artifacts_path = "input/app_artifacts.txt"

    # Run detectors
    memory_results = analyze_memory(pslist_path, netscan_path)
    disk_results = analyze_disk(disk_csv_path)
    network_results = analyze_network(network_summary_path)
    application_results = analyze_application(app_artifacts_path)

    # Correlate results
    correlation_results = correlate_evidence(
        memory_results,
        disk_results,
        network_results,
        application_results
    )

    # Generate report
    output_path = "output/tor_detection_report.txt"
    generate_report(
        memory_results,
        disk_results,
        network_results,
        application_results,
        correlation_results,
        output_path
    )

    print("Analysis complete.")
    print(f"Report generated: {output_path}")
    print(f"Conclusion: {correlation_results['conclusion']}")

if __name__ == "__main__":
    main()