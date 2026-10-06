from pysentinel.findings import create_finding


SECURITY_HEADERS = {
    "Content-Security-Policy": "MEDIUM",
    "Strict-Transport-Security": "MEDIUM",
    "X-Frame-Options": "MEDIUM",
    "X-Content-Type-Options": "LOW",
    "Referrer-Policy": "LOW",
}


def check_security_headers(response):
    findings = []

    for header, severity in SECURITY_HEADERS.items():
        if header not in response.headers:
            findings.append(
                create_finding(
                    header,
                    severity,
                    f"{header} is missing",
                    "Security Headers",
                )
            )

    return findings
