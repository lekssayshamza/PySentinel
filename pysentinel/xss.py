from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import requests

from pysentinel.findings import create_finding
from pysentinel.utils import get_parameters


def check_reflected_xss(url):
    findings = []

    parameters = get_parameters(url)

    if not parameters:
        return findings

    for parameter in parameters:
        marker = "PySentinelXSS"

        parsed_url = urlparse(url)
        query = parse_qsl(parsed_url.query, keep_blank_values=True)

        modified_query = [
            (name, marker if name == parameter else value)
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

        if marker in response.text:
            findings.append(
                create_finding(
                    f"Potential Reflected XSS: {parameter}",
                    "MEDIUM",
                    f"Parameter '{parameter}' reflects user-controlled input",
                )
            )

    return findings
