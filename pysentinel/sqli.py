from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import requests

from pysentinel.findings import create_finding
from pysentinel.utils import get_parameters, normalize_url


SQL_ERROR_PATTERNS = [
    "sql syntax",
    "mysql",
    "mysql_fetch",
    "ora-",
    "postgresql",
    "sqlite",
    "sqlite3",
    "sqlstate",
    "syntax error",
    "unclosed quotation mark",
]


def check_sql_injection(url):
    findings = []

    url = normalize_url(url)
    parameters = get_parameters(url)

    if not parameters:
        return findings

    parsed_url = urlparse(url)
    query = parse_qsl(parsed_url.query, keep_blank_values=True)

    for parameter in parameters:
        modified_query = [
            (name, "'" if name == parameter else value)
            for name, value in query
        ]

        test_url = urlunparse(
            parsed_url._replace(
                query=urlencode(modified_query)
            )
        )

        try:
            response = requests.get(test_url, timeout=5)
        except requests.RequestException:
            continue

        response_text = response.text.lower()

        for pattern in SQL_ERROR_PATTERNS:
            if pattern in response_text:
                findings.append(
                        create_finding(
                            f"Potential SQL Injection: {parameter}",
                            "HIGH",
                            f"Database error pattern detected after modifying parameter '{parameter}'",
                            "SQL Injection",
                        )
                )
                break

    return findings
