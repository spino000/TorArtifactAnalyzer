from datetime import datetime

def generate_report(
    memory_results,
    disk_results,
    network_results,
    application_results,
    correlation_results,
    output_path,
    case_name="Unknown Case",
    investigator_name="Unknown Investigator"
):
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_path, "w", encoding="utf-8") as report:
        report.write("===== Tor Activity Detection Report =====\n\n")

        report.write(f"Case Name: {case_name}\n")
        report.write(f"Investigator: {investigator_name}\n")
        report.write(f"Generated On: {report_time}\n\n")

        report.write("MEMORY ANALYSIS\n")
        for item in memory_results["evidence"]:
            report.write(f"- {item}\n")
        report.write("\n")

        report.write("DISK ARTIFACT ANALYSIS\n")
        for item in disk_results["evidence"]:
            report.write(f"- {item}\n")
        report.write("\n")

        report.write("NETWORK TRAFFIC ANALYSIS\n")
        for item in network_results["evidence"]:
            report.write(f"- {item}\n")
        report.write("\n")

        report.write("APPLICATION ARTIFACT ANALYSIS\n")
        for item in application_results["evidence"]:
            report.write(f"- {item}\n")
        report.write("\n")

        report.write("CORRELATION FINDINGS\n")
        for finding in correlation_results["findings"]:
            report.write(f"- {finding}\n")
        report.write("\n")

        report.write(f"Correlation Score: {correlation_results['correlation_score']}\n")
        report.write(f"Conclusion: {correlation_results['conclusion']}\n")