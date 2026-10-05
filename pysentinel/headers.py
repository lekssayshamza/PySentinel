SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]


def check_security_headers(response):
    results = {}

    for header in SECURITY_HEADERS:
        results[header] = header in response.headers

    return results
