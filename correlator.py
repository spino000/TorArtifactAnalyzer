def correlate_evidence(memory_results, disk_results, network_results, application_results):

    findings = []
    score = 0

    # Memory indicators
    if memory_results["tor_process_detected"]:
        findings.append("Tor process detected in memory")
        score += 2

    if memory_results["firefox_detected"]:
        findings.append("Firefox process detected (Tor Browser uses Firefox)")
        score += 1

    if memory_results["tor_related_connections"]:
        findings.append("Tor-related network connections observed in memory")
        score += 2

    # Disk indicators
    if disk_results["tor_prefetch_found"]:
        findings.append("Tor execution evidence found in Prefetch")
        score += 2

    if disk_results["firefox_prefetch_found"]:
        findings.append("Firefox Prefetch artifact found")
        score += 1

    if disk_results["tor_folder_found"]:
        findings.append("Tor Browser directory artifacts detected")
        score += 2

    if disk_results["suspicious_archive_found"]:
        findings.append("Suspicious archive file detected (possible data staging)")
        score += 1

    # Network indicators
    if network_results["tls_detected"]:
        findings.append("Encrypted TLS traffic observed")
        score += 1

    if network_results["external_ip_detected"]:
        findings.append("External IP communication detected")
        score += 1

    if network_results["persistent_connection_detected"]:
        findings.append("Persistent TCP connection observed")
        score += 1

    if network_results["tor_like_port_detected"]:
        findings.append("Connection to Tor-like ports detected")
        score += 2

    # Application artifacts
    if application_results["tor_profile_found"]:
        findings.append("Tor browser profile directory found")
        score += 2

    if application_results["places_sqlite_found"]:
        findings.append("Browser history database detected (places.sqlite)")
        score += 1

    if application_results["cookies_sqlite_found"]:
        findings.append("Browser cookie database detected (cookies.sqlite)")
        score += 1

    # Determine conclusion
    if score >= 8:
        conclusion = "High confidence of Tor usage with possible insider data exfiltration activity"
    elif score >= 4:
        conclusion = "Moderate evidence of Tor activity detected"
    else:
        conclusion = "Low evidence of Tor activity"

    return {
        "correlation_score": score,
        "findings": findings,
        "conclusion": conclusion
    }