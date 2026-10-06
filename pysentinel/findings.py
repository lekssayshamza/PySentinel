SEVERITY_LEVELS = {
    "INFO": 0,
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4,
}


def create_finding(name, severity, description):
    return {
        "name": name,
        "severity": severity,
        "description": description,
    }


def summarize_findings(findings):
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
        "INFO": 0,
    }

    for finding in findings:
        severity = finding["severity"]

        if severity in summary:
            summary[severity] += 1

    return summary
