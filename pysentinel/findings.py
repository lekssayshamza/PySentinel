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
