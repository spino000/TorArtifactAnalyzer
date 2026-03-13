def correlate_evidence(memory_results, disk_results, network_results, application_results):
    score = 0
    findings = []

    # Memory
    if memory_results["tor_process_detected"]:
        score += 2
        findings.append("Tor process detected in memory")

    if memory_results["tor_related_connections"]:
        score += 2
        findings.append("Tor-related connections detected in memory")

    # Disk
    if disk_results["tor_prefetch_found"]:
        score += 2
        findings.append("Tor execution evidence found in prefetch")

    if disk_results["tor_folder_found"]:
        score += 1
        findings.append("Tor Browser installation/folder found")

    if disk_results["suspicious_archive_found"]:
        score += 2
        findings.append("Suspicious archive prepared for possible exfiltration")

    # Network
    if network_results["tls_detected"]:
        score += 1
        findings.append("Encrypted network traffic detected")

    if network_results["persistent_connection_detected"]:
        score += 1
        findings.append("Persistent external communication observed")

    if network_results["tor_like_port_detected"]:
        score += 2
        findings.append("Tor-like network port usage detected")

    # Application
    if application_results["tor_profile_found"]:
        score += 1
        findings.append("Tor Browser profile found")

    if application_results["places_sqlite_found"] or application_results["cookies_sqlite_found"]:
        score += 1
        findings.append("Tor browser application artifacts detected")

    # Final conclusion
    if score >= 10:
        conclusion = "High confidence of Tor usage with possible insider data exfiltration activity"
    elif score >= 6:
        conclusion = "Moderate confidence of Tor-related activity"
    elif score >= 3:
        conclusion = "Low confidence Tor-related indicators present"
    else:
        conclusion = "No significant Tor-related evidence detected"

    return {
        "correlation_score": score,
        "findings": findings,
        "conclusion": conclusion
    }