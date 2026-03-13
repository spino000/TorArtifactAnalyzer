def generate_report(memory_results, disk_results, network_results, application_results, correlation_results, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("===== Tor Activity Detection Report =====\n\n")

        f.write("---- Memory Evidence ----\n")
        for item in memory_results["evidence"]:
            f.write(f"[+] {item}\n")
        f.write("\n")

        f.write("---- Disk Evidence ----\n")
        for item in disk_results["evidence"]:
            f.write(f"[+] {item}\n")
        f.write("\n")

        f.write("---- Network Evidence ----\n")
        for item in network_results["evidence"]:
            f.write(f"[+] {item}\n")
        f.write("\n")

        f.write("---- Application Evidence ----\n")
        for item in application_results["evidence"]:
            f.write(f"[+] {item}\n")
        f.write("\n")

        f.write("---- Correlation Summary ----\n")
        for item in correlation_results["findings"]:
            f.write(f"[+] {item}\n")

        f.write(f"\nCorrelation Score: {correlation_results['correlation_score']}\n")
        f.write(f"Conclusion: {correlation_results['conclusion']}\n")